import sys
import os
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QToolBar,
    QLabel,
    QAction,
    QLineEdit,
    QFileDialog,
    QMessageBox,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineDownloadItem
from PyQt5.QtGui import QIcon

# HTML content for the custom home page
HOME_PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Axina Browser Home</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&display=swap');
        body {
            font-family: "Caveat", cursive;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
            background: url(./pxfuel.jpg) no-repeat center center fixed;
            background-size: cover;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            color: #333;
        }
        input {
            padding: 10px;
            width: 300px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-top: 20px;
        }
        button {
            padding: 10px 15px;
            background: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #45a049;
        }
        #clock {
            position: absolute;
            top: 10px;
            right: 20px;
            font-size: 48px;
            color: #fff;
            background: rgba(0, 0, 0, 0.5);
            padding: 5px 10px;
            border-radius: 5px;
        }
        #speedTest {
            position: absolute;
            bottom: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.5);
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
            text-align: center;
        }
        #speedTest div {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div id="clock"></div>
    <h1>Welcome to Axina Browser</h1>
    <p>Your personal, Python-powered browser!</p>
    <form id="searchForm">
        <input type="text" id="urlInput" placeholder="Enter URL or search...">
        <button type="submit">Go</button>
    </form>

    <!-- Speed Test Section -->
    <div id="speedTest">
        <div>Download Speed: <span id="downloadSpeed">--</span> Mbps</div>
        <div>Upload Speed: <span id="uploadSpeed">--</span> Mbps</div>
    </div>

    <script>
        // Digital Clock in 12-hour format with AM/PM
        function updateClock() {
            const now = new Date();
            let hours = now.getHours();
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            const ampm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12 || 12; // Convert to 12-hour format
            document.getElementById("clock").textContent = `${hours}:${minutes}:${seconds} ${ampm}`;
        }
        setInterval(updateClock, 1000);
        updateClock();
// -------------------------------------------------------------------------------------------------------------------
        // Function to test internet speed
        async function testInternetSpeed() {
            const downloadSize = 2 * 1024 * 1024; // 5 MB
            const uploadSize = 2 * 1024 * 1024; // 1 MB
            const downloadUrl = "https://via.placeholder.com/1024x1024?text=Download+Speed&random=" + Math.random();
            const uploadData = new Blob([new Uint8Array(uploadSize)]);

            // Measure Download Speed
            const startDownload = performance.now();
            await fetch(downloadUrl).catch(() => null);
            const endDownload = performance.now();
            const downloadDuration = (endDownload - startDownload) / 1000; // seconds
            const downloadSpeed = downloadDuration > 0 ? ((downloadSize * 8) / (downloadDuration * 1024 * 1024)) : 0;

            // Measure Upload Speed
            const startUpload = performance.now();
            await fetch("https://httpbin.org/post", {
                method: "POST",
                body: uploadData,
            }).catch(() => null);
            const endUpload = performance.now();
            const uploadDuration = (endUpload - startUpload) / 1000; // seconds
            const uploadSpeed = uploadDuration > 0 ? ((uploadSize * 8) / (uploadDuration * 1024 * 1024)) : 0;

            // Update the UI
            document.getElementById("downloadSpeed").textContent = downloadSpeed.toFixed(2);
            document.getElementById("uploadSpeed").textContent = uploadSpeed.toFixed(2);
        }

        // Auto-update internet speed every 5 seconds
        setInterval(testInternetSpeed, 500);
        testInternetSpeed(); // Initial test
//--------------------------------------------------------------------------------------------------------------------------
        // Search Form Functionality
        document.getElementById("searchForm").addEventListener("submit", function (e) {
            e.preventDefault();
            const input = document.getElementById("urlInput").value;
            const url = input.startsWith("http://") || input.startsWith("https://") ? input : "https://www.google.com/search?q=" + encodeURIComponent(input);
            window.location.href = url;
        });
    </script>
</body>
</html>
"""

# Save the home page HTML locally
def save_home_page():
    with open("homepage.html", "w") as file:
        file.write(HOME_PAGE_HTML)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Save the home page locally
        save_home_page()

        self.setWindowTitle("Axina Browser")
        self.setWindowIcon(QIcon("browser_icon.png"))
        self.showMaximized()

        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(lambda: self.add_new_tab())
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
        new_tab_btn.triggered.connect(lambda: self.add_new_tab())
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


        # Add first tab
        self.add_new_tab(QUrl.fromLocalFile(os.path.abspath("homepage.html")), "Home")

        # Current zoom level
        self.current_zoom_level = 1.2

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl.fromLocalFile(os.path.abspath("homepage.html"))

        browser = QWebEngineView()
        browser.setUrl(qurl)
        browser.page().profile().downloadRequested.connect(self.handle_download)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_url(qurl, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.update_tab_title(i, browser))

    def update_tab_title(self, i, browser):
        title = browser.page().title()
        self.tabs.setTabText(i, title)

    def update_url(self, qurl, browser):
        if browser == self.tabs.currentWidget():
            self.url_bar.setText(qurl.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.tabs.currentWidget().setUrl(QUrl(url))

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl.fromLocalFile(os.path.abspath("homepage.html")))

    def navigate_back(self):
        self.tabs.currentWidget().back()

    def navigate_forward(self):
        self.tabs.currentWidget().forward()

    def reload_page(self):
        self.tabs.currentWidget().reload()

    def update_current_tab(self, i):
        if i >= 0:
            browser = self.tabs.widget(i)
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

    # Zoom In function
    def zoom_in(self):
        self.current_zoom_level += 0.1
        self.tabs.currentWidget().setZoomFactor(self.current_zoom_level)
        self.update_zoom_label()

    # Zoom Out function
    def zoom_out(self):
        self.current_zoom_level -= 0.1
        self.tabs.currentWidget().setZoomFactor(self.current_zoom_level)
        self.update_zoom_label()

    # Update Zoom Label
    def update_zoom_label(self):
        zoom_percentage = int((self.current_zoom_level - 0.2) * 100)
        self.zoom_label.setText(f"{zoom_percentage}%")

# Application Entry Point
app = QApplication(sys.argv)
QApplication.setApplicationName("Axina Browser")

window = MainWindow()
app.exec_()
