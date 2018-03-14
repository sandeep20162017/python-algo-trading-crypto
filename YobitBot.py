
import json as O00OO0O00OOO0OO00, requests as OOOO00OOOO0OO0O00
from time import strftime as O0OO0OO0O0O0OO000, gmtime as O0OOOOO000OOOO00O
import time as OO000OO000O0OOOOO, hmac as O0OO0OOOOOO0OOOO0, hashlib as O00OO0O00000000O0, pprint as OOOO0000000O0O000, pdb as O0OO00000000OO0O0, platform as OO000OOOOOO00O000, colorama as OO00000O00000OO0O, utils as OOOO0OOOOO0OO00OO, datetime as OO0OO0OO0O00OOO0O, random as O00000OO0O0O000OO
try:
    from urllib import urlencode as OO00OO00O00O0O000
    from urlparse import urljoin as OO0OOOOO0000O000O
except ImportError:
    from urllib.parse import urlencode as OO00OO00O00O0O000
    from urllib.parse import urljoin as OO0OOOOO0000O000O

import configparser as OO00OO0OOOO0O0O00, sys as OO0O00O00000000O0
OO0O00O00000000O0.setrecursionlimit(10000)
config = OO00OO0OOOO0O0O00.ConfigParser()
config.readfp(open('config.txt'))
key = config.get('Yobit', 'Key')
secret = config.get('Yobit', 'Secret')
secret = bytes(secret, 'utf8')
BuyPercent = config.get('PriceLip', 'BuyPercent')
SellPercent = config.get('PriceLip', 'SellPercent')
BuyPercent, SellPercent = OOOO0OOOOO0OO00OO.percentageFix(BuyPercent, SellPercent)

def nonceHandler():
    OOOO0O0OO0O0O00O0 = open('nonce.txt')
    OOOOO0O00OOO00O00 = OOOO0O0OO0O0O00O0.readlines()
    OOOO0O0OO0O0O00O0.close()
    O000O0OO00O0OOOOO = int(OOOOO0O00OOO00O00[0]) + 1
    OOOOOO0000OO00000 = open('nonce.txt', 'w+')
    OOOOOO0000OO00000.write(str(O000O0OO00O0OOOOO))
    OOOOOO0000OO00000.close()
    return O000O0OO00O0OOOOO


def generate_nonce(length=9):
    """"""
    return ('').join([str(O00000OO0O0O000OO.randint(0, 9)) for O0000O000OO0O00OO in range(length)])


def mean(OOO00OO0OO0OOOOO0):
    return float(sum(OOO00OO0OO0OOOOO0)) / max(len(OOO00OO0OO0OOOOO0), 1)


def getTicker(O00OOOO00OO0OOO0O):
    O0O0O00O00OO00OO0 = 'https://yobit.net/api/3/ticker/' + O00OOOO00OO0OOO0O + '_btc'
    O000O0O0OO00OOO00 = OOOO00OOOO0OO0O00.get(O0O0O00O00OO00OO0, headers={'apisign': O0OO0OOOOOO0OOOO0.new(secret, O0O0O00O00OO00OO0.encode(), O00OO0O00000000O0.sha512).hexdigest()})
    O00000000OO00O0O0 = O00OO0O00OOO0OO00.loads(O000O0O0OO00OOO00.text)
    return O00000000OO00O0O0[O00OOOO00OO0OOO0O + '_btc']['last']


def getBalance(O0O000O000OO0O000):
    O0O00O0O0O00OOO0O = {}
    O0O0O00O000O0O0OO = 'https://yobit.net/tapi'
    OO00OOO0000O00OO0 = None
    while OO00OOO0000O00OO0 == None:
        OO00OOOO00O000O00 = nonceHandler()
        O0O00O0O0O00OOO0O['method'] = 'getInfo'
        O0O00O0O0O00OOO0O['nonce'] = OO00OOOO00O000O00
        OO00OO0O00O000OO0 = OO00OO00O00O0O000(O0O00O0O0O00OOO0O)
        O0OO0000000O0000O = O0OO0OOOOOO0OOOO0.new(secret, OO00OO0O00O000OO0.encode('utf8'), O00OO0O00000000O0.sha512).hexdigest()
        OOOOOO00O00OOO00O = {'Content-Type': 'application/x-www-form-urlencoded','Key': key,'Sign': O0OO0000000O0000O}
        OOOOO00O0OO0O0O0O = OOOO00OOOO0OO0O00.post(O0O0O00O000O0O0OO, data=O0O00O0O0O00OOO0O, headers=OOOOOO00O00OOO00O)
        OO0000OO0OOOOO0OO = O00OO0O00OOO0OO00.loads(OOOOO00O0OO0O0O0O.text)
        if O0O000O000OO0O000 in OO0000OO0OOOOO0OO['return']['funds']:
            return OO0000OO0OOOOO0OO['return']['funds'][O0O000O000OO0O000]
            OO00OOO0000O00OO0 = 1


