import urllib.request, string, json


    
def url(c, a, p):
    url="http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category="+c+"&alpha="+a+"&page="+p
    urlRetrieve=urllib.request.urlopen(url)
    urlOpen = str(urlRetrieve.read())
    urlOpen = urlOpen.replace("b'", "").strip("'<>() ").replace('\'', '\"')

    with open("itemId.txt", "a") as file:
        try:
            jsonData = json.loads(urlOpen)
            results = jsonData["items"]
            print(c,a,p)
            for each in results:
                itemId=str(each["id"])
                itemName=str(each["name"]).replace('"', '')  
                file.write(itemName+"="+itemId+"\n")
        except:
            pass

        
def idAlg():
    alphabet = list(string.ascii_lowercase) #len(string.ascii...) prints out the entire english alphabet in lowercase. 
    p="0"
    for a in alphabet:
        print(a)
        for x in range(0,379):
            if x < 10:
                url(str(x),a,p)
            elif 10<=x<100:
                c,p=map(str, str(x)) # map(str, str(x)) splits x, if it is 123, to '1','2','3'.
                url(c,a,p)
            else:
                c = x//10
                z,b,p =map(str,str(x))
                url(str(c),a,p)

def main():
    idAlg()


if __name__ == "__main__":
    main()




