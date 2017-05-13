#!/bin/bash
git push
ssh ledScreen "cd macapar/rpi-rgb-led-matrix-master; git pull; sudo python $1"