words = ["loock","cloock","cook"]
x = None #to hold common characters
for word in words:
    if x:
        x = x.intersection(set(word))
    else:
        x = set(word)


for word in words:        
    print(word.count('k'))