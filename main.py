#!/usr/bin/env python
# -*- coding: utf-8 -*-


from email.MIMEText import MIMEText
import mimetypes

from sender import MailCont, MailSender


def main():
    #esta incompleto este es solo para probar
    #
    file = open('msj.txt', 'r')
    data = file.read()
    file.close()

    mensaje = MIMEText(data)
    mensaje.set_type('text/plain')
    mensaje['Subject'] = data[0]

    d_list = open('dest.txt', 'r').readlines()
    m_cont = MailCont(d_list)
    data = open('acount.txt', 'r').readlines()
    acounts = []
    for line in data:
        user, pswr, server, port = line.split()
        acounts.append(MailSender(user, pswr, serv, port, m_cont, mensaje))

    #enviar
    for acount in acounts:
        acount.start()


if __name__ == '__main__':
    main()
