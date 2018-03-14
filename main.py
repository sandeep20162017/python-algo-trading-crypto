import colorama as OO0O0O0OOO0OOO0OO, logger as O00OO000OOOO00000, BittrexBot as OO0O0O00O0OO00000, BittrexPumpDetector as O0O00OOO0OOOO000O, YobitPumpDetector as O0O0000O0OOOOOOO0, YobitBot as O00O0OO000OOOOOOO, CryptopiaBot as OOOO0OO000000OO0O, CryptopiaPumpDetector as OOO000O0O0O00O0OO, PoloniexBot as O0OO00OO0OOOO0OO0, PoloniexPumpDetector as OOOOO0O0O0O0OO0OO
if __name__ == '__main__':
    log = O00OO000OOOO00000.getLogger('test')
    log.info('Please choose an exchange, 1 or 2: ')
    log.info('[1]Bittrex')
    log.info('[2]Yobit')
    log.info('[3]Cryptopia')
    log.info('[4]Poloniex')
    print('')
    exchange = input('')
    print('')
    log.info('Please choose an option: ')
    log.info('[1]Auto Trader')
    log.info('[2]Pump and Dump Detector')
    log.info('[3]Auto Trader with Pump and Dump Detector')
    print('')
    option = input('')
if exchange == '1':
    if option == '1':
        OO0O0O00O0OO00000.main()
    if option == '2':
        auto = None
        O0O00OOO0OOOO000O.main(auto)
    if option == '3':
        auto = 1
        O0O00OOO0OOOO000O.main(auto)
else:
    if exchange == '2':
        if option == '1':
            O00O0OO000OOOOOOO.main()
        if option == '2':
            auto = None
            O0O0000O0OOOOOOO0.main(auto)
        if option == '3':
            auto = 1
    else:
        if exchange == '3':
            if option == '1':
                OOOO0OO000000OO0O.main()
            if option == '2':
                auto = None
                OOO000O0O0O00O0OO.main(auto)
            if option == '3':
                auto = 1
                OOO000O0O0O00O0OO.main(auto)
        else:
            if exchange == '4':
                if option == '1':
                    O0OO00OO0OOOO0OO0.main()
                if option == '2':
                    auto = None
                    OOOOO0O0O0O0OO0OO.main(auto)
                if option == '3':
                    auto = 1
                    OOOOO0O0O0O0OO0OO.main(auto)
            else:
                print('Not a valid option!')