def getOrder(O0000O0O0O0O00O0O):
    O00OOOO0O0OO0O0OO = nonceHandler()
    OO00O00OOOO0OO0OO = {}
    O00O00OOO0OO00OO0 = 'https://yobit.net/tapi'
    OO00O00OOOO0OO0OO['method'] = 'OrderInfo'
    OO00O00OOOO0OO0OO['nonce'] = O00OOOO0O0OO0O0OO
    OO00O00OOOO0OO0OO['order_id'] = O0000O0O0O0O00O0O
    OO0000O0O0000O0OO = OO00OO00O00O0O000(OO00O00OOOO0OO0OO)
    O00OO0OOO00O0O0OO = O0OO0OOOOOO0OOOO0.new(secret, OO0000O0O0000O0OO.encode('utf8'), O00OO0O00000000O0.sha512).hexdigest()
    OO0OO0O0O000OOOO0 = {'Content-Type': 'application/x-www-form-urlencoded','Key': key,'Sign': O00OO0OOO00O0O0OO}
    OO0OOOO000000O0OO = OOOO00OOOO0OO0O00.post(O00O00OOO0OO00OO0, data=OO00O00OOOO0OO0OO, headers=OO0OO0O0O000OOOO0)
    OO000OOO00O0OOO0O = O00OO0O00OOO0OO00.loads(OO0OOOO000000O0OO.text)
    return OO000OOO00O0OOO0O['return'][O0000O0O0O0O00O0O]


def buyOrder(O0OOOO0000000OOO0, O0OO000O0OO0OO00O):
    O000O0O000OO00OOO = nonceHandler()
    O0O00O0O0OO00000O = getTicker(O0OOOO0000000OOO0)
    OOO00O000OOO00OOO = O0O00O0O0OO00000O * (1 + float(BuyPercent))
    OOO0OO0O0OO000OO0 = {}
    OOOO0OOO000O0O00O = 'https://yobit.net/tapi'
    OOO0OO0O0OO000OO0['method'] = 'Trade'
    OOO0OO0O0OO000OO0['nonce'] = O000O0O000OO00OOO
    OOO0OO0O0OO000OO0['pair'] = O0OOOO0000000OOO0 + '_btc'
    OOO0OO0O0OO000OO0['type'] = 'buy'
    OOO0OO0O0OO000OO0['rate'] = str(OOO00O000OOO00OOO)
    OOO0OO0O0OO000OO0['amount'] = O0OO000O0OO0OO00O
    OOO00OO0O0OOO0O00 = OO00OO00O00O0O000(OOO0OO0O0OO000OO0)
    OOOO00O000OOOOO0O = O0OO0OOOOOO0OOOO0.new(secret, OOO00OO0O0OOO0O00.encode('utf8'), O00OO0O00000000O0.sha512).hexdigest()
    O000000OOO0OO0O0O = {'Content-Type': 'application/x-www-form-urlencoded','Key': key,'Sign': OOOO00O000OOOOO0O}
    OOO00OOOOOOOOO0O0 = OOOO00OOOO0OO0O00.post(OOOO0OOO000O0O00O, data=OOO0OO0O0OO000OO0, headers=O000000OOO0OO0O0O)
    OOOO0O0O00000000O = O00OO0O00OOO0OO00.loads(OOO00OOOOOOOOO0O0.text)
    if OOOO0O0O00000000O['success'] == 0:
        OO0O00O00000000O0.exit(OOOO0O0O00000000O['error'])
    else:
        OO0OOO00000000OOO = OOOO0O0O00000000O['return']['order_id']
        OOO000OO0000OO000 = [OO0OOO00000000OOO, OOO00O000OOO00OOO]
        return OOO000OO0000OO000


