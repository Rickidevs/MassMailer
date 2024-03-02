from imports import *

screen =customtkinter.CTk()
screen.title("Mass Mailer")
screen.geometry("500x300")
screen.resizable(False,False)
screen.configure(fg_color="gray65")

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

    tabview = customtkinter.CTkTabview(master=screen,width=490,height=280,fg_color="gray65")
    tabview.place(x=5,y=5)

    tabview.add("Login")  # add tab at the end
    tabview.set("Login")  # set currently visible tab

    mail_sender =customtkinter.CTkEntry(tabview.tab("Login"),placeholder_text="Enter your mail",
                                       corner_radius=10,width=250,height=30,
                                       font=font2,fg_color="white",border_color="gray25",
                                       placeholder_text_color="black",text_color="black",bg_color="gray65")
    
    app_password =customtkinter.CTkEntry(tabview.tab("Login"),placeholder_text="Enter app password",
                                       corner_radius=10,width=250,height=30,
                                       font=font2,fg_color="white",border_color="gray25",
                                       placeholder_text_color="black",text_color="black",bg_color="gray65")
    mail_sender.place(x=120,y=30)
    app_password.place(x=120,y=65)
    
    def fback_func():
        tabview.destroy()

    fback_button = customtkinter.CTkButton(tabview.tab("Login"),width=30,
                                 height=30,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#0073B7",
                                 bg_color="gray65",
                                 text="back",
                                 text_color="white",
                                 hover_color="#00578A",
                                 font=font1,
                                 command=fback_func)

    fsave_button = customtkinter.CTkButton(tabview.tab("Login"),width=30,
                                 height=30,
                                 border_color="gray25",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#0073B7",
                                 bg_color="gray65",
                                 text="save",
                                 text_color="white",
                                 hover_color="#00578A",
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
        json_login_path = "Login.json"

        if  not os.path.exists(json_login_path):
            login_button.configure(border_color="red")
        
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

def reset_func():

    json_login_path = "Login.json"
    json_mails_path = "mails.json"

    if os.path.exists(json_login_path):
       os.remove(json_login_path)
    else:
        pass

    if os.path.exists(json_mails_path):
       os.remove(json_mails_path)
    else:
        pass
#------------------------------ FRAMES -----------------------------------#

logo_frame = customtkinter.CTkFrame(screen, width=200,
                               height=210,
                               fg_color="gray75",
                               border_width=2,
                               border_color="gray55",
                               corner_radius=10)


#----------------------------- BUTTONS -------------------------------------#

send_button = customtkinter.CTkButton(screen,width=35,
                                 height=30,
                                 border_color="#0073B7",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#00578A",
                                 bg_color="gray65",
                                 text="Send Mail",
                                 text_color="white",
                                 hover_color="#0073B7",
                                 font=font1,
                                 command=send_func)

support_button = customtkinter.CTkButton(screen,width=30,
                                 height=30,
                                 border_color="#C7C7C7",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#0073B7",
                                 bg_color="gray65",
                                 text=" Help ",
                                 text_color="white",
                                 hover_color="#00578A",
                                 font=font1,
                                 command=support_func)

login_button =  customtkinter.CTkButton(master=screen,
                                 width=30,
                                 height=30,
                                 border_color="#C7C7C7",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#0073B7",
                                 bg_color="gray65",
                                 text="Login",
                                 text_color="white",
                                 hover_color="#00578A",
                                 font=font1,
                                 command=login_funct)

to_mail_button =  customtkinter.CTkButton(master=screen,
                                 width=30,
                                 height=30,
                                 border_color="#C7C7C7",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#0073B7",
                                 bg_color="gray65",
                                 text="Rcpnt",
                                 text_color="white",
                                 hover_color="#00578A",
                                 font=font1,
                                 command=get_rcpnt)

reset_button =  customtkinter.CTkButton(master=screen,
                                 width=30,
                                 height=30,
                                 border_color="#C7C7C7",
                                 border_width=2,
                                 corner_radius=10,
                                 fg_color="#0073B7",
                                 bg_color="gray65",
                                 text="Reset",
                                 text_color="white",
                                 hover_color="#00578A",
                                 font=font1,
                                 command=reset_func)



#------------------------------------------- ENTRYS --------------------------#

subject_entry = customtkinter.CTkEntry(screen,placeholder_text="Enter subject",
                                       corner_radius=10,width=150,height=30,
                                       font=font2,fg_color="#FFFFFF",border_color="gray55",
                                       placeholder_text_color="#333333",text_color="#333333",bg_color="gray75")

text_box = customtkinter.CTkTextbox(screen,width=160,height=145,border_color="gray55",text_color="black",border_width=2,fg_color="#F2F2F2",bg_color="gray75")


#-------------------------- PLACES ---------------------------#
login_button.place(x=270,y=85)
text_box.place(x=60,y=95)
subject_entry.place(x=65,y=55)
to_mail_button.place(x=350, y=85)
send_button.place(x=290, y=165)
reset_button.place(x=350,y=125)
support_button.place(x=270,y=125)
logo_frame.place(x=40,y=45)



#-----------------#
screen.mainloop() #
#-----------------#