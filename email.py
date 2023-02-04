#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:55:42 2023

@author: apolinar
"""

# pruebas de email
import socket

# información de socket
print(socket.getservbyport(25))
print(socket.gethostname())
#print(socket.gethostbyname(socket.gethostname))

from email.mime.text import MIMEText
msg = MIMEText("Hello There")
msg['Subject'] = "A Test Message"
msg['From']='Apolinar Ramirez <apolinar_r@yahoo.com>'
msg['To'] = 'José A <joseapolinaris86@gmail.com>'
# muestra contenido del mensaje
print(msg.as_string())

import smtplib
s = smtplib.SMTP('localhost')
# enviando el mensaje: remitente, [destinatario]
s.sendmail("apolinar_r@yahoo.com", ["joseapolinaris86@gmail.com"], msg.as_string())


