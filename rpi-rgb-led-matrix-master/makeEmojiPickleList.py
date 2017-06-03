import os
import pickle

emojipaths = []

for root, dirs, files in os.walk("./emojis/", topdown=False):
    for name in files:
        emojipaths.append(os.path.abspath(os.path.join("./emojis/",name)))

# save as pickle
with open("emojilist.txt", "wb") as fp:   #Pickling
    pickle.dump(emojipaths, fp)
