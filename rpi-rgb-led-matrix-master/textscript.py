import time
import sys
import textwrap
text = ["En elefant balanserade", "Pa en liten spindeltrad", "Det tyckte han var sa intressant,", "Sa han gick och hamtade en annan elefant."]
while text:
    print(text.pop(0))
    #sys.stdout.write(textwrap.wrap(text.pop(0), width=5))
    #sys.stdout.flush()
    # print("\n                        ")
    time.sleep(4)
    #sys.stdout.write("\r")
    sys.stdout.flush()
