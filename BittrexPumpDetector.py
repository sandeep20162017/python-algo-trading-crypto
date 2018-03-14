
import json as OO0000O00O0OOO0OO, requests as O00OO0O0O00000OOO
from time import strftime as O0O00OO0OOOOOOO00, gmtime as O0OOOOOOO0OOOOOO0
import time as OOOOOOOO0O00000O0, hmac as O000O0O00OOO0OO00, hashlib as O00O0OO0O0OO0OOO0, pdb as OOOOOOOOOOO00OOO0, colorama as O000O0000O00O0OOO, platform as OOO00OO00OO000O0O, BittrexBot as OOO00OO00O0OOOOO0
try:
    from urllib import urlencode as O000OOOOO0O0O0000
    from urlparse import urljoin as OO0O0O0OOO0O00OO0
except ImportError:
    from urllib.parse import urlencode as O000OOOOO0O0O0000
    from urllib.parse import urljoin as OO0O0O0OOO0O00OO0

import logger as O000000OOO00OOOO0, configparser as OO000O0O000OOOO00
nonce = str(int(OOOOOOOO0O00000O0.time() * 1000))
config = OO000O0O000OOOO00.ConfigParser()
config.readfp(open('config.txt'))
key = config.get('Bittrex', 'Key')
secret = config.get('Bittrex', 'Secret')
price = []
volume = []
volumeDict = {}

def market():
    O000OO00O0O00OO0O = 'https://bittrex.com/api/v1.1/public/getmarketsummaries'
    OO000OOO00O0O00O0 = O00OO0O0O00000OOO.get(O000OO00O0O00OO0O, headers={'apisign': O000O0O00OOO0OO00.new(secret.encode(), O000OO00O0O00OO0O.encode(), O00O0OO0O0OO0OOO0.sha512).hexdigest()})
    O0O000O000OOO000O = OO0000O00O0OOO0OO.loads(OO000OOO00O0O00O0.text)
    return O0O000O000OOO000O


