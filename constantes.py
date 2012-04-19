#!/usr/bin/env python
# -*- coding: utf-8 -*-


MSJ_DELAY = 0.5
USER_DELAY = 5.0
MAX_SEND = 15


#archivo de configuracion
CFG_FILE = 'data/conf.ini'
#lista de mails
ACOUNT_LIST = 'data/acounts.dat'

ACCOUNT_CONECTIONS = {
    #SERVER_NAME:(SMTP_SERVER, PORT, USE_SSL)
    "GMAIL":('smtp.gmail.com' , 587, True),
    "HOTMAIL":('smtp.live.com', 25, True),
    "YAHOO_AR":('smtp.mail.yahoo.com.ar', 587, False), #no confirmando
    "YAHOO_ES":('smtp.mail.yahoo.es', 587, False), #no confirmando
}
