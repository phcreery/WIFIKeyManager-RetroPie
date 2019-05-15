# WIFIKeyManager-RetroPie

Multiple Wifi Key Manager for Retropie intended for the use with TinkerBoy's Controller v3.0.1
https://www.tinkerboy.xyz/product/tinkerboy-controller-v3-0-game-boy-zero-aio-pcb-controller/

This tool allows for the quick switching and selecting of Wireless SSID and Passwords from a driectory of keyfiles by copytin one into the /boot directory.

## Getting Started

This small script helps with multiple WIFI key files that are usable in the RetroPie-Setup Script 


### Prerequisites

Works on RetroPie 4.4 or RetroPie-Setup post October 2016
 - Source: https://github.com/RetroPie/RetroPie-Setup/commit/d745cebe823820d115afa01e2359dcd6005ce443

What things you need to install the software and how to install them
```
pip install pyserial
```

### Installing

```
git clone "https://github.com/phcreery/WIFIKeyManager-RetroPie.git"
sudo cp WIFI_KEY_MGR.sh /home/pi/RetroPie/retropiemenu/WIFI_KEY_MGR.py
mkdir /home/pi/myfiles/wifi/
cp wifimgr2.py /home/pi/myfiles/wifi/wifimgr2.py
```

## Running

Restart emulationstation.

New menu item will be in RetroPie Menu.

### Usage

Place your wifikeys in /boot/wifikeys/ with any name ending in .txt

1) Launch **WIFI_KEY_MGR** item select the wifi key file.
2) Launch **WIFI** and Select **Import wifi cridentials**

## ToDo
This is the list of future changes:

 - [ ] Create KeyFiles with On-Screen Keyboard
 - [ ] More Graphical interface with something like Curses/asciimatics/npyscreen


## Authors

* **Peyton Creery** - *Initial work* - [Twinsphotography](https://twinsphotography.net)
