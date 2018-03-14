import json as O00OOO00O0OOOO00O, requests as OOOO0OO00OOO00O00
from time import strftime as O0000O00O00OOO0OO, gmtime as O000O000O00OOO0O0
import time as O00000O000OOO0000, hmac as OOOO0OO0OOOOO0OOO, hashlib as OOO0O0000OOOOO000, pdb as OO0OO00000OOOOO0O, colorama as O0OO00OO0OOOOOOOO, CryptopiaBot as O0OOO0000O00OO0OO
try:
    from urllib import urlencode as OOO0OO0O00O0O000O
    from urlparse import urljoin as O0OOO0OOOO000OOO0
except ImportError:
    from urllib.parse import urlencode as OOO0OO0O00O0O000O
    from urllib.parse import urljoin as O0OOO0OOOO000OOO0

import logger as OOO00OO0O00OOO0O0, configparser as O000OO0OO00OOOOOO
nonce = str(int(O00000O000OOO0000.time() * 1000))
config = O000OO0OO00OOOOOO.ConfigParser()
config.readfp(open('config.txt'))
key = config.get('Cryptopia', 'Key')
secret = config.get('Cryptopia', 'Secret')
price = []
volume = []
volumeDict = {}

def market():
    OO0OOO00OOO0OO0O0 = 'https://www.cryptopia.co.nz/api/GetMarkets/BTC'
    O0000O00OOOOOOOOO = OOOO0OO00OOO00O00.get(OO0OOO00OOO0OO0O0)
    O0000O0OO0O0000O0 = O00OOO00O0OOOO00O.loads(O0000O00OOOOOOOOO.text)
    return O0000O0OO0O0000O0


