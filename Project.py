from tkinter import *
import random
from PIL import ImageTk,Image
root=Tk()
root.geometry("900x500")
root.configure(bg="white")
img=ImageTk.PhotoImage(Image.open("C:\\Users\\royce\\Downloads\\Project_174_images_Student-20201211T172344Z-001\\Project_174_images_Student\\image"+str(random.randint(1, 5))+".jpg"))
Label_img=Label(root,image=img)
Label_img.place(relx=0.6,rely=0.5,anchor=CENTER)
Label_hospital=Label(root,font=("times",13,"bold"),fg="dark olive green",bg="white")
Label_hospital.place(relx=0.15,rely=0.39,anchor=CENTER)

Label_IT=Label(root,font=("times",13,"bold"),fg="dark olive green",bg="white")
Label_IT.place(relx=0.2,rely=0.69,anchor=CENTER)

Label_chemical=Label(root,font=("times",13,"bold"),bg="white",fg="dark olive green")
Label_chemical.place(relx=0.15,rely=0.96,anchor=CENTER)

Title=Label(root,text="Assigning Jobs", font=("times",30,"bold"),fg="dark olive green",bg="white")
Title.place(relx=0.15,rely=0.1,anchor=CENTER)
l1=Label(root,text="Doctor:",bg="white")
l1.place(relx=0.03,rely=0.2,anchor=CENTER)
Entry_doc=Entry()
Entry_doc.place(relx=0.13,rely=0.2,anchor=CENTER)
l1=Label(root,text="Doctor:",bg="white")
l1.place(relx=0.03,rely=0.2,anchor=CENTER)
Entry_doc=Entry()
Entry_doc.place(relx=0.13,rely=0.2,anchor=CENTER)
l2=Label(root,text="IT professional:",bg="white")
l2.place(relx=0.05,rely=0.5,anchor=CENTER)
Entry_it=Entry()
Entry_it.place(relx=0.18,rely=0.5,anchor=CENTER)
l3=Label(root,text="Chemical Engineer:",bg="white")
l3.place(relx=0.07,rely=0.8,anchor=CENTER)
Entry_che=Entry()
Entry_che.place(relx=0.2,rely=0.8,anchor=CENTER)
class Parent():
    def __init__(self):
        print("Find Job")
    def doctor(user):
        hospital_list=["Galaxy","Asian","Fortis","Apollo","AIIMS","Artemis"]
        hospital_selected=hospital_list[random.randint(0, 5)]
        Label_hospital["text"]=user+" has been alloted to "+hospital_selected
    def IT(it):
        it_list=["Tata Consultancy S","Infosys","HCL Technologies","Wipro Limited","Larsen Infotech","Tech Mahindra"]
        it_selected=it_list[random.randint(0, 5)]
        Label_IT["text"]=it+" has been alloted to "+it_selected
    def chemical(chemi):
        chemical_list=["BASF","Ineos","Reliance","DuPont"]
        chemical_selected=chemical_list[random.randint(0, 3)]
        Label_chemical["text"]=chemi+" has been alloted to "+chemical_selected
class doctor(Parent):
    def __init__(self,name):
        self.user=name
    def getDoctor(self):
        Parent.doctor(self.user)
class IT(Parent):
    def __init__(self,member):
        self.it=member
    def getmember(self):
        Parent.IT(self.it)
class Chemical(Parent):
    def __init__(self,members):
        self.chemi=members
    def getmembers(self):
        Parent.chemical(self.chemi)
def hos():
    hospital=doctor(Entry_doc.get())
    hospital.getDoctor()
def ut():
    It=IT(Entry_it.get())
    It.getmember()
def che():
    chemic=Chemical(Entry_che.get())
    chemic.getmembers()
btn_hospital=Button(root,text="Show the hospital alloted",command=hos,bg="#017bbe",relief="flat",fg="white")
btn_hospital.place(relx=0.09,rely=0.3,anchor=CENTER)

btn_IT=Button(root,text="Show the IT company alloted",command=ut,bg="#017bbe",relief="flat",fg="white")
btn_IT.place(relx=0.1,rely=0.6,anchor=CENTER)

btn_chemical=Button(root,text="Show the chemical company alloted",command=che,bg="#017bbe",relief="flat",fg="white")
btn_chemical.place(relx=0.12,rely=0.9,anchor=CENTER)
root.mainloop()