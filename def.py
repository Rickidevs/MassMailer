content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender="t05906784@gmail.com"
recipient="elvinlatiflisite@gmail.com"
mail.login("t05906784@gmail.com","tiqv otxx viny zcbj")
header='To:'+recipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
print("success")
mail.close()
