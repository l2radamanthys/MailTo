#!/usr/bin/env python
# -*- coding: utf-8 -*-


from email.MIMEText import MIMEText
import mimetypes

from sender import MailCont, MailSender


def main():
    #esta incompleto este es solo pla version base
    file = open('msj.txt', 'r')
    data = file.read()
    file.close()

    mensaje = MIMEText(data[1:])
    mensaje.set_type('text/plain')
    mensaje['Subject'] = data[0]

    d_list = open('dest.txt', 'r').readlines()
    m_cont = MailCont(d_list)

    acounts = []
    for obj in account_load():
        user, pswr serve_name = obj
        smtp_server, port, use_ssl = ACCOUNT_CONECTIONS[server]
        m_sender = MailSender(user, pswr, smtp_server, int(port), m_cont, mensaje)
        acounts.append(m_sender)
        del m_sender

    #comenzar envio
    for acount in acounts:
        acount.start()


if __name__ == '__main__':
    main()
