#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from threading import Thread, Semaphore
from random import random

from mail import EMailAccount
from utils import account_load
from constantes import *


class MailCont:
    def __init__(self, m_list):
        self.mutex = Semaphore(1) #barrera
        self.m_list = m_list


    def vacio(self):
        return not(len(self.m_list))


    def sacar(self, sender):
        self.mutex.acquire()
        if self.vacio():
            sender.enable = False
            m = sender.account.get_user()
        else:
            m = self.m_list.pop()
            m = m.replace("\n", "")
        self.mutex.release()
        return m


class MailSender(Thread):
    id = 0
    def __init__(self, user, pswr, serv, port, cont, msj):
        Thread.__init__(self)
        self.account = EMailAccount(user, pswr)
        self.m_cont = cont #apuntador al contenedor con los dest
        self.enable = False
        self.id = MailSender.id
        MailSender.id += 1
        self.msj = msj

        #conecion automatica
        try:
            self.account.connect(serv, port)
            print "HILO %d ACOUNT %s CONECTADO" %(self.id, self.account.get_user())
            self.enable = True
        except:
            print "ERROR FALLO CONECION %s" %self.account.get_user()
            self.enable = False


    def run(self):
        msj_cont = 0
        while self.enable:
            dest = self.m_cont.sacar(self)
            self.account.send(dest, self.msj)
            print "HILO %d MSJ ENVIADO A %s" %(self.id, dest)
            msj_cont += 1
            time.sleep(random())
            if msj_cont % MAX_SEND == 0:
                print "DURMIENDO HILO ",self.id
                time.sleep(USER_DELAY)
                print "DESPERTANDO HILO ",self.id

        print "EL HILO %d FINALIZO CON %d MAILS ENVIADOS" %(self.id, msj_cont)


