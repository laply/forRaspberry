#!/usr/bin/env bash

if [$1=="0"]; then
echo "[start Tcs sensing setting at pi]"
echo "[network setting]"
sudo rm /etc/wpa_supplicant/wpa_supplicant.conf
sudo cp wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf

sed -e "19 i/sudo sh ${pwd}/setting.sh 1 &" /etc/rc.local

elif [$1=="1"]; then
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
sed -e "19 i/sudo sh home/pi/raspstart/mjpg.sh &" /etc/rc.local
sed -e "20 i/sudo sh sudo -H -u pi usr/bin/python home/pi/raspstart/sensingData/sensingMain.py &" /etc/rc.local

echo "[End Tcs sensing setting at pi]"

fi

exit 0