from tkinter import *
root=Tk()
root.config(bg="Pink")
root.geometry("500x600")
root.title("Railway Ticket Booking")
label=Label(root,text='Ticket Booking',bg='Pink',font=('TimesNewRoman 15 bold')).place(x=150,y=0)
butt_1=Button(root,text="Login",width=7,bg="white").place(x=220,y=60)
butt_2=Button(root,text="Register",width=7,bg="white").place(x=220,y=100)
butt_3=Button(root,text="Exit",width=7,bg="white").place(x=220,y=140)
label=Label(root,text='Train Information',bg='Pink',font=('TimesNewRoman 15 bold')).place(x=150,y=200)
label=Label(root,text='Train no:     Train Name:  Source:  Destination:',bg='Pink',font=('TimesNewRoman 15 bold')).place(x=150,y=230)

label=Label(root,text='12711 \t\t  Pinakini SF Express \t Vijayawada \t Chennai',bg='Pink',font=('TimesNewRoman 7')).place(x=100,y=260)
label=Label(root,text='12616 \t\t  Grand Trank SF Express \t Delhi  \t\t Chennai',bg='Pink',font=('TimesNewRoman 7')).place(x=100,y=275)
label=Label(root,text='12925 \t\t  Paschim SF Express \t Mumbai \t\t New Delhi',bg='Pink',font=('TimesNewRoman 7')).place(x=100,y=290)
label=Label(root,text='12627 \t\t  Karnataka Express \t Bengaluru \t New Delhi',bg='Pink',font=('TimesNewRoman 7')).place(x=100,y=305)
label=Label(root,text='18047 \t\t  Amaravathi Express \t Vijayawada \t Vasco-do-Gama',bg='Pink',font=('TimesNewRoman 7')).place(x=100,y=320)
root.mainloop()



