import pickle

fh = open("highscore.dat","wb")

l=[[1,"1m42s","20/10/22"],[2,"2m42s","30/10/22"],[3,"4m42s","10/20/22"]]

for i in l:
    pickle.dump(i,fh)
    
fh = open("highscore.dat","rb")
data = []

while True:
    try:
        rec = pickle.load(fh)
        print(rec)
        data.append(rec)
    except EOFError:
        fh.close()
        break

print(data)
