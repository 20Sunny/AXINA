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
    <title>Axina Browser</title>
    <!-- Include Font Awesome for icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
        
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            background: url(./pxfuel.jpg) no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-align: center;
        }

        p {
            font-size: 1.2rem;
            opacity: 0.8;
            margin-bottom: 30px;
            text-align: center;
        }

        #clock {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 1.2rem;
            background: rgba(0, 0, 0, 0.5);
            padding: 10px 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        form {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }

        input {
            padding: 12px 16px;
            border: none;
            border-radius: 8px;
            width: 300px;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            backdrop-filter: blur(10px);
            outline: none;
            transition: all 0.3s ease;
        }

        input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        input:focus {
            background: rgba(255, 255, 255, 0.2);
            transform: scale(1.05);
        }

        button {
            padding: 12px 20px;
            font-size: 1rem;
            color: #fff;
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }

        #socialIconsContainer {
            display: flex;
            gap: 20px;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            margin-top: 20px;
            padding: 10px 20px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            max-width: 80%;
        }

        #socialIconsContainer a {
            font-size: 1.5rem;
            color: #fff;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        #socialIconsContainer a:hover {
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            transform: scale(1.1);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }

        #googleAppsContainer {
            display: none;
            max-width: 70vw;
            position: fixed;
            flex-wrap: wrap;
            gap: 25px;
            justify-content: center;
            align-items: center;
            padding: 25px 10px;
            backdrop-filter: blur(3px);
            background: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        #googleAppsContainer a {
            font-size: 1.5rem;
            color: #fff;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        #googleAppsContainer a:hover {
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            transform: scale(1.1);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }

        #toggleAppsButton {
            position: fixed;
            top: 20px;
            left: 20px;
            font-size: 1.8rem;
            background: rgba(0, 0, 0, 0.5);
            color: #fff;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        #toggleAppsButton:hover {
            background: linear-gradient(135deg, #43e97b, #38f9d7);
        }
        #speedMeterContainer {
            position: fixed;
            display: flex;
            align-items: center;
            justify-content: center;
            bottom: 30px;
            right: 30px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        #speedMeterContainer h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
            color: #fff;
        }

        canvas {
            display: block;
            margin: auto;
        }
    </style>
</head>
<body>
    <div id="clock"></div>
    <h1>Welcome to Axina Browser</h1>
    <p>Your personal, Python-powered browser with modern features!</p>
    <form id="searchForm">
        <input type="text" id="urlInput" placeholder="Enter URL or search...">
        <button type="submit">Go</button>
    </form>
    <div id="speedMeterContainer">
        <canvas id="speedMeter" width="150" height="150"></canvas>
    </div>
    <!-- Social Media Icons Section -->
    <div id="socialIconsContainer">
        <a href="https://facebook.com" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
        <a href="https://twitter.com" target="_blank" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
        <a href="https://instagram.com" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
        <a href="https://linkedin.com" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
        <a href="https://github.com" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
    </div>

    <!-- Toggle Button for Google Apps -->
    <button id="toggleAppsButton" aria-label="Toggle Apps"><i class="fas fa-th"></i></button>

    <!-- Google Apps Section -->
    <div id="googleAppsContainer">
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
        <a href="https://mail.google.com/" target="_blank" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
        <a href="https://www.google.com/drive/" target="_blank" aria-label="Google Drive"><i class="fas fa-cloud"></i></a>
        <a href="https://calendar.google.com/" target="_blank" aria-label="Google Calendar"><i class="fas fa-calendar-alt"></i></a>
        <a href="https://www.google.com/maps/" target="_blank" aria-label="Google Maps"><i class="fas fa-map-marked-alt"></i></a>
        <a href="https://www.youtube.com/" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="https://www.google.com/photos/" target="_blank" aria-label="Google Photos"><i class="fas fa-camera"></i></a>
        <a href="https://docs.google.com/" target="_blank" aria-label="Google Docs"><i class="fas fa-file-alt"></i></a>
        <a href="https://sheets.google.com/" target="_blank" aria-label="Google Sheets"><i class="fas fa-table"></i></a>
        <a href="https://slides.google.com/" target="_blank" aria-label="Google Slides"><i class="fas fa-presentation"></i></a>
    </div>

    <script>
// -----------------------------------
// Speed Meter Script
const canvas = document.getElementById('speedMeter');
        const ctx = canvas.getContext('2d');
        let speed = 0;

        // Function to draw the speed meter
        function drawSpeedMeter(currentSpeed) {
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            const radius = 50;

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw meter background
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0.75 * Math.PI, 2.25 * Math.PI);
            ctx.lineWidth = 10;
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.stroke();
            ctx.closePath();

            // Draw active speed arc
            const endAngle = (0.75 + (currentSpeed / 100) * 1.5) * Math.PI;
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0.75 * Math.PI, endAngle);
            ctx.lineWidth = 10;
            ctx.strokeStyle = 'rgb(67, 233, 123)';
            ctx.stroke();
            ctx.closePath();

            // Draw center text
            ctx.font = '10px Inter';
            ctx.fillStyle = '#fff';
            ctx.textAlign = 'center';
            ctx.fillText(`${currentSpeed} Mbps`, centerX, centerY + 10);
        }

        // Simulate speed changes
        function updateSpeed() {
            speed = Math.floor(Math.random() * 101); // Random speed between 0 and 100 Mbps
            drawSpeedMeter(speed);
        }

        // Update speed meter every second
        setInterval(updateSpeed, 1000);
// -----------------------------------
        // Clock Update
        function updateClock() {
            const now = new Date();
            document.getElementById("clock").textContent = now.toLocaleTimeString();
        }
        setInterval(updateClock, 1000);
        updateClock();

        // Toggle Google Apps Display
        const toggleAppsButton = document.getElementById("toggleAppsButton");
        const googleAppsContainer = document.getElementById("googleAppsContainer");

        toggleAppsButton.addEventListener("click", () => {
            const isHidden = googleAppsContainer.style.display === "none" || googleAppsContainer.style.display === "";
            googleAppsContainer.style.display = isHidden ? "flex" : "none";
            toggleAppsButton.innerHTML = isHidden ? '<i class="fas fa-times"></i>' : '<i class="fas fa-th"></i>';
        });

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
        self.tabs.currentWidget().setZoomFactor(self.current_zoom_level)

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