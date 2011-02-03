#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ConfigParser

from mail import EMailAccount
from constantes import CFG_FILE, ACOUNT_LIST, ACCOUNT_CONECTIONS


def load_data():
    """
        Carga la configuracion
    """
    cfg = ConfigParser.ConfigParser()
    cfg.read(CFG_FILE)
    mail_list = cfg.get("CONFIG", 'mail_list')
    #acount_list= cfg.get("CONFIG", 'acount_list')
    mensaje = cfg.get("CONFIG", 'mensaje')
    msj_type = cfg.get("CONFIG", 'msj_type')


def account_load():
    """
        Carga el listado de cuentas que se utilizara para realizar el envio
    """
    acount_f = open(ACOUNT_LIST, 'r')
    data = acount_f.readlines()[1:]
    acount_data = []
    for line in data:
        res = line[:-1].split(';')
        if len(res) == 3:
            acount_data.append(res)
    return acount_data


def test_account(data, test_dest='l2radamanthys@gmail.com'):
    """
        Prueba la conecion con una cuenta y envia un mail de prueba
        al destinatario selecionado
    """
    user, pswr, server = data
    smtp_server, port, use_ssl = ACCOUNT_CONECTIONS[server]
    print "\tserver: %s\n\tport: %s\n\tuser: %s\n\tssl: %s\n" %(smtp_server, port, user, use_ssl)
    #conectar server
    acount = EMailAccount(user, pswr, use_ssl)
    acount.connect(server, port)
    #envio msj prueba
    acount.send_str(test_dest, "Msj de Prueba: Hola Mundo")
    #desconecion
    acount.cerrar()


#pueba de la lista de mails
def main():
    dest = "l2radamanthys@gmail.com"
    for obj in account_load():
        test_account(obj, dest)
        delay()



if __name__ == '__main__':

    main()
