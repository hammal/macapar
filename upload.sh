#!/bin/bash
rsync -auv --progress ./ pi@192.168.42.1:~/macapar/