def main(O0O0OOOO0OO0O0O0O):
    OO0000OOO0OOO0OO0 = input(O000O0000O00O0OOO.Fore.CYAN + 'Price Percent Change? ' + O000O0000O00O0OOO.Style.RESET_ALL)
    OO0000O00O000OO00 = input(O000O0000O00O0OOO.Fore.CYAN + 'Volume Percent Change? ' + O000O0000O00O0OOO.Style.RESET_ALL)
    if O0O0OOOO0OO0O0O0O != None:
        OO0OOOOOOO000O0OO = OOO00OO00O0OOOOO0.getBalance('btc')
        OOOOOOO0OOO0O0O0O = OOO00OO00O0OOOOO0.USD_BTC_Price()
        O0000OOOO00000OO0 = OO0OOOOOOO000O0OO * OOOOOOO0OOO0O0O0O
        print(O000O0000O00O0OOO.Fore.RED + '_____________________________________________________________________' + O000O0000O00O0OOO.Style.RESET_ALL)
        print(O000O0000O00O0OOO.Fore.RED + 'Balance (BTC): ' + str(OO0OOOOOOO000O0OO) + O000O0000O00O0OOO.Style.RESET_ALL)
        print(O000O0000O00O0OOO.Fore.RED + 'Balance in USD: ' + str(O0000OOOO00000OO0) + O000O0000O00O0OOO.Style.RESET_ALL)
        print(O000O0000O00O0OOO.Fore.RED + '_____________________________________________________________________' + O000O0000O00O0OOO.Style.RESET_ALL)
        if OOO00OO00OO000O0O.system() == 'Windows':
            O000OOOO000000O00 = input('[1] Risk Multiplier: ' + O000O0000O00O0OOO.Style.RESET_ALL)
            OOOO0OO00O000OOOO = input('[2] % of bitcoin to spend: ' + O000O0000O00O0OOO.Style.RESET_ALL)
            OO000OO0OO00OOOOO = input('[3] Profit %: ' + O000O0000O00O0OOO.Style.RESET_ALL)
        else:
            O000OOOO000000O00 = input('[1] Risk Multiplier: ' + O000O0000O00O0OOO.Style.RESET_ALL)
            OOOO0OO00O000OOOO = input('[2] % of bitcoin to spend: ' + O000O0000O00O0OOO.Style.RESET_ALL)
            OO000OO0OO00OOOOO = input('[3] Profit %: ' + O000O0000O00O0OOO.Style.RESET_ALL)
        OOOO0OO00O000OOOO, OO000OO0OO00OOOOO = percentageFix(OOOO0OO00O000OOOO, OO000OO0OO00OOOOO)
    O00OO0OO0O000O0O0, OOOOO0OO0O0OOO00O = percentageFix(OO0000OOO0OOO0OO0, OO0000O00O000OO00)
    O0O0O000OOO0OO0OO = market()
    for O000OO0000O0OOO00 in O0O0O000OOO0OO0OO['result']:
        price.append(O000OO0000O0OOO00['Last'])
        volume.append(O000OO0000O0OOO00['Volume'])
        volumeDict[O000OO0000O0OOO00['MarketName']] = []

    O0OOOO000O00OO0OO = True
    O0O0OO00O00O0O00O = 1
    O0O000O00O00O000O = O000O0000O00O0OOO.Fore.YELLOW + O000O0000O00O0OOO.Back.BLUE
    OO00O0O000O0OOO00 = O000O0000O00O0OOO.Style.RESET_ALL
    OOO0O0000O000O0O0 = O000000OOO00OOOO0.getLogger('test')
    OOO0O0000O000O0O0.critical('working')
    print(' ')
    while 1:
        if O0OOOO000O00OO0OO == True:
            O00O00O0O00O0OOOO = market()
            O0O0OO00O00O0O00O += 1
            for O000OO0000O0OOO00 in O00O00O0O00O0OOOO['result']:
                O00OOO0O000O00000 = O00O00O0O00O0OOOO['result'].index(O000OO0000O0OOO00)
                if O000OO0000O0OOO00['Last'] > price[O00OOO0O000O00000] + price[O00OOO0O000O00000] * float(O00OO0OO0O000O0O0) and O000OO0000O0OOO00['Volume'] > volume[O00OOO0O000O00000] + volume[O00OOO0O000O00000] * float(OOOOO0OO0O0OOO00O):
                    O0O000OOOOOO0O0OO = str(O000OO0000O0OOO00['Last'] / price[O00OOO0O000O00000])
                    OO0OO0OO0OO0O00OO = str(O000OO0000O0OOO00['Volume'] / volume[O00OOO0O000O00000])
                    print(O0O000O00O00O000O + 'Time: ' + OO00O0O000O0OOO00 + timestamp())
                    print(O0O000O00O00O000O + 'Name: ' + OO00O0O000O0OOO00 + O000OO0000O0OOO00['MarketName'])
                    print(O0O000O00O00O000O + 'Price % Change: ' + OO00O0O000O0OOO00 + O0O000OOOOOO0O0OO[2:4] + '%')
                    print(O0O000O00O00O000O + 'Volume % Change: ' + OO00O0O000O0OOO00 + OO0OO0OO0OO0O00OO[2:4] + '%')
                    print(O0O000O00O00O000O + 'Old Price: ' + OO00O0O000O0OOO00 + '%.8f' % price[O00OOO0O000O00000])
                    print(O0O000O00O00O000O + 'New Price: ' + OO00O0O000O0OOO00 + '%.8f' % O000OO0000O0OOO00['Last'])
                    print(O0O000O00O00O000O + 'Old Volume: ' + OO00O0O000O0OOO00 + '%.8f' % volume[O00OOO0O000O00000])
                    print(O0O000O00O00O000O + 'New Volume: ' + OO00O0O000O0OOO00 + '%.8f' % O000OO0000O0OOO00['Volume'])
                    print('------------------------------')
                    if O0O0OOOO0OO0O0O0O != None:
                        OO0OOOOOOO000O0OO = OOO00OO00O0OOOOO0.getBalance('btc')
                        OOOO00O0OO0O00OOO = OO0OOOOOOO000O0OO * float(OOOO0OO00O000OOOO)
                        O0O0OOO0OO0OO0O00 = O000OO0000O0OOO00['MarketName'].split('-')
                        OOO00OO00O0OOOOO0.Trade(O0O0OOO0OO0OO0O00[1], OO000OO0OO00OOOOO, OOOO00O0OO0O00OOO, O000OOOO000000O00)
                    price[O00OOO0O000O00000] = O000OO0000O0OOO00['Last']
                    volume[O00OOO0O000O00000] = O000OO0000O0OOO00['Volume']
                else:
                    price[O00OOO0O000O00000] = O000OO0000O0OOO00['Last']
                    volume[O00OOO0O000O00000] = O000OO0000O0OOO00['Volume']

            OOOOOOOO0O00000O0.sleep(3)


def timestamp():
    return O0O00OO0OOOOOOO00('%H:%M:%S', O0OOOOOOO0OOOOOO0())


def percentageFix(O0OOOO0O0O000O0OO, OO00O00O00O00OO0O):
    if len(O0OOOO0O0O000O0OO) <= 1:
        O0OOOO0O0O000O0OO = '0.0' + O0OOOO0O0O000O0OO
    else:
        if len(O0OOOO0O0O000O0OO) <= 2:
            O0OOOO0O0O000O0OO = '0.' + O0OOOO0O0O000O0OO
        else:
            if len(O0OOOO0O0O000O0OO) <= 3:
                O0OOOO0O0O000O0OO = O0OOOO0O0O000O0OO[0] + '.' + O0OOOO0O0O000O0OO[1:]
            else:
                O0OOOO0O0O000O0OO = O0OOOO0O0O000O0OO[0:2]
            if len(OO00O00O00O00OO0O) <= 1:
                OO00O00O00O00OO0O = '0.0' + OO00O00O00O00OO0O
            else:
                if len(OO00O00O00O00OO0O) <= 2:
                    OO00O00O00O00OO0O = '0.' + OO00O00O00O00OO0O
                else:
                    if len(OO00O00O00O00OO0O) <= 3:
                        OO00O00O00O00OO0O = OO00O00O00O00OO0O[0] + '.' + OO00O00O00O00OO0O[1:]
                    else:
                        OO00O00O00O00OO0O = OO00O00O00O00OO0O[0:2]
    return (
     O0OOOO0O0O000O0OO, OO00O00O00O00OO0O)
