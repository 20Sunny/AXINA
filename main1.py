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
        @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Space+Grotesk:wght@300..700&display=swap');
        *{
            font-family: "Caveat", serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
        }

        body {
            margin: 0;
            padding: 0;
            background: url(./pxfuel.jpg);
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: bottom center;
            background-size: cover;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            height: 100vh;
            overflow: hidden;
            z-index: -1;
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
            padding: 5px;
            margin-top: 20vh;
            background: rgba(255, 255, 255, 0.2);
            border-radius:30px;
            width: 70vw;
            overflow: hidden;
        }

        input {
            padding: 12px 16px;
            border: none;
            width: 100%;
            font-size: 1rem;
            background: #ffffff00;
            color: #fff;
            outline: none;
            transition: all 0.3s ease;
        }

        input::placeholder {
            color: rgb(255, 255, 255);
            background: #ffffff00 !important;
        }
        input::target-text{
            background: #ffffff00;
        }

        input:focus {
            background: #ffffff00;        }

        button {
            padding: 10px 10px;
            height: 50px;
            width: 50px;
            justify-content: center;
            align-items: center;
            font-size: 1rem;
            color: #fff;
            background: linear-gradient(135deg, #ec5a97, #2022559d, #202255);
            border: none;
            cursor: pointer;
            transition: all 0.5s ease-in-out;
            border-radius: 100%;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
        }

        button:hover {
            transform: translate3d(2px);
            background: #ffffff00;
            border: 1px solid #202255;
            backdrop-filter: blur(2px);
            transition: all 0.5s ease-in-out;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.5);
        }

        #socialIconsContainer { 
            display: grid;
            grid-template-columns: repeat(10, minmax(0, 1fr));
            gap: 20px;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            margin-top: 20px;
            padding: 10px 20px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            max-width: 80%;
        }

        .shortcut{
            display: contents;
        }
            .wallpaper{
                display: flex;
                gap: 20px;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;
                padding: 10px 20px;
                background: rgba(0, 0, 0, 0.5);
                border-radius: 0 0 10px 10px;
                max-width: 80%;
            }
            .wallpaper a{
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
            }
            .wallpaper a:hover{
                background: linear-gradient(135deg, #ec5a97, #2022559d, #202255);
                transform: scale(1.05);
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
                transition: all 0.3s ease;
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
            background: linear-gradient(135deg, #ec5a97, #2022559d, #202255);
            transform: scale(1.05);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
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
            background: linear-gradient(135deg, #ec5a97, #2022559d, #202255);
            transform: scale(1.05);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
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

        #net {
            position: fixed;
            bottom: 20px;
            right: 20px;
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
            background: linear-gradient(135deg, #ec5a97, #2022559d, #202255);
        }
        #quote{
            font-family: "Space Grotesk", serif;
            font-weight: 400;
            font-style: normal;
        }

        .qout{
            position: absolute;
            pointer-events: none;
            bottom: 0;
            flex: 1 1 0%;
            display: flex;
            flex-direction: column;
            flex-wrap: nowrap;
            align-items: flex-end;
        }


    </style>
</head>
<body>
    <div id="clock"></div>
    <a id="net" aria-label="Internet Status" style="color: #fff;"></a>
    <form id="searchForm">
        <input type="text" id="urlInput" placeholder="Enter URL or search..." autocomplete="off" name="AXINA">
        <button type="submit"><svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#FFFFFF"><path d="M778-164 528-414q-30 26-69 40t-77 14q-92.23 0-156.12-63.84-63.88-63.83-63.88-156Q162-672 225.84-736q63.83-64 156-64Q474-800 538-736.12q64 63.89 64 156.12 0 41-15 80t-39 66l250 250-20 20ZM382-388q81 0 136.5-55.5T574-580q0-81-55.5-136.5T382-772q-81 0-136.5 55.5T190-580q0 81 55.5 136.5T382-388Z"/></svg></button>
    </form>
    <!-- Social Media Icons Section -->
    <div class="shortcut">
    <div id="socialIconsContainer">
        <abbr title="OpenAI ChatGPT"><a href="https://chatgpt.com"><svg width="30px" height="30px" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="h-2/3 w-2/3" role="img"><path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg></a></abbr>
        <abbr title="TensorArt"><a href="https://tensor.art" style="overflow: hidden;"><img style="height: 40px;width: 40px;mix-blend-mode: color-dodge;filter: invert(100%);" src="https://tensor.art/tensorart_logo_square_version.png" alt="" srcset="https://tensor.art/tensorart.ico"></a></abbr>
        <abbr title="Runway"><a href="https://runwayml.com" style="overflow: hidden;"><img style="height: 40px;width: 40px;mix-blend-mode: color-dodge;filter: invert(100%);" src="https://runwayml.com/icon.png" alt="" srcset="https://runwayml.com/icon.png"></a></abbr>
        <abbr title="Civitai"><a href="https://civitai.com"><img style="height: 30px;width: 30px;" src="https://civitai.com/favicon-blue.ico" alt="" srcset="https://civitai.com/favicon-blue.ico"></a></abbr>
        <abbr title="Fotor"><a href="https://www.fotor.com"><img style="height: 30px;width: 30px;" src="https://static.fotor.com/web/_next/static/images/favicon-d4b8dbe4630a2bc790117e61267bbb33.png" alt="" srcset="https://static.fotor.com/web/_next/static/images/favicon-d4b8dbe4630a2bc790117e61267bbb33.png"></a></abbr>
        <abbr title="ClipDrop"><a href="https://clipdrop.co"><svg height="30px" width="30px" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 8.93333C0 4.55187 3.47466 1 7.76087 1H9.8913C10.7317 1 11.413 1.69645 11.413 2.55556V3.95556C11.413 4.81467 10.7317 5.51111 9.8913 5.51111H7.76087C5.99596 5.51111 4.1087 7.1292 4.1087 8.93333V11.1111C4.1087 11.9702 3.42739 12.6667 2.58696 12.6667H1.52174C0.681306 12.6667 0 11.9702 0 11.1111L0 8.93333Z" fill="currentcolor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M28 21.0667C28 25.4481 24.5253 29 20.2391 29H18.1087C17.2683 29 16.587 28.3036 16.587 27.4444V26.0444C16.587 25.1853 17.2683 24.4889 18.1087 24.4889H20.2391C22.004 24.4889 23.8913 22.8708 23.8913 21.0667V18.8889C23.8913 18.0298 24.5726 17.3333 25.413 17.3333H26.4783C27.3187 17.3333 28 18.0298 28 18.8889V21.0667Z" fill="currentcolor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M20.2391 1C24.5253 1 28 4.55187 28 8.93333V11.1111C28 11.9702 27.3187 12.6667 26.4783 12.6667H25.1087C24.2683 12.6667 23.587 11.9702 23.587 11.1111V8.93333C23.587 7.1292 22.004 5.2 20.2391 5.2H18.1087C17.2683 5.2 16.587 4.50355 16.587 3.64444V2.55556C16.587 1.69645 17.2683 1 18.1087 1L20.2391 1Z" fill="currentcolor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M7.76087 29C3.47466 29 1.56318e-07 25.4481 7.18387e-07 21.0667L9.97759e-07 18.8889C1.10797e-06 18.0298 0.681307 17.3333 1.52174 17.3333H2.89131C3.73174 17.3333 4.41304 18.0298 4.41304 18.8889V21.0667C4.41304 22.8708 5.99596 24.8 7.76087 24.8L9.8913 24.8C10.7317 24.8 11.413 25.4964 11.413 26.3556V27.4444C11.413 28.3036 10.7317 29 9.8913 29L7.76087 29Z" fill="currentcolor"></path></svg></a></abbr>
        <abbr title="Stable Diffusion"><a href="https://stablediffusionweb.com"><img style="height: 30px;width: 30px;" src="https://stablediffusionweb.com/favicon.ico" alt="" srcset="https://stablediffusionweb.com/favicon.ico"></a></abbr>
        <abbr title="OpenArt"><a href="https://openart.ai" style="overflow: hidden;"><img style="height: 40px;width: 40px;mix-blend-mode: color-dodge;filter: invert(100%);" src="https://cdn.prod.website-files.com/6600e1eab90de089c2d9c972/660736422d6d72ba4a9ad9e9_logo_webclip_256x256.png" alt="" srcset="https://cdn.prod.website-files.com/6600e1eab90de089c2d9c972/660736422d6d72ba4a9ad9e9_logo_webclip_256x256.png"></a></abbr>
        <abbr title="TensorArt"><a href="https://tensor.art" style="overflow: hidden;"><img style="height: 40px;width: 40px;mix-blend-mode: color-dodge;filter: invert(100%);" src="https://www.zmo.ai/wp-content/uploads/2022/05/cropped-favcon-192x192.png" alt="" srcset="https://www.zmo.ai/wp-content/uploads/2022/05/cropped-favcon-192x192.png"></a></abbr>
        <abbr title="Deviant Art"><a href="https://www.deviantart.com/"><svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" width="30" height="30" viewBox="0 0 100 167"><path d=" M100 0 L99.96 0 L99.95 0 L71.32 0 L68.26 3.04 L53.67 30.89 L49.41 33.35 L0 33.35 L0 74.97 L26.40 74.97 L29.15 77.72 L0 133.36 L0 166.5 L0 166.61 L0 166.61 L28.70 166.6 L31.77 163.55 L46.39 135.69 L50.56 133.28 L100 133.28 L100 91.68 L73.52 91.68 L70.84 89 L100 33.33 "></path></svg></a></abbr>    
    </div>
    <div class="wallpaper">
        <abbr title="Rare Gallery"><a href="https://coolwallpapers.me"><img style="filter: invert(100%); mix-blend-mode: plus-lighter;height: 30px;width: 30px;" src="https://coolwallpapers.me/templates/ultimate/images/favicon.png" alt="" srcset="https://coolwallpapers.me/templates/ultimate/images/favicon.png"></a></abbr>
        <abbr title="PxFuel"><a href="https://www.pxfuel.com"><img style="height: 30px;width: 30px;border-radius: 25px;" src="https://www.pxfuel.com/public/icons/favicon-32x32.png" alt="" srcset="https://www.pxfuel.com/public/icons/favicon-32x32.png"></a></abbr>
        <abbr title="Rare Gallery"><a href="https://rare-gallery.com"><img src="https://rare-gallery.com/favicon.ico" alt="" srcset="https://rare-gallery.com/favicon.ico"></a></abbr>
        <abbr title="WallpapersHome"><a href="https://wallpapershome.com/"><img style="height: 30px;width: 30px;border-radius: 25px;" src="https://wallpapershome.com/favicon.ico" alt="" srcset="https://wallpapershome.com/favicon.svg"></a></abbr>
        <abbr title="Wallpapers"><a href="https://wallpapers.com"><svg id="Layer_1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" height="30px" width="30px"><defs><style>.cls-1{fill:#df2b51;}.cls-1,.cls-10,.cls-11,.cls-12,.cls-2,.cls-3,.cls-4,.cls-5,.cls-6,.cls-7,.cls-8,.cls-9{fill-rule:evenodd;}.cls-2{fill:#be2130;}.cls-3{fill:#e3502c;}.cls-4{fill:#f19722;}.cls-5{fill:#f9e21e;}.cls-6{fill:#88cf59;}.cls-7{fill:#54ae3c;}.cls-8{fill:#29ab88;}.cls-9{fill:#1d76bb;}.cls-10{fill:#214497;}.cls-11{fill:#862887;}.cls-12{fill:#ef4481;}</style></defs><path id="_012" data-name=" 012" class="cls-1" d="M10.22.31a8,8,0,0,1,3.33,1.92L11,4.78a4.33,4.33,0,0,0-1.7-1Z" transform="translate(0 0)"/><path id="_011" data-name=" 011" class="cls-2" d="M7,3.72,6.08.23a8,8,0,0,1,3.84,0L9,3.71A4.51,4.51,0,0,0,7,3.72Z" transform="translate(0 0)"/><path id="_010" data-name=" 010" class="cls-3" d="M6.71,3.8A4.44,4.44,0,0,0,5,4.78L2.45,2.23A7.9,7.9,0,0,1,5.78.32Z" transform="translate(0 0)"/><path id="_09" data-name=" 09" class="cls-4" d="M3.8,6.71.31,5.77A7.93,7.93,0,0,1,2.23,2.45L4.78,5A4.37,4.37,0,0,0,3.8,6.71Z" transform="translate(0 0)"/><path id="_08" data-name=" 08" class="cls-5" d="M3.72,9,.23,9.91a8,8,0,0,1,0-3.83L3.72,7A4.32,4.32,0,0,0,3.72,9Z" transform="translate(0 0)"/><path id="_07" data-name=" 07" class="cls-6" d="M4.78,11,2.23,13.55A7.9,7.9,0,0,1,.32,10.22l3.49-.93A4.38,4.38,0,0,0,4.78,11Z" transform="translate(0 0)"/><path id="_06" data-name=" 06" class="cls-7" d="M5.78,15.69a8,8,0,0,1-3.33-1.92L5,11.22a4.38,4.38,0,0,0,1.7,1Z" transform="translate(0 0)"/><path id="_05" data-name=" 05" class="cls-8" d="M9,12.27l.94,3.5a8,8,0,0,1-3.84,0L7,12.28A4.32,4.32,0,0,0,9,12.27Z" transform="translate(0 0)"/><path id="_04" data-name=" 04" class="cls-9" d="M9.29,12.19a4.21,4.21,0,0,0,1.7-1l2.56,2.56a7.9,7.9,0,0,1-3.33,1.91Zm4.48,1.36L11.22,11" transform="translate(0 0)"/><path id="_03" data-name=" 03" class="cls-10" d="M12.2,9.29l3.49.94a8.05,8.05,0,0,1-1.92,3.32L11.22,11A4.46,4.46,0,0,0,12.2,9.29Z" transform="translate(0 0)"/><path id="_02" data-name=" 02" class="cls-11" d="M12.28,7l3.49-.93a8,8,0,0,1,0,3.83L12.28,9A4.32,4.32,0,0,0,12.28,7Z" transform="translate(0 0)"/><path id="_01" data-name=" 01" class="cls-12" d="M11.22,5l2.55-2.56a7.92,7.92,0,0,1,1.91,3.32l-3.49.94A4.24,4.24,0,0,0,11.22,5Z"/></svg></abbr></a></abbr>
        <abbr title="Rare Gallery"><a href="https://wallpapercrafter.com"><img style="height: 30px;width: 30px;border-radius: 25px;" src="https://wallpapercrafter.com/templates/dark/images/favicon.png" alt="" srcset="https://wallpapercrafter.com/templates/dark/images/favicon.png"></a></abbr>
    </div>
    </div>
    

    <!-- Toggle Button for Google Apps-------------------------------------------------------------------------------------------------------------------------- -->
    <button id="toggleAppsButton" aria-label="Toggle Apps"><svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#FFFFFF"><path d="M120-380q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-160q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm120 332q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm160.24 332Q382-356 369-368.76q-13-12.77-13-31Q356-418 368.76-431q12.77-13 31-13Q418-444 431-431.24q13 12.77 13 31Q444-382 431.24-369q-12.77 13-31 13Zm0-160Q382-516 369-528.76q-13-12.77-13-31Q356-578 368.76-591q12.77-13 31-13Q418-604 431-591.24q13 12.77 13 31Q444-542 431.24-529q-12.77 13-31 13ZM400-208q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-480q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0 588q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-720q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm160.24 464Q542-356 529-368.76q-13-12.77-13-31Q516-418 528.76-431q12.77-13 31-13Q578-444 591-431.24q13 12.77 13 31Q604-382 591.24-369q-12.77 13-31 13Zm0-160Q542-516 529-528.76q-13-12.77-13-31Q516-578 528.76-591q12.77-13 31-13Q578-604 591-591.24q13 12.77 13 31Q604-542 591.24-529q-12.77 13-31 13ZM560-208q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-480q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0 588q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-720q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm160 612q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm120 308q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-160q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Z"/></svg></button>

    <!-- Google Apps Section -->
    <div id="googleAppsContainer">
        <a href="https://mail.google.com/" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
    </div>

    <div class="qout" onload="fetchQuote()">
        <div id="quote">Two Clever People Can't Fall In The Love;<br/> It Requires One Idiot!</div>
        <div id="author">- Wise Man</div>
    </div>

    <script>
// -----------------------------------
// Function to update the icon based on online status
function updateStatusIcon() {
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
            toggleAppsButton.innerHTML = isHidden ? '<svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#FFFFFF"><path d="M400-528q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2Zm0 160q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2ZM280-540q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm120 280q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6ZM280-380q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm120-280q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm160 132q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2Zm0-132q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm120 280q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm0-160q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6ZM480.17-132q-72.17 0-135.73-27.39-63.56-27.39-110.57-74.35-47.02-46.96-74.44-110.43Q132-407.65 132-479.83q0-72.17 27.39-135.73 27.39-63.56 74.35-110.57 46.96-47.02 110.43-74.44Q407.65-828 479.83-828q72.17 0 135.73 27.39 63.56 27.39 110.57 74.35 47.02 46.96 74.44 110.43Q828-552.35 828-480.17q0 72.17-27.39 135.73-27.39 63.56-74.35 110.57-46.96 47.02-110.43 74.44Q552.35-132 480.17-132Zm-.17-28q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm80-100q8 0 14-6t6-14q0-8-6-14t-14-6q-8 0-14 6t-6 14q0 8 6 14t14 6Zm0-108q13.6 0 22.8-9.2 9.2-9.2 9.2-22.8 0-13.6-9.2-22.8-9.2-9.2-22.8-9.2-13.6 0-22.8 9.2-9.2 9.2-9.2 22.8 0 13.6 9.2 22.8 9.2 9.2 22.8 9.2Zm-80-112Z"/></svg>' : '<svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#FFFFFF"><path d="M120-380q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-160q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm120 332q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm160.24 332Q382-356 369-368.76q-13-12.77-13-31Q356-418 368.76-431q12.77-13 31-13Q418-444 431-431.24q13 12.77 13 31Q444-382 431.24-369q-12.77 13-31 13Zm0-160Q382-516 369-528.76q-13-12.77-13-31Q356-578 368.76-591q12.77-13 31-13Q418-604 431-591.24q13 12.77 13 31Q444-542 431.24-529q-12.77 13-31 13ZM400-208q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-480q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0 588q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-720q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm160.24 464Q542-356 529-368.76q-13-12.77-13-31Q516-418 528.76-431q12.77-13 31-13Q578-444 591-431.24q13 12.77 13 31Q604-382 591.24-369q-12.77 13-31 13Zm0-160Q542-516 529-528.76q-13-12.77-13-31Q516-578 528.76-591q12.77-13 31-13Q578-604 591-591.24q13 12.77 13 31Q604-542 591.24-529q-12.77 13-31 13ZM560-208q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-480q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0 588q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-720q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm160 612q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm0-160q-13.6 0-22.8-9.2-9.2-9.2-9.2-22.8 0-13.6 9.2-22.8 9.2-9.2 22.8-9.2 13.6 0 22.8 9.2 9.2 9.2 9.2 22.8 0 13.6-9.2 22.8-9.2 9.2-22.8 9.2Zm120 308q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Zm0-160q-8 0-14-6t-6-14q0-8 6-14t14-6q8 0 14 6t6 14q0 8-6 14t-14 6Z"/></svg>';
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
    with open("index.html", "w") as file:
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
        self.add_new_tab(QUrl.fromLocalFile(os.path.abspath("index.html")), "Home")

        # Current zoom level
        self.current_zoom_level = 1.2

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl.fromLocalFile(os.path.abspath("index.html"))

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
        self.tabs.currentWidget().setUrl(QUrl.fromLocalFile(os.path.abspath("index.html")))

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
        zoom_percentage = int((self.current_zoom_level) * 100)
        self.zoom_label.setText(f"{zoom_percentage}%")

# Application Entry Point
app = QApplication(sys.argv)
QApplication.setApplicationName("Axina Browser")

window = MainWindow()
app.exec_()
