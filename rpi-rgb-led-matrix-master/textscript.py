import time
import sys
text = ["En elefant balanserade", "Pa en liten spindeltrad", "Det tyckte han var sa intressant,", "Sa han gick och hamtade en annan elefant."]
while text:
    sys.stdout.write(text.pop(0))
    sys.stdout.flush()
    time.sleep(5)
    print('')
