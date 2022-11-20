import pickle

fh = open("highscore.dat","wb")

l=[]

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
