
import json as O000O0OOO000OO0OO, requests as OO000O0000O000000
from time import strftime as O00OO00O000O0000O, gmtime as OOO0OOO0O00OO0000
import time as O0000OO000OO0O000, hmac as OO0O0000O000O000O, hashlib as OOOOOO0O0O0000O00, pdb as O0O00O000OO000OO0, colorama as OO0000OOOOOOO000O, PoloniexBot as O0O0OO0OO000000OO
try:
    from urllib import urlencode as O000O0OOO0OO000OO
    from urlparse import urljoin as OOOO0O0OOO00O000O
except ImportError:
    from urllib.parse import urlencode as O000O0OOO0OO000OO
    from urllib.parse import urljoin as OOOO0O0OOO00O000O

import logger as O00OOOO0OOOO000O0, configparser as O0OO00OO00OOOO000
nonce = str(int(O0000OO000OO0O000.time() * 1000))
config = O0OO00OO00OOOO000.ConfigParser()
config.readfp(open('config.txt'))
key = config.get('Poloniex', 'Key')
secret = config.get('Poloniex', 'Secret')
price = []
volume = []
names = []
priceNew = []
volumeNew = []
volumeDict = {}

def market():
    O00OOO0O00O0OO0O0 = 'https://poloniex.com/public?command=returnTicker'
    O0OO0O0O0000OOOO0 = OO000O0000O000000.get(O00OOO0O00O0OO0O0)
    O00OO000O0OOOO0O0 = O000O0OOO000OO0OO.loads(O0OO0O0O0000OOOO0.text)
    return O00OO000O0OOOO0O0


