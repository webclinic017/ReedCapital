import requests
import datetime

print('Welcome to Reed Capital. Would you like to start investing today?')
answer = input()

if answer.lower() != 'no' and answer.lower() != 'no way' and answer.lower() != 'no thanks':
    print('Wonderful. Let\'s get started.')
    print('How much money would you like to invest?')
    initial_amount = input()
    if '$' in initial_amount:
        amount2 = initial_amount.translate({ord('$'): None})
        initial_amount = (amount2)

    # amount = int(input())
    while int(initial_amount) < 1000:
            print('Sorry, but we require a minimum investment of $1000.')
            print('We will be here when you are ready to invest.')
            break
    else:

        print('Wonderful! Let\'s get started!')
        print('Which stonk do you want to purchase?')

        while int(initial_amount) > 100:

            stonk = str(input())
            now = datetime.datetime.now()
            r = requests.get(
                'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stonk + '&apikey=CHPSEMPFTVB0EX4U')

            result = r.json()
            dataForAllDays = result['Time Series (Daily)']
            dataForSingleDate = dataForAllDays[(now.strftime("%Y-%m-%d"))]

            price = (dataForSingleDate['4. close'])

            print('One share of ' + stonk.upper() + ' is currently valued at $' + price + (
                ' How many shares would you like to purchase?'))

            max_purchase = int(int(initial_amount)//float(price))

            print ('You have enough money to purchase up to ' + str(max_purchase) + ' shares')

            amount3 = int(input())
            total_price = float(price)*amount3

            balance = int(initial_amount) - float(total_price)

            print('That comes out to $' + str(total_price) + '. Your balance is now $' + str(balance) +'.')
            print('What other stonks would you like to purchase?')

            initial_amount = balance


else:
            print('We will be here when you are ready to invest.')


print('END')
