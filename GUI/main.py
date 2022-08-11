#Imports##########################################################################
import tkinter as tk
##################################################################################


#Functions########################################################################
def Homeframe():
    home_frame.lift()
    
def Lightframe():
    light_frame.lift()

def Mailframe():
    mail_frame.lift()
##################################################################################


##############
window=tk.Tk()
##############


#Variables########################################################################
app_colour="#4b4f4f"
home=tk.PhotoImage(file="home.png")
light=tk.PhotoImage(file="light.png")
mail=tk.PhotoImage(file="mail.png")
##################################################################################


#Application-Window###############################################################
window.title("Controller")
icon=tk.PhotoImage(file="keyboard.png")
window.wm_iconphoto(False,icon)
window.geometry("570x210")
window.config(background=app_colour)
window.resizable(False,False)
##################################################################################


#Navigation-Buttons###############################################################
home_button=tk.Button(window,image=home,background=app_colour,activebackground=app_colour,command=Homeframe)
home_button.grid(row=0,column=0)

light_button=tk.Button(window,image=light,background=app_colour,activebackground=app_colour,command=Lightframe)
light_button.grid(row=1,column=0)

mail_button=tk.Button(window,image=mail,background=app_colour,activebackground=app_colour,command=Mailframe)
mail_button.grid(row=2,column=0)
##################################################################################


#Light-Menu#######################################################################
light_frame=tk.Frame(window,background=app_colour,width=500,height=3*70)
light_frame.place(x=70,y=0)

light_label=tk.Label(light_frame,text="Light")
light_label.place(relx=0.5,rely=0.5)
##################################################################################


#Mail-Menu########################################################################
mail_frame=tk.Frame(window,background=app_colour,width=500,height=3*70)
mail_frame.place(x=70,y=0)

mail_label=tk.Label(mail_frame,text="Mail")
mail_label.place(relx=0.5,rely=0.5)
##################################################################################


#Home-Menu########################################################################
home_frame=tk.Frame(window,background=app_colour,width=500,height=3*70)
home_frame.place(x=70,y=0)

home_label=tk.Label(home_frame,text="Home")
home_label.place(relx=0.5,rely=0.5)
##################################################################################














#################
window.mainloop()
#################