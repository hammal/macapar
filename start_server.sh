#!/bin/bash
/bin/sleep 3
cd /home/pi/macapar/webinterface
PORT=80
/usr/bin/sudo /usr/bin/npm start /home/pi/macapar/webinterface/app.js
