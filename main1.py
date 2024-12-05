import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtGui import QIcon, QPixmap

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

# Save the home page to a local file
def save_home_page():
    with open("homepage.html", "w") as file:
        file.write(HOME_PAGE_HTML)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Save the home page HTML locally
        save_home_page()

        # Set up the browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile(os.path.abspath("homepage.html")))
        self.browser.urlChanged.connect(self.update_url)
        self.browser.titleChanged.connect(self.update_title)
        self.browser.loadFinished.connect(self.update_status)

        self.setCentralWidget(self.browser)
        self.setWindowIcon(QIcon("browser_icon.png"))  # Add a custom icon if available
        self.showMaximized()

        # Set default zoom level to 120%
        self.current_zoom = 1.2
        self.browser.setZoomFactor(self.current_zoom)

        # Create Navbar
        navbar = QToolBar("Navigation")
        navbar.setIconSize(QSize(20, 20))
        self.addToolBar(navbar)

        # Back Button with Icon
        back_btn = QAction(QIcon("left.png"), "Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward Button with Icon
        forward_btn = QAction(QIcon("right.png"), "Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Refresh Button with Icon
        refresh_btn = QAction(QIcon("refresh.png"), "Refresh", self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        # Home Button with Icon
        home_btn = QAction(QIcon("home.png"), "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or search...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Zoom In Button
        zoom_in_btn = QAction(QIcon("plus.png"), "Zoom In", self)
        zoom_in_btn.triggered.connect(self.zoom_in)
        navbar.addAction(zoom_in_btn)

        # Zoom Percentage Label
        self.zoom_label = QLabel("100%")
        navbar.addWidget(self.zoom_label)

        # Zoom Out Button
        zoom_out_btn = QAction(QIcon("minus.png"), "Zoom Out", self)
        zoom_out_btn.triggered.connect(self.zoom_out)
        navbar.addAction(zoom_out_btn)

        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def navigate_home(self):
        # Load the custom home page
        home_path = os.path.abspath("homepage.html")
        self.browser.setUrl(QUrl.fromLocalFile(home_path))

    def navigate_to_url(self):
        user_input = self.url_bar.text()
        # Check if input looks like a URL
        if "." in user_input and not user_input.startswith("http"):
            user_input = "http://" + user_input
        elif not user_input.startswith("http") and not "." in user_input:
            # Treat as a Google search query
            user_input = f"https://www.google.com/search?q={user_input}"
        self.browser.setUrl(QUrl(user_input))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def update_title(self, title):
        self.setWindowTitle(title + " - Axina")

    def update_status(self):
        self.status_bar.showMessage("Page Loaded", 2000)  # Message stays for 2 seconds

    def zoom_in(self):
        self.current_zoom += 0.1
        self.browser.setZoomFactor(self.current_zoom)
        self.update_zoom_label()

    def zoom_out(self):
        self.current_zoom -= 0.1
        if self.current_zoom < 0.5:  # Minimum zoom level
            self.current_zoom = 0.5
        self.browser.setZoomFactor(self.current_zoom)
        self.update_zoom_label()

    def update_zoom_label(self):
        zoom_percentage = int(self.current_zoom * 100)
        self.zoom_label.setText(f"{zoom_percentage}%")
        self.status_bar.showMessage(f"{zoom_percentage}%", 2000)

# Application Entry Point
app = QApplication(sys.argv)
QApplication.setApplicationName('Axina Browser')

window = MainWindow()
app.exec_()
