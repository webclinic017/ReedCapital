import requests
import datetime
import sys

def ask(): #Asks whether or not they want to invest
    print('Welcome to Reed Capital. Would you like to start investing today?')
    answer = input()
    if answer.lower() != 'no' and answer.lower() != 'no way' and answer.lower() != 'no thanks':
        yes()
    else:
        no()

def yes(): #If yes, this.
    print('Wonderful. Let\'s get started.')
    print('How much money would you like to invest?')
    global initial_amount
    initial_amount = (input())
    if '$' in str(initial_amount):
        amount2 = initial_amount.translate({ord('$'): None})
        initial_amount = (amount2)
    if int(initial_amount) > 1000:
        invest1000()
    elif int(initial_amount) < 1000:
        invest0()

def no(): #If no, this.
    print('We will be here when you are ready to invest.')
    sys.exit()

def get_price():
    global stock
    stock = str(input())
    now = datetime.datetime.now()
    r = requests.get(
        'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock + '&apikey=CHPSEMPFTVB0EX4U')

    result = r.json()
    dataForAllDays = result['Time Series (Daily)']
    dataForSingleDate = dataForAllDays[(now.strftime("%Y-%m-%d"))]

    global price
    price = (dataForSingleDate['4. close'])

def invest1000():
    print('Which stock do you want to purchase?')
    global initial_amount
    while float(initial_amount) > 100:
        get_price()

        print('One share of ' + stock.upper() + ' is currently valued at $' + price + (
            ' How many shares would you like to purchase?'))

        max_purchase = int(float(initial_amount) // float(price))

        print('You have enough money to purchase up to ' + str(max_purchase) + ' shares')

        amount3 = int(input())
        total_price = format(float(price) * amount3, '.2f')
        #format(foo, '.2f')
        balance = format(round(float(initial_amount) - float(total_price), 2), '.2f')

        print('That comes out to $' + str(total_price) + '. Your balance is now $' + str(balance) + '.')

        if float(balance) > float(100):
            print('What other stocks would you like to purchase?')

        initial_amount = balance
    invest_end()

def invest_end():
    print('We are almost finished allocating your assets. If you would like, we can save the residual funds for next time. How does that sound?')
    answer = input()
    if answer != 'no':
            goodbye()


def invest0(): #If they don't have enough $ to make initial investment
    print('Unfortunately, Reed Capital requires a minimum initial investment of over $1000.')
    sys.exit()

def goodbye():
    print('Thank you for coming in today, we will keep an eye on your investments.')

ask()
