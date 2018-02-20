import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("avinashshekar12345@gmail.com","AvinashShekar87654321")
msg="Hi. How are you?"
s.sendmail("avinashshekar12345@gmail.com","brijeshsharma7975@gmail.com",msg)
print("success")
s.quit()           

