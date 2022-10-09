from http import server
import smtplib
FROM='kkipngenokoech22@gmail.com'
TO=['randomemail@gmail.com','flippibrian@gmail.com']
SUBJECT='TESTEMAILSEND'
TEXT='hello, i am just tasting if my code works so don\'t mind me'
messagesent=FROM,TO,SUBJECT,TEXT
server=smtplib.SMTP('localhost')
server.sendmail(FROM,TO,messagesent)
server.quit()