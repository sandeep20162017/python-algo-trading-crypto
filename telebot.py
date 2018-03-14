
from pytg.sender import Sender
import re, time, colorama, pickle
from pytg import Telegram
import BittrexBot, YobitBot, logger
s = Sender('127.0.0.1', 4458)
tg = Telegram(telegram='tg/bin/telegram-cli', pubkey_file='tg/tg-server.pub')
receiver = tg.receiver
with open('pairs.txt', 'rb') as (fp):
    yobitpairs = pickle.load(fp)
with open('BittrexPairs.txt', 'rb') as (fp):
    bittrexpairs = pickle.load(fp)
result = s.dialog_list()

def initialise():
    tg = Telegram(telegram='tg/bin/telegram-cli', pubkey_file='tg/tg-server.pub')
    receiver = tg.receiver
    sender = tg.sender


count = 0

def yobitTelegram():
    initialise()
    balance = YobitBot.getBalance('btc')
    market = input(colorama.Fore.CYAN + '[1] What Telegram Group: ' + colorama.Style.RESET_ALL)
    risk = input(colorama.Fore.CYAN + '[1] Risk Multiplier: ' + colorama.Style.RESET_ALL)
    amount = input(colorama.Fore.CYAN + '[2] % of bitcoin to spend: ' + colorama.Style.RESET_ALL)
    profit = input(colorama.Fore.CYAN + '[3] Profit %: ' + colorama.Style.RESET_ALL)
    amount, profit = percentageFix(amount, profit)
    amount = balance * float(amount)
    for i in result:
        if 'title' in i and market in i['title']:
            ExID = i['id']

    print('')
    print(colorama.Fore.CYAN + 'waiting' + colorama.Style.RESET_ALL)
    while True:
        messages = s.history(ExID)
        length = len(messages)
        if 'text' in messages[length - 1] and 'https://www.yobit.net/en/trade/' in messages[length - 1]['text']:
            coin = messages[length - 1]['text'].split('trade/')
            m = coin[1].split('/')
            st = re.sub('\\W+', '', m[0])
            YobitBot.Trade(st, profit, amount, risk)
        if 'text' in messages[length - 1]:
            wordList = messages[length - 1]['text'].split()
            newWordList = []
            for word in wordList:
                scrub = re.sub('\\W+', '', word)
                newWordList.append(scrub)

            for pair in yobitpairs:
                p = pair.split('_')
                for word in newWordList:
                    if word.lower() == p[0]:
                        YobitBot.Trade(word.lower(), profit, amount, risk)

        time.sleep(1)


def bittrexTelegram():
    initialise()
    balance = BittrexBot.getBalance('btc')
    market = input(colorama.Fore.CYAN + '[1] What Group: ' + colorama.Style.RESET_ALL)
    risk = input(colorama.Fore.CYAN + '[1] Risk Multiplier: ' + colorama.Style.RESET_ALL)
    amount = input(colorama.Fore.CYAN + '[2] % of bitcoin to spend: ' + colorama.Style.RESET_ALL)
    profit = input(colorama.Fore.CYAN + '[3] Profit %: ' + colorama.Style.RESET_ALL)
    amount, profit = percentageFix(amount, profit)
    amount = balance * float(amount)
    for i in result:
        if 'title' in i and market in i['title']:
            ExID = i['id']

    log = logger.getLogger('test')
    log.critical('waiting')
    while True:
        print(ExID)
        s = Sender('127.0.0.1', 4458)
        messages = s.history(ExID)
        length = len(messages)
        if 'text' in messages[length - 1] and 'https://bittrex.com/Market/Index?MarketName=BTC' in messages[length - 1]['text']:
            coin = messages[length - 1]['text'].split('BTC-')
            st = re.sub('\\W+', '', coin[1])
            BittrexBot.Trade(st, profit, amount, risk)
        if 'text' in messages[length - 1]:
            wordList = messages[length - 1]['text'].split()
            newWordList = []
            for word in wordList:
                scrub = re.sub('\\W+', '', word)
                newWordList.append(scrub)

            for pair in bittrexpairs:
                p = pair.split('-')
                for word in newWordList:
                    if word == p[1]:
                        BittrexBot.Trade(word, profit, amount, risk)

        time.sleep(1)


def percentageFix(pricepercent, volumepercent):
    if len(pricepercent) <= 1:
        pricepercent = '0.0' + pricepercent
    else:
        if len(pricepercent) <= 2:
            pricepercent = '0.' + pricepercent
        else:
            if len(pricepercent) <= 3:
                pricepercent = pricepercent[0] + '.' + pricepercent[1:]
            else:
                pricepercent = pricepercent[0:2]
            if len(volumepercent) <= 1:
                volumepercent = '0.0' + volumepercent
            else:
                if len(volumepercent) <= 2:
                    volumepercent = '0.' + volumepercent
                else:
                    if len(volumepercent) <= 3:
                        volumepercent = volumepercent[0] + '.' + volumepercent[1:]
                    else:
                        volumepercent = volumepercent[0:2]
    return (
     pricepercent, volumepercent)
