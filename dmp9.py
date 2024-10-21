from tkinter import *
from tkinter import messagebox
def submit_form():
    nm=ety_nm.get()
    ag=scale_age.get()
    gender=gender_var.get()
    if not nm:
        messagebox.showwarning('input Error','please enter valid name')
    else:
        messagebox.showinfo('form submited',f'Name: {nm}\nAge: {ag}\nGender: {gender}\nSubscribe to anime_web !')             
win = Tk()
win.title("Registration Form")
win.geometry("500x500")
msg=Message(win,text='Fill out the form below:',width=500,font=('times',10),bg='pink')
msg.pack(pady=10)
l_nm=Label(win,text='Name:',font=('times',10))
l_nm.pack(pady=10)
ety_nm=Entry(win,font=('times',10))
ety_nm.pack()
l_ag=Label(win,text='Age:',font=('times',10))
l_ag.pack(pady=10)
scale_age=Scale(win,from_=10,to=100,orient='horizontal',font=('times',10))
scale_age.pack(pady=10)
gender=Label(win,text='Gender:',font=('times',10))
gender.pack(pady=10)
gender_var=StringVar(value='male')
rm=Radiobutton(win,text='male',variable=gender_var,value='male',font=('times',10))
rf=Radiobutton(win,text='female',variable=gender_var,value='female',font=('times',10))
rm.pack()
rf.pack()
nl=IntVar()
chk_nl=Checkbutton(win,text='subscribe to anime_web',variable=nl,font=('times',19),bg='orange',fg='white')


chk_nl.pack(pady=10)
s_btn=Button(win,text='Submit',command=submit_form,font=('times',19),bg='blue',fg='white')
s_btn.pack(pady=10)
win.mainloop()
