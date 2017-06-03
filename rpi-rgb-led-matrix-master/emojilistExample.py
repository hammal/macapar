import pickle

with open("emojilist.txt", "rb") as fp:   # Unpickling
    emojilist = pickle.load(fp)

print(emojilist)
