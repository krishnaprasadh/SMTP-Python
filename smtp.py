import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls() #TLS-Trasport Layer Security
print "#" * 50
print "Python SMTP"
print "#" * 50
username=raw_input("Enter your gmail username (Without @): ")
password=raw_input("Enter your password: ")
server.login(username,password)


sender=raw_input("Enter From address including @: ")
receiver=raw_input("Enter To mail id including @: ")
message=raw_input("Ener your message: ")

server.sendmail(sender,receiver,message)
server.quit()
