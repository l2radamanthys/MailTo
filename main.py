#!/usr/bin/env python
# -*- coding: utf-8 -*-


from email.MIMEText import MIMEText
import mimetypes

from sender import MailCont, MailSender
from constantes import CFG_FILE, ACOUNT_LIST, ACCOUNT_CONECTIONS

def main():
    #esta incompleto este es solo para probar
    #
    file = open('data/msj.txt', 'r')
    data = file.read()
    file.close()

    mensaje = MIMEText(data)
    mensaje.set_type('text/plain')
    mensaje['Subject'] = "Hola"

    d_list = open('data/dest.txt', 'r').readlines()
    m_cont = MailCont(d_list)
    data = open('data/acounts.dat', 'r').readlines()[1:]
    acounts = []
    for line in data:
        print line
        line = line.replace("\n", "")
        print line.split(';')
        user, pswr, server = line.split(';')
        smtp_server, port, use_ssl = ACCOUNT_CONECTIONS[server]
		acounts.append(MailSender(user, pswr, smtp_server, port, use_ssl, m_cont, mensaje))
		
			

    #enviar
    for acount in acounts:
        acount.start()


if __name__ == '__main__':
    main()
