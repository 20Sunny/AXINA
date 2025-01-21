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
    
    svgIcons: {
        humidity: `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="M559.88-286q14.12 0 24.12-9.88 10-9.88 10-24T584.12-344q-9.88-10-24-10T536-344.12q-10 9.88-10 24t9.88 24.12q9.88 10 24 10ZM378-279l223-223-19-20-224 224 20 19Zm21.88-167q14.12 0 24.12-9.88 10-9.88 10-24T424.12-504q-9.88-10-24-10T376-504.12q-10 9.88-10 24t9.88 24.12q9.88 10 24 10Zm79.94 314Q365-132 288.5-211.1T212-408q0-82 66.5-182.5T480-812q135 121 201.5 221.5T748-408q0 117.8-76.68 196.9-76.69 79.1-191.5 79.1Zm.18-28q104 0 172-70.5T720-408q0-73-60.5-165T480-774Q361-665 300.5-573T240-408q0 107 68 177.5T480-160Zm0-312Z"/></svg>`,
        
        wind: `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="M460-198q-32 0-56.5-19.5T370-266h30q8 18 24 29t36 11q27 0 46.5-19.5T526-292q0-27-19.5-46.5T460-358H106v-28h354q39 0 66.5 27.5T554-292q0 39-27.5 66.5T460-198ZM106-574v-28h514q36 0 61-25t25-61q0-36-25-61t-61-25q-30 0-52 17t-30 43h-30q9-39 40-63.5t72-24.5q48 0 81 33t33 81q0 48-33 81t-81 33H106Zm660 306v-30q26-8 43-30t17-52q0-36-25-61t-61-25H106v-28h634q48 0 81 33t33 81q0 41-24.5 72T766-268Z"/></svg>`,
        
        pressure: `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="M212-464v-28h536v28H212Zm0-108v-28h536v28H212Zm254 440v-176l-90 90-20-20 124-124 124 124-20 20-90-90v176h-28Zm14-570L356-826l20-20 90 90v-176h28v176l90-90 20 20-124 124Z"/></svg>`,
        
        aqi: `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="m730-287-23-35q-17 9-35 14t-38 5q-66 0-111.5-45.5T477-460q0-66 45.5-111.5T633-617q65 0 110 46t45 111q0 36-15 67.5T730-338l23 35-23 16Zm-558-23 116-300h33l118 300h-32l-28-74H232l-28 74h-32Zm461-21q15 0 29.5-3.5T691-346l-36-54 23-16 36 54q21-19 32.5-44t11.5-54q0-53-36-91t-89-38q-53 0-89.5 37.5T507-460q0 54 36.5 91.5T633-331Zm-391-78h128l-63-163h-4l-61 163Z"/></svg>`,

        city: `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="M226-164v-508h160v-146l94-88 94 88v306h160v348H226Zm28-28h132v-132H254v132Zm0-160h132v-132H254v132Zm0-160h132v-132H254v132Zm160 320h132v-132H414v132Zm0-160h132v-132H414v132Zm0-160h132v-132H414v132Zm0-160h132v-132H414v132Zm160 480h132v-132H574v132Zm0-160h132v-132H574v132Z"/></svg>`,

        visible: `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="M480.24-364q56.76 0 96.26-39.74 39.5-39.73 39.5-96.5 0-56.76-39.74-96.26-39.73-39.5-96.5-39.5-56.76 0-96.26 39.74-39.5 39.73-39.5 96.5 0 56.76 39.74 96.26 39.73 39.5 96.5 39.5Zm-.24-28q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm.14 140Q355-252 252-319.5 149-387 96-500q53-113 155.86-180.5 102.85-67.5 228-67.5Q605-748 708-680.5 811-613 864-500q-53 113-155.86 180.5-102.85 67.5-228 67.5ZM480-500Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z"/></svg>`,

        map: `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFFFF"><path d="m334-334 218-74 74-218-218 74-74 218Zm145.76-106q-16.76 0-28.26-11.74-11.5-11.73-11.5-28.5 0-16.76 11.74-28.26 11.73-11.5 28.5-11.5 16.76 0 28.26 11.74 11.5 11.73 11.5 28.5 0 16.76-11.74 28.26-11.73 11.5-28.5 11.5Zm.41 308q-72.17 0-135.73-27.39-63.56-27.39-110.57-74.35-47.02-46.96-74.44-110.43Q132-407.65 132-479.83q0-72.17 27.39-135.73 27.39-63.56 74.35-110.57 46.96-47.02 110.43-74.44Q407.65-828 479.83-828q72.17 0 135.73 27.39 63.56 27.39 110.57 74.35 47.02 46.96 74.44 110.43Q828-552.35 828-480.17q0 72.17-27.39 135.73-27.39 63.56-74.35 110.57-46.96 47.02-110.43 74.44Q552.35-132 480.17-132Zm-.17-28q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg>`
    },

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
            .then((data) => {
                const lat = data.coord.lat;
                const lon = data.coord.lon;
                return Promise.all([
                    Promise.resolve(data),
                    fetch(
                        `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${this.apiKey}`
                    ).then(response => response.json())
                ]);
            })
            .then(([weatherData, aqiData]) => {
                this.displayWeather(weatherData, aqiData);
            })
            .catch(error => {
                console.error("Error:", error);
                this.showSearchInterface();
            });
    },

    fetchWeatherByCoords: function (lat, lon) {
        Promise.all([
            fetch(
                `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${this.apiKey}`
            ).then(response => {
                if (!response.ok) throw new Error("No weather found.");
                return response.json();
            }),
            fetch(
                `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${this.apiKey}`
            ).then(response => response.json())
        ])
            .then(([weatherData, aqiData]) => {
                this.displayWeather(weatherData, aqiData);
            })
            .catch(error => {
                console.error("Error:", error);
                this.showSearchInterface();
            });
    },

    getAQIDescription: function(aqi) {
        const aqiDescriptions = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        };
        return aqiDescriptions[aqi] || "Unknown";
        },

        displayWeather: function (weatherData, aqiData) {
        const { name } = weatherData;
        const { icon, description } = weatherData.weather[0];
        let { temp, humidity, pressure} = weatherData.main;
        let visibility = weatherData.visibility;
        let { speed } = weatherData.wind;
        const aqi = aqiData.list[0].main.aqi;

        let isCelsius = true;

        function updateTemperatureAndWind() {

            const lat = weatherData.coord.lat;
            const lon = weatherData.coord.lon;
            document.querySelector(".points").innerHTML = 
                `<a class="flex-center" href="https://www.google.com/maps?q=${lat},${lon}">${weather.svgIcons.map}</a>
                </div>`;

            if (isCelsius) {
            document.querySelector(".temp").innerText = temp + "°C";
            document.querySelector(".wind").innerHTML = 
                `<div class="weather-item">
                ${weather.svgIcons.wind} : 
                <span>${speed} km/h</span>
                </div>`;
            document.querySelector(".Visibility").innerHTML = 
                `<div class="weather-item">
                ${weather.svgIcons.visible} : 
                <span>${(visibility / 1000).toFixed(2)} km</span>
                </div>`;
            } else {
            const tempF = (temp * 9/5) + 32;
            const speedMph = speed * 0.621371;
            const visibilityMiles = visibility * 0.000621371;
            document.querySelector(".temp").innerText = tempF.toFixed(2) + "°F";
            document.querySelector(".wind").innerHTML = 
                `<div class="weather-item">
                ${weather.svgIcons.wind} : 
                <span>${speedMph.toFixed(2)} mph</span>
                </div>`;
            document.querySelector(".Visibility").innerHTML = 
                `<div class="weather-item">
                ${weather.svgIcons.visible} : 
                <span>${visibilityMiles.toFixed(2)} miles</span>
                </div>`;
            }
        }

        document.querySelector(".city").innerHTML = `${this.svgIcons.city} : ` + name;
        document.querySelector(".iconi").style.backgroundImage =
            "url('https://openweathermap.org/img/wn/" + icon + ".png')";
        document.querySelector(".description").innerText = description;
        updateTemperatureAndWind();
        
        // Update humidity with icon
        document.querySelector(".humidity").innerHTML = 
            `<div class="weather-item">
            ${this.svgIcons.humidity} : 
            <span>${humidity}%</span>
            </div>`;
        
        // Update pressure with icon
        document.querySelector(".pressure").innerHTML = 
            `<div class="weather-item">
            ${this.svgIcons.pressure} : 
            <span>${pressure} hPa</span>
            </div>`;
        
        // Update AQI with icon
        document.querySelector(".aqi").innerHTML = 
            `<div class="weather-item">
            ${this.svgIcons.aqi} : 
            <span>${this.getAQIDescription(aqi)} (AQI: ${aqi})</span>
            </div>`;
        
        document.querySelector(".weather").classList.remove("loading");
        document.querySelector("#searchPrompt").style.display = "none";
        document.querySelector(".weather").style.display = "block";

        document.querySelector(".temp-style").addEventListener("click", () => {
            isCelsius = !isCelsius;
            updateTemperatureAndWind();
        });
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
// Map button click event to get current location
document.querySelector(".maps").addEventListener("click", function () {
    weather.getLocation();
});
// ----------------------------------------------------------------------------------------------------------------------------------------------------