from imports import *

screen =customtkinter.CTk()
screen.title("Mass Mailer")
screen.geometry("500x300")
screen.resizable(False,False)
screen.configure(fg_color="#495867")


#------------------------------ FRAMES -----------------------------------#

logo_frame = customtkinter.CTkFrame(screen, width=200,
                               height=200,
                               fg_color="#c18c5d",
                               border_width=2,
                               border_color="gray25",
                               corner_radius=10)

#----------------------------- LABELS ------------------------------------#

logo = customtkinter.CTkLabel(screen,text='📑',bg_color="#c18c5d",font=("Arial",150),text_color="black")


#----------------------------- BUTTONS -------------------------------------#

send_button = customtkinter.CTkButton(screen,width=35,
                                 height=85,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#c18c5d",
                                 bg_color="#495867",
                                 text="Send \nmail",
                                 text_color="black",
                                 hover_color="#ecc8af",
                                 font=font1)

support_button = customtkinter.CTkButton(screen,width=30,
                                 height=30,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#c18c5d",
                                 bg_color="#495867",
                                 text=" Help ",
                                 text_color="black",
                                 hover_color="#ecc8af",
                                 font=font1)

login_button =  customtkinter.CTkButton(master=screen,
                                 width=30,
                                 height=30,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#c18c5d",
                                 bg_color="#495867",
                                 text="Login",
                                 text_color="black",
                                 hover_color="#ecc8af",
                                 font=font1)

to_mail_button =  customtkinter.CTkButton(master=screen,
                                 width=30,
                                 height=30,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#c18c5d",
                                 bg_color="#495867",
                                 text="Rcpnt",
                                 text_color="black",
                                 hover_color="#ecc8af",
                                 font=font1)



#------------------------------------------- ENTRYS --------------------------#

subject_entry = customtkinter.CTkEntry(screen,placeholder_text="Enter subject",
                                       corner_radius=10,width=150,height=30,
                                       font=font2,fg_color="#BBC6D3",border_color="gray25",
                                       placeholder_text_color="black",text_color="black")

text_box = customtkinter.CTkTextbox(screen,width=160,height=145,border_color="gray25",border_width=2,)


#-------------------------- PLACES ---------------------------#
login_button.place(x=400,y=60)
text_box.place(x=225,y=105)
subject_entry.place(x=230,y=65)
to_mail_button.place(x=400, y=130)
send_button.place(x=400, y=165)
support_button.place(x=400,y=95)
logo.place(x=20,y=55)
logo_frame.place(x=10,y=50)



#-----------------#
screen.mainloop() #
#-----------------#