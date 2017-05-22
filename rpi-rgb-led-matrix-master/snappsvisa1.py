import time
import sys
import textwrap
text = ["Fåååm fåååm, fååm fååm", "fåm vi lite opp i kosa", "Fåååm fåååm, fååm fååm", "fåm vi lite opp i kosa","Jengang å", "jengan å","jengan å jengang te."]
while text:
    print(text.pop(0))
    #sys.stdout.write(textwrap.wrap(text.pop(0), width=5))
    #sys.stdout.flush()
    # print("\n                        ")
    time.sleep(4)
    #sys.stdout.write("\r")
    sys.stdout.flush()

# //: Fåm, fåm, fåm, fåm, fåm vi lite opp i kosa :// 
# Jen gang och jen gang och jen gang och jen gang te 
# Jen gang och jen gang och jen gang och jen gang te