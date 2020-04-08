from libraries import *


class StartScreen:
    def start(self):
        print("Welcome to the Currency Exchange!")
        print("What you want to do?")
        print("""
        ############################
        1. Check the exchange rate
        2. Currency converter
        3. Buy currency
        4. Sell currency
        #############################""")
    def options(self):
        try:
            choice = int(input("\nChoose from menu 1 to 4: "))
            if choice == 1:
                return CheckTheExchangeRate().frame()
            elif choice == 2:
                return CurrencyConverter().cookies_scroll()
            elif choice == 3:
                return CurrencyPurchase().purchase_calculation()
            elif choice == 4:
                return SellCurrency().sell_calculation()
        except:
            print("Invalid number.\nSelect again")
            return StartScreen().options()




class CheckTheExchangeRate():
    def __init__(self):

        moneypl = kursywalut.handlers.MoneyPlHandler()

        data = moneypl.get_moneypl()

        data_dict = dict(data)

        self.EUR_buy = data_dict['FOREX']['EUR'][0]
        self.EUR_sell = data_dict['FOREX']['EUR'][1]
        self.USD_buy = data_dict['FOREX']['USD'][0]
        self.USD_sell = data_dict['FOREX']['USD'][1]
        self.GBP_buy = data_dict['FOREX']['GBP'][0]
        self.GBP_sell = data_dict['FOREX']['GBP'][1]
        self.CHF_buy = data_dict['FOREX']['CHF'][0]
        self.CHF_sell = data_dict['FOREX']['CHF'][1]
        self.date = datetime.date.today()

    def prepare_the_inscription(self):
        inscription_in_the_frame = f'\nExchange rates for: {self.date}\n\nBUY:\nEURO = {self.EUR_buy} PLN\nU.S.DOLLAR = {self.USD_buy} PLN\nBRITISH POUND = {self.GBP_buy} ' \
            f'PLN\nSWISS FRANK = {self.CHF_buy} PLN\n\nSELL:\nEURO = {self.EUR_sell} PLN\nU.S.DOLLAR = {self.USD_sell} PLN\nBRITISH POUND = {self.GBP_sell} PLN\nSWISS FRANK = {self.GBP_sell} PLN'
        return inscription_in_the_frame

    def frame(self):
        inscription = self.prepare_the_inscription()
        up = '\n\n'.ljust(50, '#')
        middle = inscription.center(0)
        down = ''.ljust(50, '#')
        print('\n'.join((up, middle, down)))




class CurrencyConverter:
    def __init__(self):

        chrome_options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://cinkciarz.pl/wymiana-walut/kalkulator-walutowy")

    def cookies_scroll(self):
        cookies = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/button")
        cookies.click()

        converter = self.driver.find_element_by_class_name("page-currency-exchange-currency-converter")
        converter.location_once_scrolled_into_view




class CurrencyPurchase(CheckTheExchangeRate):

    def __init__(self):

        allowed_values = ("EUR", "USD", "GBP", "CHF")

        while True:
            self.currency_selection = input("What currency do you want to buy (EUR/USD/GBP/CHF) : ").upper()
            if self.currency_selection in allowed_values:
                break
            else:
                print("Invalid currency. Try again.")

        while True:
            try:
                self.amount = float(input(f'How many {self.currency_selection} do you want to buy: '))
                break
            except ValueError:
                print("Selected value is not a number. Try again.")


    def purchase_calculation(self):

        statement_of_operations_file = open('statement_of_operations.txt', mode='a', encoding="utf-8")

        if self.currency_selection == "EUR":
            eur_purchase = float(CheckTheExchangeRate().EUR_sell.replace(",","."))
            purchase_worth = f'\nThe amount to be paid for {self.amount} EUR is {round(eur_purchase * self.amount, 2)} PLN'
            print(purchase_worth)

        elif self.currency_selection == "USD":
            usd_purchase = float(CheckTheExchangeRate().USD_sell.replace(",","."))
            purchase_worth = f'\nThe amount to be paid for {self.amount} USD is {round(usd_purchase * self.amount, 2)} PLN'
            print(purchase_worth)

        elif self.currency_selection == "GBP":
            gbp_purchase = float(CheckTheExchangeRate().GBP_sell.replace(",","."))
            purchase_worth = f'\nThe amount to be paid for {self.amount} GBP is {round(gbp_purchase * self.amount, 2)} PLN'
            print(purchase_worth)

        elif self.currency_selection == "CHF":
            chf_purchase = float(CheckTheExchangeRate().CHF_sell.replace(",","."))
            purchase_worth = f'\nThe amount to be paid for {self.amount} CHF is {round(chf_purchase * self.amount, 2)} PLN'
            print(purchase_worth)

        statement_of_operations_file.write(f'{purchase_worth}\n')




class SellCurrency(CheckTheExchangeRate):

    def __init__(self):

        allowed_values = ("EUR", "USD", "GBP", "CHF")

        while True:
            self.currency_selection = input("What currency do you want to sell (EUR/USD/GBP/CHF) : ").upper()
            if self.currency_selection in allowed_values:
                break
            else:
                print("Invalid currency. Try again.")

        while True:
            try:
                self.amount = float(input(f'How many {self.currency_selection} do you want to sell: '))
                break
            except ValueError:
                print("Selected value is not a number. Try again.")


    def sell_calculation(self):

        statement_of_operations_file = open('statement_of_operations.txt', mode='a', encoding="utf-8")

        if self.currency_selection == "EUR":
            eur_sale = float(CheckTheExchangeRate().EUR_buy.replace(",","."))
            sale_worth = f'\nThe withdrawal amount for {self.amount} EUR is {round(eur_sale * self.amount, 2)} PLN'
            print(sale_worth)

        elif self.currency_selection == "USD":
            usd_sale = float(CheckTheExchangeRate().USD_buy.replace(",","."))
            sale_worth = f'\nThe withdrawal amount for {self.amount} USD is {round(usd_sale * self.amount, 2)} PLN'
            print(sale_worth)

        elif self.currency_selection == "GBP":
            gbp_sale = float(CheckTheExchangeRate().GBP_buy.replace(",","."))
            sale_worth = f'\nThe withdrawal amount for {self.amount} GBP is {round(gbp_sale * self.amount, 2)} PLN'
            print(sale_worth)

        elif self.currency_selection == "CHF":
            chf_sale = float(CheckTheExchangeRate().CHF_buy.replace(",","."))
            sale_worth = f'\nThe withdrawal amount for {self.amount} CHF is {round(chf_sale * self.amount, 2)} PLN'
            print(sale_worth)

        statement_of_operations_file.write(f'{sale_worth}\n')




class AnotherOperation:

    def __init__(self):
        self.question = input("\n\nDo you want to go to another operation (Y/N)").upper()

        while True:
            if self.question == "Y":
                return StartScreen().options()
            else:
                print("\n\nThank you for using Currency Exchange.\nWelcome again!")
                break


start_app = StartScreen()
start_app.start()
start_app.options()
next = AnotherOperation()
next

