import sys, math, matplotlib.pyplot as plt, numpy as np



        
def main():
    t = plt.figure(1)
    dataFile=input("please input the name of the data file (.txt is not necessary): ")+".txt"
    with open(dataFile, "r") as file:
        data = file.read()
    data = data.split("\n")
    x = [row.split(" ")[0] for row in data[:180]]
    y = [row.split(" ")[1] for row in data[:180]]
    x2= [row.split(" ")[0] for row in data[180:]]
    y2= [row.split(" ")[1] for row in data[180:]]
    x,y,x2,y2=np.array(x),np.array(y),np.array(x2),np.array(y2)
    plt.plot(x,y)
    plt.plot(x2,y2)
    t.show(1)

    j = plt.figure(2)    
    a = []
    X2 = x2.tolist()
    Y2 = y2.tolist()
    for x in range(0, len(X2)):
        try:
              k = int(X2[x+1]) - int(X2[x])
              z = int(Y2[x+1]) - int(Y2[x])
              w = (z/k)
              a.append(str(w))
        except:
            continue
    print("Hello World")
    a  = np.array(a)
    x2 = np.delete(x2, 0)
    x2 = np.array(x2)
    a  = a.astype(np.float)
    x2 = x2.astype(np.float)

    lis = []
    for x in range (0, (len(X2)-2)):
        try:
            k = int(X2[x+2]) - int(X2[x])
            z = int(Y2[x+2]) - int(Y2[x])
            lis.append(str(z/k))
        except:
            q = int(Y2[x+1]) - int(Y2[x])
            p = int(X2[x+1]) - int(X2[x])
            lis.append(str(q/p)) 
        else:
            continue
    print(len(lis))
    plt.plot(x2,a)
    j.show(2)
    print("Hello World")

    
if __name__=="__main__":
    main()