def main(OOOOOO0000000OOO0):
    OO00OOO0OOOO0OOO0 = input(OO0000OOOOOOO000O.Fore.CYAN + 'Price Percent Change? ' + OO0000OOOOOOO000O.Style.RESET_ALL)
    O00OOOO0OO0OO0O0O = input(OO0000OOOOOOO000O.Fore.CYAN + 'Volume Percent Change? ' + OO0000OOOOOOO000O.Style.RESET_ALL)
    if OOOOOO0000000OOO0 != None:
        OOOO0O0OO0OOOO000 = O0O0OO0OO000000OO.getBalance('BTC')
        OO000OOOO0O0OO0OO = O0O0OO0OO000000OO.USD_BTC_Price()
        OOOO0O00O00O000O0 = float(OOOO0O0OO0OOOO000) * float(OO000OOOO0O0OO0OO)
        print(OO0000OOOOOOO000O.Fore.RED + '_____________________________________________________________________' + OO0000OOOOOOO000O.Style.RESET_ALL)
        print(OO0000OOOOOOO000O.Fore.RED + 'Balance (BTC): ' + str(OOOO0O0OO0OOOO000) + OO0000OOOOOOO000O.Style.RESET_ALL)
        print(OO0000OOOOOOO000O.Fore.RED + 'Balance in USD: ' + str(OOOO0O00O00O000O0) + OO0000OOOOOOO000O.Style.RESET_ALL)
        print(OO0000OOOOOOO000O.Fore.RED + '_____________________________________________________________________' + OO0000OOOOOOO000O.Style.RESET_ALL)
        if platform.system() == 'Windows':
            O00000O00O00OO0O0 = input('[1] Risk Multiplier: ' + OO0000OOOOOOO000O.Style.RESET_ALL)
            OOOOOO0O0000OO00O = input('[2] % of bitcoin to spend: ' + OO0000OOOOOOO000O.Style.RESET_ALL)
            O000OOOO0OO0OO000 = input('[3] Profit %: ' + OO0000OOOOOOO000O.Style.RESET_ALL)
        else:
            O00000O00O00OO0O0 = input('[1] Risk Multiplier: ' + OO0000OOOOOOO000O.Style.RESET_ALL)
            OOOOOO0O0000OO00O = input('[2] % of bitcoin to spend: ' + OO0000OOOOOOO000O.Style.RESET_ALL)
            O000OOOO0OO0OO000 = input('[3] Profit %: ' + OO0000OOOOOOO000O.Style.RESET_ALL)
        OOOOOO0O0000OO00O, O000OOOO0OO0OO000 = percentageFix(OOOOOO0O0000OO00O, O000OOOO0OO0OO000)
    O0O0OOOO00OO0O0O0, O0000O00O0OOOOOOO = percentageFix(OO00OOO0OOOO0OOO0, O00OOOO0OO0OO0O0O)
    OOO00O00OOOOO0OOO = market()
    for O00O0OO000000O0OO in OOO00O00OOOOO0OOO:
        if 'BTC_' in O00O0OO000000O0OO:
            price.append(OOO00O00OOOOO0OOO[O00O0OO000000O0OO]['last'])
            volume.append(OOO00O00OOOOO0OOO[O00O0OO000000O0OO]['baseVolume'])
            names.append(O00O0OO000000O0OO)

    O0O00000O0O0O0OO0 = True
    O0O0O0OO0OOO0000O = 1
    O0O0OOO000O0OO0O0 = OO0000OOOOOOO000O.Fore.YELLOW + OO0000OOOOOOO000O.Back.BLUE
    OO00O0OOOO000000O = OO0000OOOOOOO000O.Style.RESET_ALL
    O00OOO0O000000OO0 = O00OOOO0OOOO000O0.getLogger('test')
    O00OOO0O000000OO0.critical('working')
    print(' ')
    while 1:
        if O0O00000O0O0O0OO0 == True:
            OOOO00O000O0O00O0 = market()
            for O00O0OO000000O0OO in OOOO00O000O0O00O0:
                if 'BTC_' in O00O0OO000000O0OO:
                    priceNew.append(OOOO00O000O0O00O0[O00O0OO000000O0OO]['last'])
                    volumeNew.append(OOOO00O000O0O00O0[O00O0OO000000O0OO]['baseVolume'])

            for O00O0OO000000O0OO in priceNew:
                O0OOO00OO0O0O0OOO = priceNew.index(O00O0OO000000O0OO)
                if float(O00O0OO000000O0OO) > float(price[O0OOO00OO0O0O0OOO]) + float(price[O0OOO00OO0O0O0OOO]) * float(O0O0OOOO00OO0O0O0) and float(volumeNew[O0OOO00OO0O0O0OOO]) > float(volume[O0OOO00OO0O0O0OOO]) + float(volume[O0OOO00OO0O0O0OOO]) * float(O0000O00O0OOOOOOO):
                    O0O0O0OOO0O00O00O = str(float(O00O0OO000000O0OO) / float(price[O0OOO00OO0O0O0OOO]))
                    O0O0OO0OO000OOOO0 = str(float(volumeNew[O0OOO00OO0O0O0OOO]) / float(volume[O0OOO00OO0O0O0OOO]))
                    print(O0O0OOO000O0OO0O0 + 'Time: ' + OO00O0OOOO000000O + timestamp())
                    print(O0O0OOO000O0OO0O0 + 'Name: ' + OO00O0OOOO000000O + names[O0OOO00OO0O0O0OOO])
                    print(O0O0OOO000O0OO0O0 + 'Price % Change: ' + OO00O0OOOO000000O + O0O0O0OOO0O00O00O[2:4] + '%')
                    print(O0O0OOO000O0OO0O0 + 'Volume % Change: ' + OO00O0OOOO000000O + O0O0OO0OO000OOOO0[2:4] + '%')
                    print(O0O0OOO000O0OO0O0 + 'Old Price: ' + OO00O0OOOO000000O + '%.8f' % float(price[O0OOO00OO0O0O0OOO]))
                    print(O0O0OOO000O0OO0O0 + 'New Price: ' + OO00O0OOOO000000O + '%.8f' % float(O00O0OO000000O0OO))
                    print(O0O0OOO000O0OO0O0 + 'Old Volume: ' + OO00O0OOOO000000O + '%.8f' % float(volume[O0OOO00OO0O0O0OOO]))
                    print(O0O0OOO000O0OO0O0 + 'New Volume: ' + OO00O0OOOO000000O + '%.8f' % float(volumeNew[O0OOO00OO0O0O0OOO]))
                    print('------------------------------')
                    if OOOOOO0000000OOO0 != None:
                        OOOO0O0OO0OOOO000 = O0O0OO0OO000000OO.getBalance('BTC')
                        OO0000OO0OO0OOO0O = float(OOOO0O0OO0OOOO000) * float(OOOOOO0O0000OO00O)
                        OOOOOO000O00OO0OO = names[O0OOO00OO0O0O0OOO].split('_')
                        BittrexBot.Trade(OOOOOO000O00OO0OO[0], O000OOOO0OO0OO000, OO0000OO0OO0OOO0O, O00000O00O00OO0O0)
                    price[O0OOO00OO0O0O0OOO] = priceNew[O0OOO00OO0O0O0OOO]
                    volume[O0OOO00OO0O0O0OOO] = volumeNew[O0OOO00OO0O0O0OOO]
                else:
                    price[O0OOO00OO0O0O0OOO] = priceNew[O0OOO00OO0O0O0OOO]
                    volume[O0OOO00OO0O0O0OOO] = volumeNew[O0OOO00OO0O0O0OOO]

            volumeNew[:] = []
            priceNew[:] = []
            O0000OO000OO0O000.sleep(1)


def timestamp():
    return O00OO00O000O0000O('%H:%M:%S', OOO0OOO0O00OO0000())


def percentageFix(O00000O00OOO00O00, OOOOOO0OOOO00O00O):
    if len(O00000O00OOO00O00) <= 1:
        O00000O00OOO00O00 = '0.0' + O00000O00OOO00O00
    else:
        if len(O00000O00OOO00O00) <= 2:
            O00000O00OOO00O00 = '0.' + O00000O00OOO00O00
        else:
            if len(O00000O00OOO00O00) <= 3:
                O00000O00OOO00O00 = O00000O00OOO00O00[0] + '.' + O00000O00OOO00O00[1:]
            else:
                O00000O00OOO00O00 = O00000O00OOO00O00[0:2]
            if len(OOOOOO0OOOO00O00O) <= 1:
                OOOOOO0OOOO00O00O = '0.0' + OOOOOO0OOOO00O00O
            else:
                if len(OOOOOO0OOOO00O00O) <= 2:
                    OOOOOO0OOOO00O00O = '0.' + OOOOOO0OOOO00O00O
                else:
                    if len(OOOOOO0OOOO00O00O) <= 3:
                        OOOOOO0OOOO00O00O = OOOOOO0OOOO00O00O[0] + '.' + OOOOOO0OOOO00O00O[1:]
                    else:
                        OOOOOO0OOOO00O00O = OOOOOO0OOOO00O00O[0:2]
    return (
     O00000O00OOO00O00, OOOOOO0OOOO00O00O)
