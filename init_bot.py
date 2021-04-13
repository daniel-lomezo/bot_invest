# -*- coding: utf-8 -*-
# Your code goes below this line

from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from dateutil import tz
import time, json


API = IQ_Option('daniel.ubletech@gmail.com', 'daniellomezo008090')
API.connect()
API.change_balance('PRACTICE')

while True:
    if API.check_connect() == False:
        print('Falha de login')
    else:
        print('Conectado com Sucesso')
        break
    time.sleep(1)

def convert_timestamp(x):

    hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    hora = hora.replace(tzinfo=tz.gettz('GMT'))
    return hora

def perfil():
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))
    return perfil

balance = API.get_balance()
print('O saldo da conta está em ', balance, '\n')
x = perfil()
print(x['name'])
print(x['nickname'])
print('A conta foi criada em ', convert_timestamp(x['created']))

modo_investimento = 'EURUSD'
velas = API.get_candles(modo_investimento, 5, 60, time.time())

for i in velas:
    API.connect()
    print(i, '\n')
