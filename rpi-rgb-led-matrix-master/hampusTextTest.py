#Usage is as follows:
#See the Wiki for more details: https://github.com/ManiacalLabs/BiblioPixel/wiki

from bibliopixel import *
import bibliopixel.colors as colors
from ada-matrix import DriverAdaMatrix

driver = DriverAdaMatrix(rows=32, chain=1)
driver.SetPWMBits(6) #decrease bit-depth for better performance
#MUST use serpentine=False because rgbmatrix handles the data that way
led = LEDMatrix(driver, 32, 32, serpentine=False)

#Must have code downloaded from GitHub for matrix_animations
from matrix_animations import *
import bibliopixel.log as log
log.setLogLevel(log.DEBUG)


try:
    anim = ScrollText(led, "Hello World!", size=4)
    anim.run()
except KeyboardInterrupt:
    led.all_off()
    led.update()
