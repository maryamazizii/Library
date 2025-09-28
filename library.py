from tkinter import*
import library_db
from tkinter import messagebox
win = Tk()
win.geometry('550x285')
win.title('Library')

#_________Function_________
li1=library_db.Library('D:/p_database/library.db')

def cleaer_entry():
    entry_tit.delete(0,END)
    entry_author.delete(0,END)
    entry_years.delete(0,END)
    entry_isbn.delete(0,END)


def  select_record():
    listbox.delete(0,END)
    records=li1.select()
    for record in records:
        listbox.insert(END,record)

def insert_record():
    title=entry_tit.get()
    author=entry_author.get()
    years=entry_years.get()
    isbn=entry_isbn.get()
    li1.insert(title,author,years,isbn)
    cleaer_entry()

def search_record():
    listbox.delete(0,END)
    records=(li1.search(entry_tit.get(),entry_author.get(),entry_years.get(),entry_isbn.get()))
    for record in records:
       listbox.insert(END,record)
    cleaer_entry() 

def delet_record():
    index=listbox.curselection()
    data=listbox.get(index)
    li1.delete(data[0])
    select_record()

def close():
    result=messagebox.askquestion('CLOSE','Dou you want exit?')
    if result == 'yes':
        win.destroy()

    



    






#__________Labale__________

lable=Label(win,text='عنوان',font='tahoma 10').place(x=39,y=17)
lable=Label(win,text='سال انتشار',font='tahoma 10').place(x=30,y=47)
lable=Label(win,text='نویسنده',font='tahoma 10').place(x=280,y=17)
lable=Label(win,text='ISBN',font='tahoma 10').place(x=289,y=47)


#____________Entry___________

entry_tit=Entry(win,width=23)
entry_tit.place(x=106,y=18)

entry_years=Entry(win,width=23)
entry_years.place(x=106,y=48)

entry_author=Entry(win,width=23)
entry_author.place(x=350,y=18)

entry_isbn=Entry(win,width=23)
entry_isbn.place(x=350,y=48)

#____________Button_________

btn_select=Button(win,text='مشاهده همه',font='tahoma 9',width=14,command=select_record)
btn_select.place(x=377,y=87)

btn_search=Button(win,text='جستوجوی کتاب',font='tahoma 9',width=14,command=search_record)
btn_search.place(x=377,y=119)

btn_insert=Button(win,text='اضافه کردن کتاب',font='tahoma 9',width=14,command=insert_record)
btn_insert.place(x=377,y=151)

btn_delete=Button(win,text='حذف کردن',font='tahoma 9',width=14,command=delet_record)
btn_delete.place(x=377,y=183)

btn_close=Button(win,text='بستن',font='tahoma 9',width=14,command=close)
btn_close.place(x=377,y=215)

#______________Listbox__________

listbox=Listbox(win,width=53,height=9)
listbox.place(x=30,y=97)

sb = Scrollbar(win)
sb.place(x=335,y=99,height=150)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

win.mainloop()
