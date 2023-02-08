#IMPORT THE FOLLOWING MODULES
#IMPORT smtplib MODULE
import smtplib
#IMPORT EmailMessage MODULE
from email.message import EmailMessage
#IMPORT glob MODULE
import glob	
#Write Your message you want to email 
msg=EmailMessage()
#Subject of the Email
msg['Subject']="Birthday Invitiation"
#Sender of the Email
msg['From']="SQUAD Family"
#Person's  Email Username you want to send email
msg['To']="siddhant.sahay_cs21@gla.ac.in","rishabhsaxena577@gmail.com","abhijaat763@gmail.com","khushus7525@gmail.com","tanishkasharma225@gmail.com"
#Message to display on the email
msg.set_content("Greetings From SQUAD FAMILY")

#Add the Text file to the email
with open("fg.txt") as myfile:
    #READ THE FILE DATA IN TEXT FILE
    data=myfile.read()
    #CONNECTION TO THE EMAIL DATA
    msg.set_content(data)
#Add the Attachment file to the Email
for files in glob.glob("*.docx"):
    with open(files,"rb") as f:
        #READ THE FILE DATA IN ATTACHMENT DOCUMENT
        file_data=f.read()
        #NAME OF THE FILE	
        file_name=f.name
        #ADD ATTACHMENT TO THE EMAIL
        msg.add_attachment(file_data,maintype="application",subtype="docx",filename=file_name)
#Display the message if the attachment is done                                                       
print("Atttachment Done!!!")  

#Connection to the server of smtp 


    #SERVER NAME 
server= smtplib.SMTP_SSL('smtp.gmail.com',465)
    #LOGIN IN THE SERVER 
server.login("sahaysidd1503@gmail.com","siddhu@1503")
    #SEND THE MESSAGE
server.send_message(msg)
server.quit()
#Diplay the message if email is sent
print("Email Sent!!!!")
