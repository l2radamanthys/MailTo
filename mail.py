#!/usr/bin/env python
# -*- coding: utf-8 -*-


from smtplib import SMTP
from email.Encoders import encode_base64


class EMailAccount:
    def __init__(self, user, pswr, use_ssl=True):
        self.__server = SMTP()
        self.__user = user
        self.__pswr = pswr
        self.__use_ssl = use_ssl #si usa cifrado

        #caso que no se expecifique otra cuenta se usa la de login
        self.adress = self.__user
        #self.asunto = ''


    def connect(self, server, port):
        """
            Conecta con el servidor SMTP
        """
        self.__server.connect(server, port)
        #pregunta si es un servidor con cifrado SSL o TTL
        if self.__use_ssl:
            self.__server.ehlo()
            self.__server.starttls()
            self.__server.ehlo()
        self.__server.login(self.__user, self.__pswr)


    def send_one(self, from_addres='', to_adress='', asunto='', mensaje=None):
        """
            Envia un mensaje particular
        """
        mensaje['To'] = to_adress
        mensaje['From'] = from_addres
        mensaje['Subject'] = asunto
        self.__server.sendmail(from_adress, to_adress, mensaje.as_string())


    def send(self, address, mensaje):
        mensaje['To'] = address #destinatario
        #mensaje['From'] = self.addres #envia
        #mensaje['Subject'] = asunto #asunto
        self.__server.sendmail(self.addres, address, mensaje.as_string())


    def get_user(self):
        return self.__user


    def cerrar(self):
        self.__server.close()
