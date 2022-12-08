#!/usr/bin/python3.10.8
# coding: utf-8
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np 
username = "a.isli@noralsy.com"
password = "Vaw21317"
mail_from = "a.isli@noralsy.com"
mail_to_Abdel="a.isli@noralsy.com"
mail_to_yann = "y.cosson@noralsy.com"
mail_to_Baptiste="b.berthin@noralsy.com"
mail_subject = "Etat de parc pp4g"




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
QtePlatine = 0
for row in records:
        if (row[0] == "2.4.12 (pp4g)"):

                tab="Version = " + row[0]+ "\t" +"|| Qté = " + row[1] + " \n " 
                QtePlatine = QtePlatine + row[1]
        else:
                tab="Version = " + row[0]+ "\t\t" +"|| Qté = " + row[1] + " \n "
                taab.extend(tab)
                QtePlatine = QtePlatine + row[1]


print(taab)

cursor.close()

cnxSqlProd.close()
str1=" Liste des Versions et des Qtés par Version des PP4G || " + str(QtePlatine)+" platines : \n"
str = ' '.join(taab)
str.replace(',', '\n')
mail_body = str1+"\n"+str
#recipients = ['b.berthin@noralsy.com','y.cosson@noralsy.com','a.isli@noralsy.com']
recipients = ['isliabdelai@gmail.com','a.isli@noralsy.com']
mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=", ".join(recipients)
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()
