// Function to update the icon based on online status
function updateStatusIcon() {
     const sIcon = document.getElementById('alart');
        const offlineAlert = sIcon.children[0];
        const onlineAlert = sIcon.children[1];
        if (navigator.onLine) {
            onlineAlert.classList.remove('hidden');
            offlineAlert.classList.add('hidden');
            setTimeout(() => {
                onlineAlert.classList.add('hidden');
            }, 5000); // Hide the online alert after 5 seconds
            if (!sessionStorage.getItem('refreshed')) {
                sessionStorage.setItem('refreshed', 'true');
                location.reload();
            }
        } else {
                    offlineAlert.classList.remove('hidden');
                    onlineAlert.classList.add('hidden');
                    sessionStorage.removeItem('refreshed'); // Reset the refresh flag when offline
                }
    
      const statusIcon = document.getElementById('net');
      if (navigator.onLine) {
        statusIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="M480-150q-21 0-35.5-14.5T430-200q0-21 14.5-35.5T480-250q21 0 35.5 14.5T530-200q0 21-14.5 35.5T480-150ZM254-346l-28-28q50-50 114.67-78 64.66-28 139.5-28 74.83 0 139.33 28Q684-424 734-374l-28 28q-44-44-102-69t-124-25q-66 0-124 25t-102 69ZM84-516l-28-28q81-81 189-128.5T480-720q127 0 235 47.5T904-544l-28 28q-77-77-178.5-120.5T480-680q-116 0-217.5 43.5T84-516Z"/></svg>'; // Online icon
        statusIcon.className = 'icon online';
      } else {
        statusIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#fff"><path d="m796.5-125-316-317.5q-65-.5-124.5 24.5t-100 68l-25.5-24.5q41-41 96.75-69.75T445.5-478l-161-161q-47 16.5-99.75 50.25T91.5-514.5L68-539q42-42 92-77t95-52.5L159-765l18-18 639.5 639.5-20 18.5ZM480-156.5q-20 0-33.75-13.5t-13.75-34q0-19.5 13.75-33.5t33.75-14q20 0 33.75 14T527.5-204q0 20.5-13.75 34T480-156.5Zm233.5-204-13-13-13-13-62-62q18 7.5 47.25 26t56.75 46l-16 16Zm155.5-154q-76.5-76-176.25-118.5T480-675.5q-21 0-40.75 1.5t-34.75 4l-33-33q19.5-4 45-6.25t63.5-2.25q122 0 227 45.25T894-539l-25 24.5Z"/></svg>'; // Offline icon
        statusIcon.className = 'icon offline';
      }
    }

    // Check status when the page loads
    updateStatusIcon();

    // Listen for online and offline events
    window.addEventListener('online', updateStatusIcon);
    window.addEventListener('offline', updateStatusIcon);