def sellOrder(OOO0OO0O000OO0O0O, OOO00O00O0O0O0000):
    O0O0OO0O00O00OO0O = getBalance(OOO0OO0O000OO0O0O)
    O0O0O0O000O00O00O = nonceHandler()
    OOOOOO00O0O00000O = {}
    O00OOOO0O00OOO0O0 = 'https://yobit.net/tapi'
    OOOOOO00O0O00000O['method'] = 'Trade'
    OOOOOO00O0O00000O['nonce'] = O0O0O0O000O00O00O
    OOOOOO00O0O00000O['pair'] = OOO0OO0O000OO0O0O + '_btc'
    OOOOOO00O0O00000O['type'] = 'sell'
    OOOOOO00O0O00000O['rate'] = OOO00O00O0O0O0000
    OOOOOO00O0O00000O['amount'] = O0O0OO0O00O00OO0O
    OOOO00OO0000O0O00 = OO00OO00O00O0O000(OOOOOO00O0O00000O)
    OO0OO0OOOOO00OO00 = O0OO0OOOOOO0OOOO0.new(secret, OOOO00OO0000O0O00.encode('utf8'), O00OO0O00000000O0.sha512).hexdigest()
    O00O0O0OO0000O00O = {'Content-Type': 'application/x-www-form-urlencoded','Key': key,'Sign': OO0OO0OOOOO00OO00}
    OOOOOOO00OO00OOO0 = OOOO00OOOO0OO0O00.post(O00OOOO0O00OOO0O0, data=OOOOOO00O0O00000O, headers=O00O0O0OO0000O00O)
    O000O0000OO00000O = O00OO0O00OOO0OO00.loads(OOOOOOO00OO00OOO0.text)
    OO00OOO0O00OOO00O = O000O0000OO00000O['return']['order_id']
    return OO00OOO0O00OOO00O


def marketHistory(OOOOO0OOO0O00O00O):
    OO0O0OOO000OO0O0O = 'https://yobit.net/api/3/trades/' + OOOOO0OOO0O00O00O + '_btc'
    O0OOO0O0O000OO0O0 = OOOO00OOOO0OO0O00.get(OO0O0OOO000OO0O0O, headers={'apisign': O0OO0OOOOOO0OOOO0.new(secret, OO0O0OOO000OO0O0O.encode(), O00OO0O00000000O0.sha512).hexdigest()})
    OOOOO00000OO0O00O = O00OO0O00OOO0OO00.loads(O0OOO0O0O000OO0O0.text)
    OO0OO0OO0O00OOO0O.datetime.fromtimestamp(1499275110).strftime('%H:%M')
    with open('mh.json', 'w') as (O00O0OO00O0OO0OOO):
        O00OO0O00OOO0OO00.dump(OOOOO00000OO0O00O, O00O0OO00O0OO0OOO)
    O000O00O0O0OO0000 = []
    OOOOOOOO0OO000OO0 = []
    for O0O0O00OOO00000O0 in OOOOO00000OO0O00O[OOOOO0OOO0O00O00O + '_btc']:
        O000O00O0O0OO0000.append(O0O0O00OOO00000O0['price'])
        OOOOOOOO0OO000OO0.append(O0O0O00OOO00000O0['timestamp'])

    O0O0OO0O0O00O0OO0 = OOOOOOOO0OO000OO0[0]
    O0OOO00000OO0O0O0 = OO0OO0OO0O00OOO0O.datetime.fromtimestamp(O0O0OO0O0O00O0OO0).strftime('%M')
    O0O0O00O0OO000OO0 = 0
    OO00000O0O000O00O = 0
    for O0O0O00OOO00000O0 in OOOOOOOO0OO000OO0:
        OOO000OO0000O0000 = OO0OO0OO0O00OOO0O.datetime.fromtimestamp(O0O0O00OOO00000O0).strftime('%M')
        if float(OOO000OO0000O0000) == float(O0OOO00000OO0O0O0) - 1:
            O0O0O00O0OO000OO0 = OOOOOOOO0OO000OO0.index(O0O0O00OOO00000O0)
            OO00000O0O000O00O = O000O00O0O0OO0000[O0O0O00O0OO000OO0]
            break

    O0O0OOO0O000O0O0O = 0
    OOO0O00O00O0OO0OO = 0
    for O0O0O00OOO00000O0 in OOOOOOOO0OO000OO0:
        OOO000OO0000O0000 = OO0OO0OO0O00OOO0O.datetime.fromtimestamp(O0O0O00OOO00000O0).strftime('%M')
        if float(OOO000OO0000O0000) == float(O0OOO00000OO0O0O0) - 2:
            O0O0OOO0O000O0O0O = OOOOOOOO0OO000OO0.index(O0O0O00OOO00000O0)
            OOO0O00O00O0OO0OO = O000O00O0O0OO0000[O0O0OOO0O000O0O0O]
            break

    return (
     OO00000O0O000O00O, OOO0O00O00O0OO0OO)


