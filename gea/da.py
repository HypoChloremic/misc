import urllib.request as UR, time

def miner():
    itemName = input("What is the name of the item: ")
    itemId = input("Input the item id of the specific item: ")
    url = "http://services.runescape.com/m=itemdb_rs/api/graph/"+itemId+".json" 
    data = str(UR.urlopen(url).read())
    data = data.replace("daily","").replace("average","").replace("b'", "").replace("{:","").replace("{","").replace("}","").replace("'","").replace('"','').replace(",", "\n").replace("0:",",").replace(":","").replace(","," ")
    date = str(time.strftime("%d%m%y"))
    txtFile1=itemName+date+".txt"

    with open(txtFile1, "w") as file:
        file.write(data)
    