def main(OOO0OOOOO0OOO0000):
    O000O0O0OOOO0OO0O = input(O0OO00OO0OOOOOOOO.Fore.CYAN + 'Price Percent Change? ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
    OOO00OOO0000O0OO0 = input(O0OO00OO0OOOOOOOO.Fore.CYAN + 'Volume Percent Change? ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
    if OOO0OOOOO0OOO0000 != None:
        O0O0OOO00O0O00OOO = O0OOO0000O00OO0OO.getBalance('BTC')
        OO000OOO00O0O0O0O = O0OOO0000O00OO0OO.USD_BTC_Price()
        OOOO0OO0000O000O0 = O0O0OOO00O0O00OOO * OO000OOO00O0O0O0O
        print(O0OO00OO0OOOOOOOO.Fore.RED + '_____________________________________________________________________' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
        print(O0OO00OO0OOOOOOOO.Fore.RED + 'Balance (BTC): ' + str(O0O0OOO00O0O00OOO) + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
        print(O0OO00OO0OOOOOOOO.Fore.RED + 'Balance in USD: ' + str(OOOO0OO0000O000O0) + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
        print(O0OO00OO0OOOOOOOO.Fore.RED + '_____________________________________________________________________' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
        if platform.system() == 'Windows':
            OO00O0OOOO000OOO0 = input('[1] Risk Multiplier: ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
            OO0OOOO00OO0O0000 = input('[2] % of bitcoin to spend: ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
            OOOOOOOOO0O00O00O = input('[3] Profit %: ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
        else:
            OO00O0OOOO000OOO0 = input('[1] Risk Multiplier: ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
            OO0OOOO00OO0O0000 = input('[2] % of bitcoin to spend: ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
            OOOOOOOOO0O00O00O = input('[3] Profit %: ' + O0OO00OO0OOOOOOOO.Style.RESET_ALL)
        OO0OOOO00OO0O0000, OOOOOOOOO0O00O00O = percentageFix(OO0OOOO00OO0O0000, OOOOOOOOO0O00O00O)
    OO00OOO00OO0OOOOO, O0OO000OOOOO000OO = percentageFix(O000O0O0OOOO0OO0O, OOO00OOO0000O0OO0)
    O00O00O00O0OO0OO0 = market()
    for O0OOOO00O00O0OOOO in O00O00O00O0OO0OO0['Data']:
        price.append(O0OOOO00O00O0OOOO['LastPrice'])
        volume.append(O0OOOO00O00O0OOOO['BaseVolume'])
        volumeDict[O0OOOO00O00O0OOOO['Label']] = []

    OO00O00O0OO0OO00O = True
    OOOOOOO00OO0O00OO = 1
    O00O0O00OOOOOO0O0 = O0OO00OO0OOOOOOOO.Fore.YELLOW + O0OO00OO0OOOOOOOO.Back.BLUE
    O0OO00O0O000O0O00 = O0OO00OO0OOOOOOOO.Style.RESET_ALL
    O0OOOOO0O00OOOOO0 = OOO00OO0O00OOO0O0.getLogger('test')
    O0OOOOO0O00OOOOO0.critical('working')
    print(' ')
    while 1:
        if OO00O00O0OO0OO00O == True:
            O00O00OOOO0OOOO00 = market()
            OOOOOOO00OO0O00OO += 1
            for O0OOOO00O00O0OOOO in O00O00OOOO0OOOO00['Data']:
                O00OOO0000O00OOOO = O00O00OOOO0OOOO00['Data'].index(O0OOOO00O00O0OOOO)
                if O0OOOO00O00O0OOOO['LastPrice'] > price[O00OOO0000O00OOOO] + price[O00OOO0000O00OOOO] * float(OO00OOO00OO0OOOOO) and O0OOOO00O00O0OOOO['BaseVolume'] > volume[O00OOO0000O00OOOO] + volume[O00OOO0000O00OOOO] * float(O0OO000OOOOO000OO):
                    O0O000O0OO0OOOO0O = str(O0OOOO00O00O0OOOO['LastPrice'] / price[O00OOO0000O00OOOO])
                    OOO00O0000O000OO0 = str(O0OOOO00O00O0OOOO['BaseVolume'] / volume[O00OOO0000O00OOOO])
                    print(O00O0O00OOOOOO0O0 + 'Time: ' + O0OO00O0O000O0O00 + timestamp())
                    print(O00O0O00OOOOOO0O0 + 'Name: ' + O0OO00O0O000O0O00 + O0OOOO00O00O0OOOO['Label'])
                    print(O00O0O00OOOOOO0O0 + 'Price % Change: ' + O0OO00O0O000O0O00 + O0O000O0OO0OOOO0O[2:4] + '%')
                    print(O00O0O00OOOOOO0O0 + 'Volume % Change: ' + O0OO00O0O000O0O00 + OOO00O0000O000OO0[2:4] + '%')
                    print(O00O0O00OOOOOO0O0 + 'Old Price: ' + O0OO00O0O000O0O00 + '%.8f' % price[O00OOO0000O00OOOO])
                    print(O00O0O00OOOOOO0O0 + 'New Price: ' + O0OO00O0O000O0O00 + '%.8f' % O0OOOO00O00O0OOOO['LastPrice'])
                    print(O00O0O00OOOOOO0O0 + 'Old Volume: ' + O0OO00O0O000O0O00 + '%.8f' % volume[O00OOO0000O00OOOO])
                    print(O00O0O00OOOOOO0O0 + 'New Volume: ' + O0OO00O0O000O0O00 + '%.8f' % O0OOOO00O00O0OOOO['BaseVolume'])
                    print('------------------------------')
                    if OOO0OOOOO0OOO0000 != None:
                        O0O0OOO00O0O00OOO = O0OOO0000O00OO0OO.getBalance('BTC')
                        O00OOOOO00OO0OO00 = O0O0OOO00O0O00OOO * float(OO0OOOO00OO0O0000)
                        OO00OO0O0O0OOOOO0 = O0OOOO00O00O0OOOO['Label'].split('/')
                        O0OOO0000O00OO0OO.Trade(OO00OO0O0O0OOOOO0[0], OOOOOOOOO0O00O00O, O00OOOOO00OO0OO00, OO00O0OOOO000OOO0)
                    price[O00OOO0000O00OOOO] = O0OOOO00O00O0OOOO['LastPrice']
                    volume[O00OOO0000O00OOOO] = O0OOOO00O00O0OOOO['BaseVolume']
                else:
                    price[O00OOO0000O00OOOO] = O0OOOO00O00O0OOOO['LastPrice']
                    volume[O00OOO0000O00OOOO] = O0OOOO00O00O0OOOO['BaseVolume']

            O00000O000OOO0000.sleep(3)


def timestamp():
    return O0000O00O00OOO0OO('%H:%M:%S', O000O000O00OOO0O0())


def percentageFix(O0O0O00000O0O0O0O, OOO000O000OOOO000):
    if len(O0O0O00000O0O0O0O) <= 1:
        O0O0O00000O0O0O0O = '0.0' + O0O0O00000O0O0O0O
    else:
        if len(O0O0O00000O0O0O0O) <= 2:
            O0O0O00000O0O0O0O = '0.' + O0O0O00000O0O0O0O
        else:
            if len(O0O0O00000O0O0O0O) <= 3:
                O0O0O00000O0O0O0O = O0O0O00000O0O0O0O[0] + '.' + O0O0O00000O0O0O0O[1:]
            else:
                O0O0O00000O0O0O0O = O0O0O00000O0O0O0O[0:2]
            if len(OOO000O000OOOO000) <= 1:
                OOO000O000OOOO000 = '0.0' + OOO000O000OOOO000
            else:
                if len(OOO000O000OOOO000) <= 2:
                    OOO000O000OOOO000 = '0.' + OOO000O000OOOO000
                else:
                    if len(OOO000O000OOOO000) <= 3:
                        OOO000O000OOOO000 = OOO000O000OOOO000[0] + '.' + OOO000O000OOOO000[1:]
                    else:
                        OOO000O000OOOO000 = OOO000O000OOOO000[0:2]
    return (
     O0O0O00000O0O0O0O, OOO000O000OOOO000)