def Trade(OO0OOOOOO0OOO0000, O00OOO0000000OO0O, OO000O000OOO0OOO0, OOOOO00O00O0O0OO0):
    O000OOOO000OOOO00 = OO00000O00000OO0O.Fore.YELLOW + OO00000O00000OO0O.Back.BLUE + '['
    O000OO0OO0OOOO0OO = ']' + OO00000O00000OO0O.Style.RESET_ALL + ' '
    OOOOO0OO0O0000O0O = OO00000O00000OO0O.Fore.YELLOW
    O000O0O0OOO0OO0O0 = OO00000O00000OO0O.Style.RESET_ALL
    print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Symbol: ' + O000O0O0OOO0OO0O0 + OO0OOOOOO0OOO0000)
    O000000O00OOO000O = getTicker(OO0OOOOOO0OOO0000)
    print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Current Price: ' + O000O0O0OOO0OO0O0 + '%.8f' % O000000O00OOO000O)
    O0O0000OO0O000OOO = USD_BTC_Price()
    OOOO0O0O00O0OO0OO = getBalance('btc')
    OO0OOOO00O0OO00O0 = OOOO0O0O00O0OO0OO * O0O0000OO0O000OOO
    O0OO00O0O0000O0OO = OO000O000OOO0OOO0 * O0O0000OO0O000OOO
    print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Bitcoin Balance:  ' + O000O0O0OOO0OO0O0 + '%.8f' % OOOO0O0O00O0OO0OO + ' | $' + '%.2f' % OO0OOOO00O0OO00O0)
    print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Amount to use:  ' + O000O0O0OOO0OO0O0 + '%.8f' % OO000O000OOO0OOO0 + ' | $' + '%.2f' % O0OO00O0O0000O0OO)
    O0OO00OOO0OOO0O0O = OO000O000OOO0OOO0 / O000000O00OOO000O
    print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Amount To Purchase: ' + O000O0O0OOO0OO0O0 + '%.8f' % O0OO00OOO0OOO0O0O)
    print('------------------------------------' + O000O0O0OOO0OO0O0)
    print(' ')
    O0OOOO0OO0O00OO00, O0000OOOOOOO00000 = marketHistory(OO0OOOOOO0OOO0000)
    if float(OOOOO00O00O0O0OO0) != 0:
        O0OOOO0OO0O00OO00, O0000OOOOOOO00000 = marketHistory(OO0OOOOOO0OOO0000)
        O0OO0O00O0OOOO000 = config.get('RiskMultiplier', OOOOO00O00O0O0OO0)
        O000O00O000000O00 = O0OOOO0OO0O00OO00 * float(O0OO0O00O0OOOO000)
        O0O000O0OOO0O0O00 = O0000OOOOOOO00000 * float(O0OO0O00O0OOOO000)
        if O0OOOO0OO0O00OO00 != 0 and O000000O00OOO000O + O000000O00OOO000O * float(O00OOO0000000OO0O) >= O000O00O000000O00:
            print('Buy conditions not met, canceling order.')
            print('price 1')
            O0O0O0OOO0O0OO00O = O000000O00OOO000O * O0O0000OO0O000OOO
            print('Last Price: BTC ' + '%.8f' % O000000O00OOO000O + ' | $' + '%.2f' % O0O0O0OOO0O0OO00O)
            O00O0OO0OO00O000O = O000000O00OOO000O + O000000O00OOO000O * float(O00OOO0000000OO0O)
            OO0000OO00OO000O0 = O00O0OO0OO00O000O * O0O0000OO0O000OOO
            print('Potential Sell Price: BTC ' + '%.2f' % O00O0OO0OO00O000O + ' | $' + '%.2f' % OO0000OO00OO000O0)
            OOOOOO0000OOO00OO = O000O00O000000O00 * O0O0000OO0O000OOO
            print('Price Limit: BTC ' + '%.8f' % O000O00O000000O00 + ' | $' + '%.2f' % OOOOOO0000OOO00OO)
            O000OOOO000OOOO00 = getTicker(OO0OOOOOO0OOO0000)
            O000000000OO0O00O = O000OOOO000OOOO00 * O0O0000OO0O000OOO
            print('Current Price: BTC ' + '%.8f' % O000OOOO000OOOO00 + ' | $' + '%.2f' % O000000000OO0O00O)
            return
        if O0000OOOOOOO00000 != 0 and O000000O00OOO000O + O000000O00OOO000O * float(O00OOO0000000OO0O) >= O0O000O0OOO0O0O00:
            print('Buy conditions not met, canceling order.')
            print('price 2')
            O0O0O0OOO0O0OO00O = O000000O00OOO000O * O0O0000OO0O000OOO
            print('Last Price: BTC ' + '%.8f' % O000000O00OOO000O + ' | $' + '%.2f' % O0O0O0OOO0O0OO00O)
            O00O0OO0OO00O000O = O000000O00OOO000O + O000000O00OOO000O * float(O00OOO0000000OO0O)
            OO0000OO00OO000O0 = O00O0OO0OO00O000O * O0O0000OO0O000OOO
            print('Potential Sell Price: BTC ' + '%.2f' % O00O0OO0OO00O000O + ' | $' + '%.2f' % OO0000OO00OO000O0)
            OOOOOO0000OOO00OO = O000O00O000000O00 * O0O0000OO0O000OOO
            print('Price Limit: BTC ' + '%.8f' % O000O00O000000O00 + ' | $' + '%.2f' % OOOOOO0000OOO00OO)
            O000OOOO000OOOO00 = getTicker(OO0OOOOOO0OOO0000)
            O000000000OO0O00O = O000OOOO000OOOO00 * O0O0000OO0O000OOO
            print('Current Price: BTC ' + '%.8f' % O000OOOO000OOOO00 + ' | $' + '%.2f' % O000000000OO0O00O)
            return
        O0O0OOO000O0OO0O0 = buyOrder(OO0OOOOOO0OOO0000, O0OO00OOO0OOO0O0O)
        OO000O0O00000OO00 = True
        print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Placing Order...')
        while OO000O0O00000OO00:
            OOOO0OO00O00O00O0 = getOrder(str(O0O0OOO000O0OO0O0[0]))
            if OOOO0OO00O00O00O0['status'] == 1:
                print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Order Successful!')
                print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Price: ' + O000O0O0OOO0OO0O0 + '%.8f' % OOOO0OO00O00O00O0['rate'])
                print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Bitcoin Balance: ' + O000O0O0OOO0OO0O0 + '%.8f' % getBalance('btc'))
                print('------------------------------------')
                print(' ')
                OO000O0O00000OO00 = False

        OOOO0OO00O00O00O0 = getOrder(str(O0O0OOO000O0OO0O0[0]))
        OOO00OO0OOOO0OO00 = OOOO0OO00O00O00O0['rate'] * float(O00OOO0000000OO0O)
        O000O0OO00OOO0OOO = OOOO0OO00O00O00O0['rate'] + OOO00OO0OOOO0OO00
        O00OO00OOOOOOOOO0 = O000O0OO00OOO0OOO / (1 + float(SellPercent))
        OO0OOO0O0O0OO0OOO = sellOrder(OO0OOOOOO0OOO0000, O00OO00OOOOOOOOO0)
        print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Sell Order Placed!')
        print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Price: ' + O000O0O0OOO0OO0O0 + '%.8f' % O00OO00OOOOOOOOO0)
        print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Patiently Waiting...' + O000O0O0OOO0OO0O0)
        O0O0OO00OO000OO0O = True
        while O0O0OO00OO000OO0O:
            OOOO0OO00O00O00O0 = getOrder(str(OO0OOO0O0O0OO0OOO))
            print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Current Price: ' + O000O0O0OOO0OO0O0 + '%.8f' % getTicker(OO0OOOOOO0OOO0000), end='\r')
            if OOOO0OO00O00O00O0['status'] == 1:
                print('------------------------------------')
                print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Sold!')
                print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Bitcoin Balance: ' + O000O0O0OOO0OO0O0 + '%.8f' % getBalance('btc'))
                O0O0000OO0O000OOO = USD_BTC_Price()
                print(O000OOOO000OOOO00 + O0OO0OO0O0O0OO000('%H:%M:%S', O0OOOOO000OOOO00O()) + O000OO0OO0OOOO0OO + OOOOO0OO0O0000O0O + 'Bitcoin Balance in USD: ' + O000O0O0OOO0OO0O0 + str(getBalance('btc') * O0O0000OO0O000OOO))
                O0O0OO00OO000OO0O = False


