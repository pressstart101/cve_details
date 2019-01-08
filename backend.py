import sqlite3

def connect():
    conn=sqlite3.connect("cvedetails.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cvedetail (id INTEGER PRIMARY KEY, cveid text, severity text, name integer, date integer)")
    conn.commit()
    conn.close()

def insert(cveid,severity,name,date):
    conn=sqlite3.connect("cvedetails.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO cvedetail VALUES (NULL,?,?,?,?)",(cveid,severity,name,date))
    conn.commit()
    conn.close()    

def view():
    conn=sqlite3.connect("cvedetails.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM cvedetail")
    rows=cur.fetchall()
    conn.close()   
    return rows


def search(cveid="",severity="",name="",date=""):
    conn=sqlite3.connect("cvedetails.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM cvedetail WHERE cveid=? OR severity=? OR name=? OR date=?", (cveid,severity,name,date))
    rows=cur.fetchall()
    conn.close()   
    return rows  


def delete(id):
    conn=sqlite3.connect("cvedetails.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM cvedetail WHERE id=?", (id,))
    conn.commit()    
    conn.close()   

def update(id,cveid,severity,name,date):
    conn=sqlite3.connect("cvedetails.db")
    cur=conn.cursor()
    cur.execute("UPDATE cvedetail SET cveid=?, severity=?,name=?,date=? WHERE id=?",(cveid,severity,name,date,id))
    conn.commit()    
    conn.close()  


connect()    

# print(view())
