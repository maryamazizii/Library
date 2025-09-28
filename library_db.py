import sqlite3 
class Library:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute('''create table if not exists library 
                         (id integer primary key, title text ,author  text ,
                         years integer , ISBN integer ) ''')
        self.con.commit()


    def select(self):
        self.cur.execute('select *from library ')
        return self.cur.fetchall()
    

    def search(self, title="", author="", years="", isbn=""):
        self.cur.execute('''
            SELECT * FROM library WHERE
            title LIKE ? AND
            author LIKE ? AND
            years LIKE ? AND
            ISBN LIKE ?
        ''', (f'%{title}%', f'%{author}%', f'%{years}%', f'%{isbn}%'))

        return self.cur.fetchall()
    

    def insert(self,title,author,years,isbn):
        self.cur.execute('insert into library  values (NULL,?,?,?,?)',(title,author,years,isbn))
        self.con.commit()
    
    def delete(self,id):
        self.cur.execute('delete from library where id =?',(id,))
        self.con.commit()


        






li1=Library('D:/p_database/library.db')