from tkinter import *
from mysql import connector

con = connector.connect(host = "localhost" , user = "root" , password = "" , database = "p10c")
cur = con.cursor()

root = Tk()
root.title("Product Manager")

pid = 0

def add_product() :         #adds new record then clears entry fields and refreshesh listbox
    cur.execute("insert into product(pname , quantity) values(%s , %s)" , (pname_entry.get() , quantity_entry.get()))
    con.commit()
    clear()
    display_entry()
def modify_product():       #updates selected record then clears entry fields and refreshesh listbox
    cur.execute("update product set pname = %s , quantity = %s where pid = %s" , (pname_entry.get() , quantity_entry.get() , pid))
    con.commit()
    clear()
    display_entry()
def delete_product():
    cur.execute("delete from product where pid = %s" , (pid ,))
    con.commit()
    clear()
    display_entry()
def display_entry():
    listbox.delete(0 ,END)
    cur.execute("select * from product")
    for data in cur.fetchall():
        listbox.insert(END , f"{data[0]} {data[1]} {data[2]}\n")
def valueSelected(event):
    global pid
    index = listbox.curselection()[0]
    pid , newPname , newQty = listbox.get(index).split(" ")
    print(pid,newPname,newQty)
    pname_entry.insert(0 , newPname)
    quantity_entry.insert(0 , newQty)
def clear() :
    pname_entry.delete(0 , END)
    quantity_entry.delete(0 , END)
Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=10)
pname_entry = Entry(root, width=30)
pname_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
quantity_entry = Entry(root, width=30)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = Button(root, text="Add Product", command=add_product)
add_button.grid(row=2, column=0, padx=10, pady=10)

modify_button = Button(root, text="Modify Product", command=modify_product)
modify_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = Button(root, text="Delete Product", command=delete_product)
delete_button.grid(row=2, column=2, padx=10, pady=10)

listbox = Listbox(root, height=10, width=60)
listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

listbox.bind("<Double-1>" , valueSelected)

root.mainloop()