def USD_BTC_Price():
    OOO00O0O0OOOOOOOO = 'https://yobit.net/api/3/ticker/btc_usd'
    O000O00O0OO000000 = OOOO00OOOO0OO0O00.get(OOO00O0O0OOOOOOOO, headers={'apisign': O0OO0OOOOOO0OOOO0.new(secret, OOO00O0O0OOOOOOOO.encode(), O00OO0O00000000O0.sha512).hexdigest()})
    OOO00000O0O0OO0OO = O00OO0O00OOO0OO00.loads(O000O00O0OO000000.text)
    return OOO00000O0O0OO0OO['btc_usd']['last']


def main():
    OO0OOO00O000O00OO = getBalance('btc')
    O0O0OO00O00O00O00 = USD_BTC_Price()
    O000O00OOO000O00O = OO0OOO00O000O00OO * O0O0OO00O00O00O00
    print(OO00000O00000OO0O.Fore.RED + '_____________________________________________________________________')
    print(OO00000O00000OO0O.Fore.RED + 'Balance (BTC): ' + str(OO0OOO00O000O00OO))
    print(OO00000O00000OO0O.Fore.RED + 'Balance in USD: ' + str(O000O00OOO000O00O))
    print(OO00000O00000OO0O.Fore.RED + '_____________________________________________________________________')
    if OO000OOOOOO00O000.system() == 'Windows':
        O00O00OO0O0000OO0 = input('[1] Risk Multiplier: ')
        O0OO000OOOOOO00OO = input('[2] % of bitcoin to spend: ')
        O000O0OOO0000OOO0 = input('[3] Profit %: ')
        O0OO0O0OOO0000O00 = input('[4] Coin: ')
    else:
        O00O00OO0O0000OO0 = input(OO00000O00000OO0O.Fore.CYAN + '[1] Risk Multiplier: ')
        O0OO000OOOOOO00OO = input(OO00000O00000OO0O.Fore.CYAN + '[2] % of bitcoin to spend: ')
        O000O0OOO0000OOO0 = input(OO00000O00000OO0O.Fore.CYAN + '[3] Profit %: ')
        O0OO0O0OOO0000O00 = input(OO00000O00000OO0O.Fore.CYAN + '[4] Coin: ')
    if len(O000O0OOO0000OOO0) <= 1:
        O000O0OOO0000OOO0 = '0.0' + O000O0OOO0000OOO0
    else:
        if len(O000O0OOO0000OOO0) <= 2:
            O000O0OOO0000OOO0 = '0.' + O000O0OOO0000OOO0
        else:
            if len(O000O0OOO0000OOO0) <= 3:
                O000O0OOO0000OOO0 = O000O0OOO0000OOO0[0] + '.' + O000O0OOO0000OOO0[1:]
            else:
                O000O0OOO0000OOO0 = O000O0OOO0000OOO0[0:2]
            if len(O0OO000OOOOOO00OO) <= 1:
                O0OO000OOOOOO00OO = '0.0' + O0OO000OOOOOO00OO
            else:
                if len(O0OO000OOOOOO00OO) <= 2:
                    O0OO000OOOOOO00OO = '0.' + O0OO000OOOOOO00OO
                else:
                    if len(O0OO000OOOOOO00OO) <= 3:
                        O0OO000OOOOOO00OO = O0OO000OOOOOO00OO[0] + '.' + O0OO000OOOOOO00OO[1:]
                    else:
                        O0OO000OOOOOO00OO = O0OO000OOOOOO00OO[0:2]
                    O00O0OOOOO0O0OO00 = OO0OOO00O000O00OO * float(O0OO000OOOOOO00OO)
                    Trade(O0OO0O0OOO0000O00.lower(), O000O0OOO0000OOO0, O00O0OOOOO0O0OO00, O00O00OO0O0000OO0)
