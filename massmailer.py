from imports import *

screen =customtkinter.CTk()
screen.title("Mass Mailer")
screen.geometry("500x300")
screen.resizable(False,False)
screen.configure(fg_color="#495867")

file_path=""

#------------------------- FUNCTIONS -------------------------------------#

def get_rcpnt():
    global file_path
    file_path = filedialog.askopenfilename(title="Select file", filetypes=[("txt file", "*.txt")], initialdir="/", defaultextension=".txt")
    if file_path:

        mails = []

        with open(file_path, "r") as file:
            for line in file:
                mails.append(line.strip())
        
        json_data = {"mailler": mails}

        with open("mails.json", "w") as file:
            json.dump(json_data, file, indent=4)

def support_func():
    support ="https://t.me/HackerRick"
    webbrowser.open_new_tab(support)

def login_funct():

    def save_func():
        from_mail = mail_sender.get()
        apppassword = app_password.get()

        if from_mail == "":
            mail_sender.configure(border_color="red")
        if apppassword == "":
            app_password.configure(border_color="red")

        else:

            json_data = {"Email":from_mail,"Password":apppassword}

            with open("Login.json", "w") as file:
                json.dump(json_data, file, indent=4)

            fsave_button.configure(text="Saved!")

            mail_sender.delete(0,END)
            app_password.delete(0,END)

    tabview = customtkinter.CTkTabview(master=screen,width=490,height=280)
    tabview.place(x=5,y=5)

    tabview.add("tab 2")  # add tab at the end
    tabview.set("tab 2")  # set currently visible tab

    mail_sender =customtkinter.CTkEntry(tabview.tab("tab 2"),placeholder_text="Enter your mail",
                                       corner_radius=10,width=250,height=30,
                                       font=font2,fg_color="#BBC6D3",border_color="gray25",
                                       placeholder_text_color="black",text_color="black")
    
    app_password =customtkinter.CTkEntry(tabview.tab("tab 2"),placeholder_text="Enter app password",
                                       corner_radius=10,width=250,height=30,
                                       font=font2,fg_color="#BBC6D3",border_color="gray25",
                                       placeholder_text_color="black",text_color="black")
    mail_sender.place(x=120,y=30)
    app_password.place(x=120,y=65)
    
    def fback_func():
        tabview.destroy()

    fback_button = customtkinter.CTkButton(tabview.tab("tab 2"),width=30,
                                 height=30,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#c18c5d",
                                 bg_color="#495867",
                                 text="back",
                                 text_color="black",
                                 hover_color="#ecc8af",
                                 font=font1,
                                 command=fback_func)

    fsave_button = customtkinter.CTkButton(tabview.tab("tab 2"),width=30,
                                 height=30,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#c18c5d",
                                 bg_color="#495867",
                                 text="save",
                                 text_color="black",
                                 hover_color="#ecc8af",
                                 font=font1,
                                 command=save_func)
    
    fsave_button.place(x=250,y=150)
    
    
    fback_button.place(x=160,y=150)


def send_func():
    subject = subject_entry.get()
    text = text_box.get(1.0,END)

    if subject == "":
        subject_entry.configure(border_color="red")
    if text == "":
        text_box.configure(border_color="red")

    else:

        if file_path:

            mailss = []

            with open("mails.json", "r") as file:
                verii = json.load(file)
                mailler = verii["mailler"]
                mail_listesi = ",".join(mailler)
                

            with open("Login.json", "r") as dosya:
                veri = json.load(dosya)

            email = veri["Email"]
            password = veri["Password"]

            if email == "":
               login_button.configure(border_color="red")
            if password == "":
               login_button.configure(border_color="red")
            else:
                try:
                    content=text
                    mail=smtplib.SMTP('smtp.gmail.com', 587)
                    mail.ehlo()
                    mail.starttls()
                    sender=email
                    mail.login(email,password)
                    mail_listesi = mail_listesi.split(",")
                    print(mail_listesi)
                    for recipient in mail_listesi:
                        print(recipient)
                        content = ""
                        header='To:'+recipient+'\n'+'From:' \
                        +sender+'\n'+f'subject:{subject}\n'
                        content=header+content
                        mail.sendmail(sender, recipient, content)
                        print("success",recipient)
                
                    mail.quit()
                except KeyError as e:
                    print("error",e)
                
        else:
            to_mail_button.configure(border_color="red",border_width=2)

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
                                 font=font1,
                                 command=send_func)

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
                                 font=font1,
                                 command=support_func)

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
                                 font=font1,
                                 command=login_funct)

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
                                 font=font1,
                                 command=get_rcpnt)



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