#!bin/bash

if [ ${1} -eq "0" ]; then
    echo "[start Tcs sensing setting at pi]"
    echo "[network setting]"
    sudo rm /etc/wpa_supplicant/wpa_supplicant.conf
    sudo cp ./setting_file/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf

    sudo rm /etc/rc.local
    sudo cp ./setting_file/rc_1.local /etc/rc.local

    sudo reboot
elif [ ${1} -eq "1" ]; then
    echo "[init setting install]"
    sudo apt-get update
    sudo apt-get upgrade

    sudo apt-get install git 
    sudp apt-get install python-pip

    git clone https://github.com/munu2635/raspstart.git

    sudo apt-get install cmake libjpeg-dev
    cd raspstart/mjpg-streamer/mjpg-streamer-experimental/
    make CMAKE_BUILD_TYPE=Debug
    cd ..

    sudo install spidev
    sudo apt-get install python-smbus

    sudo rm /etc/rc.local
    sudo cp ./setting_file/rc_2.local /etc/rc.local

    echo "[End Tcs sensing setting at pi]"

fi

exit 0