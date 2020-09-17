import os
import ctypes
import random


class AppOpener:
    def OpenApplication(self):
        print("DEMO PATH : C:\\Program Files\\Microsoft VS Code\\Code.exe")
        path = input("Enter the path of Application you want to open.")
        os.startfile(path)

    def desktop_background(self):
        lst_images = ["mountain.jpg", "wallpaper.jpg", "brown.jpg", "pink_beauty.jpg", "alone.jpg", "sun.jpg",
                      "city_beauty.jpg", "happy.jpg", "pokemon.jpg", "purple_beauty.jpg", "wheat.jpg", "paris.jpg"]
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, random.choice(lst_images), 0)
        print("Desktop background is successfully changed!")



A = AppOpener()
