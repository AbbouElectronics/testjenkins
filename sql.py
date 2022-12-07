import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np
username = "a.isli@noralsy.com"
password = "Vaw21317"
mail_from = "a.isli@noralsy.com"
mail_to = "isliabdelali@gmail.com"
mail_subject = "Test Subject"




cnxSqlProd = mysql.connector.connect(user='root', password='olwbnR2b6OI=olwbnR2b6OI=',
                              host='37.187.25.141',
                              database='campihome')

cursor = cnxSqlProd.cursor()

query = ("SELECT DISTINCT n4_version, COUNT(n4_version) FROM nph400s WHERE n4_type IN (1, 2) GROUP BY n4_version ORDER BY n4_version DESC")

cursor.execute(query)

records = cursor.fetchall()

print("Total number of rows in table: ", cursor.rowcount, "\n")
tab=[]
taab=[]
for row in records:
        tab=[f'Version = "{row[0]}|| Qté = {row[1]} ']
        taab.extend(tab)

print(taab)

cursor.close()

cnxSqlProd.close()
str = ' '.join(taab)
mail_body = str

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()
