import sys
import os
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPositioning import *
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QToolBar,
    QLabel,
    QAction,
    QLineEdit,
    QFileDialog,
    QMessageBox,
    QPlainTextEdit,
    QMenuBar,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineDownloadItem, QWebEngineSettings, QWebEnginePage, QWebEngineProfile
from PyQt5.QtGui import QIcon, QFont

# Global variable to store the main window instance
main_window = None

class WebEnginePage(QWebEnginePage):
    def createWindow(self, _type):
        if _type == QWebEnginePage.WebBrowserTab:
            new_tab = main_window.create_new_tab_return_view()
            return new_tab.page()
        return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set global reference
        global main_window
        main_window = self
        
        # Set up location permissions globally
        profile = QWebEngineProfile.defaultProfile()
        settings = profile.settings()
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        settings.setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)  # Enable DNS prefetching
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        self.setWindowTitle("Axina Browser")
        self.setWindowIcon(QIcon("browser_icon.png"))
        self.showMaximized()

        # Create menu bar
        menubar = self.menuBar()
        view_menu = menubar.addMenu('View')
        
        # Add "View Source" action
        view_source_action = QAction('View Page Source', self)
        view_source_action.setShortcut('Ctrl+U')
        view_source_action.triggered.connect(self.view_page_source)
        view_menu.addAction(view_source_action)

        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(lambda _: self.add_new_tab())
        self.tabs.currentChanged.connect(self.update_current_tab)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        # Add navigation bar
        navbar = QToolBar("Navigation")
        navbar.setIconSize(QSize(20, 20))
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction(QIcon("left.png"), "Back", self)
        back_btn.triggered.connect(self.navigate_back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction(QIcon("right.png"), "Forward", self)
        forward_btn.triggered.connect(self.navigate_forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction(QIcon("refresh.png"), "Reload", self)
        reload_btn.triggered.connect(self.reload_page)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction(QIcon("home.png"), "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # New Tab button
        new_tab_btn = QAction(QIcon("new_tab.png"), "New Tab", self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Zoom In button
        zoom_in_btn = QAction(QIcon("plus.png"), "Zoom In", self)
        zoom_in_btn.triggered.connect(self.zoom_in)
        navbar.addAction(zoom_in_btn)

        # Zoom Percentage Label
        self.zoom_label = QLabel("100%")
        navbar.addWidget(self.zoom_label)

        # Zoom Out button
        zoom_out_btn = QAction(QIcon("minus.png"), "Zoom Out", self)
        zoom_out_btn.triggered.connect(self.zoom_out)
        navbar.addAction(zoom_out_btn)

        #view source code
        view_source_btn = QAction(QIcon("source.jpg"), "View Source", self)
        view_source_btn.setShortcut('Ctrl+U')
        view_source_btn.triggered.connect(self.view_page_source)
        navbar.addAction(view_source_btn)

        # Current zoom level Sunny@bca
        self.current_zoom_level = 1.2

        # Add first tab
        self.add_new_tab(QUrl("https://axina.netlify.app"), "Home")

    def view_page_source(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.page().toHtml(self.show_source_code)

    def show_source_code(self, html_content):
        # Create new window for source code
        source_window = QMainWindow(self)
        source_window.setWindowTitle("Page Source")
        source_window.resize(800, 600)

        # Create text edit widget
        text_edit = QPlainTextEdit()
        text_edit.setPlainText(html_content)
        text_edit.setReadOnly(True)
        
        # Set monospace font for better code readability
        font = QFont("Courier")
        font.setStyleHint(QFont.Monospace)
        text_edit.setFont(font)

        source_window.setCentralWidget(text_edit)
        source_window.show()

    # ... (rest of your existing methods remain exactly the same)
    def create_new_tab_return_view(self):
        browser = QWebEngineView()
        page = WebEnginePage(browser)
        browser.setPage(page)
        
        # Set up the new tab
        browser.page().profile().downloadRequested.connect(self.handle_download)
        browser.page().featurePermissionRequested.connect(self.handle_permission_request)
        
        i = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(i)
        
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_url(qurl, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.update_tab_title(i, browser))
        
        return browser

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl("https://axina.netlify.app")
        elif isinstance(qurl, bool):
            qurl = QUrl("https://axina.netlify.app")
        elif not isinstance(qurl, QUrl):
            qurl = QUrl(qurl)

        browser = QWebEngineView()
        page = WebEnginePage(browser)
        browser.setPage(page)
        browser.setUrl(qurl)
        browser.page().profile().downloadRequested.connect(self.handle_download)
        browser.page().featurePermissionRequested.connect(self.handle_permission_request)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_url(qurl, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.update_tab_title(i, browser))

    def handle_permission_request(self, origin, feature):
        if feature == QWebEnginePage.Geolocation:
            current_browser = self.tabs.currentWidget()
            current_browser.page().setFeaturePermission(
                origin,
                feature,
                QWebEnginePage.PermissionGrantedByUser
            )

    def update_tab_title(self, i, browser):
        if i >= 0:  # Add check to prevent index error
            title = browser.page().title()
            if title:  # Only update if there's a title
                self.tabs.setTabText(i, title)

    def update_url(self, qurl, browser):
        if browser == self.tabs.currentWidget():
            self.url_bar.setText(qurl.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(("http://", "https://", "file:///")):
            url = "http://" + url
        self.tabs.currentWidget().setUrl(QUrl(url))

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://axina.netlify.app"))

    def navigate_back(self):
        self.tabs.currentWidget().back()

    def navigate_forward(self):
        self.tabs.currentWidget().forward()

    def reload_page(self):
        self.tabs.currentWidget().reload()

    def update_current_tab(self, i):
        if i >= 0:
            browser = self.tabs.widget(i)
            if browser:
                self.update_url(browser.url(), browser)

    def close_current_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)

    def handle_download(self, download_item: QWebEngineDownloadItem):
        original_filename = os.path.basename(download_item.url().toString())
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", original_filename)
        if save_path:
            download_item.setPath(save_path)
            download_item.accept()
            download_item.finished.connect(
                lambda: QMessageBox.information(self, "Download Complete", f"File downloaded to: {save_path}")
            )
        else:
            download_item.cancel()

    def zoom_in(self):
        self.current_zoom_level += 0.1
        self.tabs.currentWidget().setZoomFactor(self.current_zoom_level)
        self.update_zoom_label()

    def zoom_out(self):
        self.current_zoom_level -= 0.1
        self.tabs.currentWidget().setZoomFactor(self.current_zoom_level)
        self.update_zoom_label()

    def update_zoom_label(self):
        zoom_percentage = int((self.current_zoom_level) * 100)
        self.zoom_label.setText(f"{zoom_percentage}%")

# Application Entry Point
app = QApplication(sys.argv)
QApplication.setApplicationName("Axina Browser")
window = MainWindow()
app.exec_()