from bs4 import BeautifulSoup
import urllib
import MySQLdb as mdb
import sys

def createTable():
    con = mdb.connect('localhost', 'testuser','test66', 'testdb')

    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS NASDAQ")
        cur.execute("""CREATE TABLE NASDAQ(id INT PRIMARY KEY AUTO_INCREMENT,code VARCHAR(8),
                     high VARCHAR(10), low VARCHAR(10), close VARCHAR(10),volumn VARCHAR(15),
                    changeValue VARCHAR(10), changeRatio VARCHAR(10))""")

def insertIntoTable(dataList):
    length = len(dataList)
    count = 0
    con = mdb.connect('localhost', 'testuser','test66', 'testdb')
    with con:
        cur = con.cursor()
        for data in dataList:
            cur.execute("""INSERT INTO NASDAQ(code,high,low,close,volumn,changeValue,changeRatio)
                        VALUES('%s','%s','%s','%s','%s','%s','%s')"""% data)
            count = count + 1
        print("Inserted:", count)
        print("Should insert:", length)

def grabData(url):

    htmltext = urllib.urlopen(url).read()
    soup = BeautifulSoup(htmltext)
    table = soup.body.form.find("div", {"id":'col1w'})\
            .div.find("div", {"class":"cb"}).find("table", {"class":"quotes"})

    dataList = []

    # code   high    low    close   volumn    changeValue changeRatio
    for data in table.find_all("tr", attrs={'onclick': True}):
        pre = "http://eoddata.com"
        link = str(pre + data['onclick'].split("'")[1])
        code = str(link.split('.')[-2].split("/")[-1])
        td = data.find_all("td")
        name = str(td[1].text)
        high = str(td[2].text)
        low = str(td[3].text)
        close = str(td[4].text)
        volumn = str(td[5].text)
        changeValue = str(td[6].text)
        changeRatio = str(td[8].text)
        dataList.append((code, high, low, close, volumn, changeValue, changeRatio))
        
    insertIntoTable(dataList)



#main#

createTable()
for c in range(ord('A'), ord('Z')+1):
    url = "http://eoddata.com/stocklist/NASDAQ/"+chr(c)+".htm"
    print url,"......"
    grabData(url)