// -----------------------------------
        // Clock Update
        let is24Hour = false;
        const clockElement = document.getElementById('clock');
        const dateElement = document.getElementById('date');
        const menuIcon = document.getElementById('menuIcon');
        const menu = document.getElementById('menu');
        const formatSwitch = document.getElementById('formatSwitch');

        function updateClock() {
            const now = new Date();
            let hours = now.getHours();
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            let timeString;

            if (is24Hour) {
                timeString = `${String(hours).padStart(2, '0')}<span class="time-separator">:</span>${minutes}<span class="time-separator">:</span>${seconds}`;
            } else {
                const period = hours >= 12 ? 'PM' : 'AM';
                hours = hours % 12 || 12;
                timeString = `${hours}<span class="time-separator">:</span>${minutes}<span class="time-separator">:</span>${seconds} ${period}`;
            }

            clockElement.innerHTML = timeString;

            const options = { 
                weekday: 'long', 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            };
            dateElement.textContent = now.toLocaleDateString('en-US', options);
        }

        menuIcon.addEventListener('click', (e) => {
            e.stopPropagation();
            menu.classList.toggle('show');
        });

        formatSwitch.addEventListener('click', () => {
            is24Hour = !is24Hour;
                        updateClock();formatSwitch.innerHTML = is24Hour ? '<img width="24" height="24" src="https://img.icons8.com/color-glass/24/last-12-hours.png" alt="24 To 12"/>' : '<img width="24" height="24" src="https://img.icons8.com/color-glass/24/last-24-hours.png" alt="12 To 24"/>';

            menu.classList.remove('show');
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!menu.contains(e.target)) {
                menu.classList.remove('show');
            }
        });

        updateClock();
        setInterval(updateClock, 1000);

        // Toggle Google Apps Display
        const toggleAppsButton = document.getElementById("toggleAppsButton");
        const googleAppsContainer = document.getElementById("googleAppsContainer");

        toggleAppsButton.addEventListener("click", () => {
            const isHidden = googleAppsContainer.style.display === "none" || googleAppsContainer.style.display === "";
            googleAppsContainer.style.display = isHidden ? "flex" : "none";
            toggleAppsButton.innerHTML = isHidden ? '<svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#FFFFFF"><path d="M400-528q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2Zm0 160q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2ZM280-540q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm120 280q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6ZM280-380q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm120-280q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm160 132q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2Zm0-132q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm120 280q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm0-160q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6ZM480.17-132q-72.17 0-135.73-27.39-63.56-27.39-110.57-74.35-47.02-46.96-74.44-110.43Q132-407.65 132-479.83q0-72.17 27.39-135.73 27.39-63.56 74.35-110.57 46.96-47.02 110.43-74.44Q407.65-828 479.83-828q72.17 0 135.73 27.39 63.56 27.39 110.57 74.35 47.02 46.96 74.44 110.43Q828-552.35 828-480.17q0 72.17-27.39 135.73-27.39 63.56-74.35 110.57-46.96 47.02-110.43 74.44Q552.35-132 480.17-132Zm-.17-28q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm80-100q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm0-108q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2Zm-80-112Z"/></svg>' : '<svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#FFFFFF"><path d="M120-380q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-160q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm120 332q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm160.24 332Q382-356 369-368.76q-13-12.77-13-31Q356-418 368.76-431q12.77-13 31-13Q418-444 431-431.24q13 12.77 13 31Q444-382 431.24-369q-12.77 13-31 13Zm0-160Q382-516 369-528.76q-13-12.77-13-31Q356-578 368.76-591q12.77-13 31-13Q418-604 431-591.24q13 12.77 13 31Q444-542 431.24-529q-12.77 13-31 13ZM400-208q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-480q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0 588q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-720q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm160.24 464Q542-356 529-368.76q-13-12.77-13-31Q516-418 528.76-431q12.77-13 31-13Q578-444 591-431.24q13 12.77 13 31Q604-382 591.24-369q-12.77 13-31 13Zm0-160Q542-516 529-528.76q-13-12.77-13-31Q516-578 528.76-591q12.77-13 31-13Q578-604 591-591.24q13 12.77 13 31Q604-542 591.24-529q-12.77 13-31 13ZM560-208q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-480q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0 588q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-720q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm160 612q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm120 308q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-160q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Z"/></svg>';
            toggleAppsButton.style.background = isHidden ? "linear-gradient(135deg, #ec5a97, #2022559d, #202255)" : "rgba(0, 0, 0, 0.2)";
            toggleAppsButton.onmouseover = () => {
                toggleAppsButton.style.background = isHidden ? "rgba(0, 0, 0, 0.2)" : "rgba(0, 0, 0, 0.2)";
            };
            toggleAppsButton.onmouseout = () => {
                toggleAppsButton.style.background = isHidden ? "linear-gradient(135deg, #ec5a97, #2022559d, #202255)" : "rgba(0, 0, 0, 0.2)";
            };
        });

        // Search Form Functionality
        document.getElementById("searchForm").addEventListener("submit", function (e) {
            e.preventDefault();
            const input = document.getElementById("urlInput").value;
            const url = input.startsWith("http://") || input.startsWith("https://") ? input : "https://www.google.com/search?q=" + encodeURIComponent(input);
            window.location.href = url;
        });

// wheather open & close
document.querySelector('.sea.icon').addEventListener('click', function () {
    document.querySelector('.card').classList.remove('hidden');
});

document.querySelector('.close').addEventListener('click', function () {
    document.querySelector('.card').classList.add('hidden');
});

// Weather API workings--------------------------------------------------------------------------------------------------------------------------------
let weather = {
    apiKey: "67b92f0af5416edbfe58458f502b0a31",
    fetchWeatherByCity: function (city) {
        fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${this.apiKey}`
        )
            .then((response) => {
                if (!response.ok) {
                    alert("No weather found.");
                    throw new Error("No weather found.");
                }
                return response.json();
            })
            .then((data) => this.displayWeather(data));
    },

    fetchWeatherByCoords: function (lat, lon) {
        fetch(
            `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${this.apiKey}`
        )
            .then((response) => {
                if (!response.ok) {
                    this.showSearchInterface();
                    throw new Error("No weather found.");
                }
                return response.json();
            })
            .then((data) => this.displayWeather(data));
    },

    displayWeather: function (data) {
        const { name } = data;
        const { icon, description } = data.weather[0];
        const { temp, humidity } = data.main;
        const { speed } = data.wind;
        document.querySelector(".city").innerText = "Weather in " + name;
        document.querySelector(".iconi").src =
            "https://openweathermap.org/img/wn/" + icon + ".png";
        document.querySelector(".description").innerText = description;
        document.querySelector(".temp").innerText = temp + "°C";
        document.querySelector(".humidity").innerText =
            "Humidity : " + humidity + "%";
        document.querySelector(".wind").innerText =
            "Wind speed : " + speed + " km/h";
        document.querySelector(".weather").classList.remove("loading");
        document.querySelector("#searchPrompt").style.display = "none";
        document.querySelector(".weather").style.display = "block";
    },

    showSearchInterface: function() {
        document.querySelector(".weather").style.display = "none";
        document.querySelector("#searchPrompt").style.display = "block";
    },

    search: function () {
        const searchValue = document.querySelector(".search-bar").value;
        if (searchValue) {
            this.fetchWeatherByCity(searchValue);
        }
    },

    getLocation: function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;
                    this.fetchWeatherByCoords(lat, lon);
                },
                (error) => {
                    console.error(error);
                    this.showSearchInterface();
                }
            );
        } else {
            this.showSearchInterface();
        }
    }
};

// Search button click event
document.querySelector(".search-btn").addEventListener("click", function () {
    weather.search();
});

// Enter key press event
document.querySelector(".search-bar").addEventListener("keyup", function (event) {
    if (event.key == "Enter") {
        weather.search();
    }
});

// Get location automatically when page loads
weather.getLocation();
// ----------------------------------------------------------------------------------------------------------------------------------------------------