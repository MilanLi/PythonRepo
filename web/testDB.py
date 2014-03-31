import MySQLdb as mdb
import sys


def checkVersion():
    try:
        con = mdb.connect('localhost', 'testuser', 'test66', 'testdb');

        #get cursor object
        cur = con.cursor()
        cur.execute("SELECT VERSION()")

        #fetch the first row
        ver = cur.fetchone()

        print("Database version : %s " % ver)

    except mdb.Error as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if con:
            con.close()

def createTable():

    con = mdb.connect('localhost', 'testuser','test66', 'testdb')

    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS writers")
        cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
        cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")

    print("Creation and insertion have been finished!")
    

def fetchFromTable():

    con = mdb.connect('localhost', 'testuser','test66', 'testdb')

    with con:
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * from Writers")
        rows = cur.fetchall()
        for row in rows:
            print row["Id"], row["Name"]

    print("fetch has been finished!")

def updateTable():
    con = mdb.connect('localhost', 'testuser','test66', 'testdb')
    with con:
        cur = con.cursor()
        cur.execute("update writers set Name = %s where Id = %s", ("Guy de Maupasant", "4"))
        print "Number of rows updated:", cur.rowcount

    print("updating has been finished!")

