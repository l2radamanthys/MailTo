#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from threading import Thread, Semaphore

from mail import EMailAccount
from constantes import *

class MailCont:
    def __init__(self, m_list):
        self.mutex = Semaphore(1) #barrera
        self.m_list = m_list


    def vacio(self):
        return not(len(m_list))


    def sacar(self, sender):
        self.mutex.acquire()
        if self.vacio():
            sender.enable = False
            m = sender.get_user()
        else:
            m = self.m_list.pop()
        self.mutex.release()
        return m


class MailSender(Thread):
    pid = 0
    def __init__(self, user, pswr, serv, port, cont, msj):
        Thread.__init__(self)
        self.account = EMailAccount(user, pswr)
        self.account.connect(serv, port)
        self.m_cont = cont #contenedor con los dest
        self.enable = True
        #
        self.pid = cls.pid
        cls.pid += 1


    def run(self):
        msj_cont = 0
        while self.enable:
            dest = self.m_cont.sacar()
            self.account.send(dest, msj)
            msj_cont += 1
            if msj_cont % MAX_SEND == 0:
                print "DURMIENDO HILO ",self.pid
                time.sleep(USER_DELAY)
                print "DESPERTANDO HILO ",self.pid
            else:
                time.sleep(random())
        print "EL HILO %d FINALIZO CON %d MAILS ENVIADOS" %(self.pid, msj_cont)


