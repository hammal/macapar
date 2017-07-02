import os
import pickle

emojipaths = []

for root, dirs, files in os.walk("./emojis/emotions/", topdown=False):
    for name in files:
    	if name[-4:] == ".png" and name[0] != ".":
        	emojipaths.append(os.path.abspath(os.path.join("./emojis/emotions/",name)))

# save as pickle
with open("emojiemotionlist.txt", "wb") as fp:   #Pickling
    pickle.dump(emojipaths, fp)


emojipaths = []

for root, dirs, files in os.walk("./emojis/aon/", topdown=False):
    for name in files:
    	if name[-4:] == ".png" and name[0] != ".":
        	emojipaths.append(os.path.abspath(os.path.join("./emojis/aon/",name)))

# save as pickle
with open("emojiaonlist.txt", "wb") as fp:   #Pickling
    pickle.dump(emojipaths, fp)


emojipaths = []

for root, dirs, files in os.walk("./emojis/antik/", topdown=False):
    for name in files:
    	if name[-4:] == ".png" and name[0] != ".":
        	emojipaths.append(os.path.abspath(os.path.join("./emojis/antik/",name)))

# save as pickle
with open("antiklist.txt", "wb") as fp:   #Pickling
    pickle.dump(emojipaths, fp)

emojipaths = []

for root, dirs, files in os.walk("./emojis/gunnar/", topdown=False):
    for name in files:
        if name[-4:] == ".png" and name[0] != ".":
            emojipaths.append(os.path.abspath(os.path.join("./emojis/gunnar/",name)))

# save as pickle
with open("gunnarlist.txt", "wb") as fp:   #Pickling
    pickle.dump(emojipaths, fp)

emojipaths = []

for root, dirs, files in os.walk("./emojis/martin/", topdown=False):
    for name in files:
        if name[-4:] == ".png" and name[0] != ".":
            emojipaths.append(os.path.abspath(os.path.join("./emojis/martin/",name)))

# save as pickle
with open("martinlist.txt", "wb") as fp:   #Pickling
    pickle.dump(emojipaths, fp)