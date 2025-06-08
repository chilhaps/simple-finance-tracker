import json, datetime as dt

transaction_history = {}

operations_desc = 'Available operations:\n' \
                    'l (log a transaction)\n' \
                    'b (display current balance)\n' \
                    't (display transaction history)\n' \
                    'h (display this list again)\n' \
                    'q (quit program)\n'

try:
    with open('transaction_history.json', 'r') as openfile: transaction_history = json.load(openfile)
except:
    pass

print(operations_desc)

while True:
    usr_input = input('Please choose an operation: ')
    
    if usr_input == 'l':
        usr_input = input('Please enter transaction amount: ')
        try:
            usr_input = round(float(usr_input), 2)
            transaction_history[str(dt.datetime.now())] = usr_input
        except:
            print('Invalid transaction amount')
    elif usr_input == 'b':
        print('Current balance:', sum(transaction_history.values()))
    elif usr_input == 't':
        print()
        for i in transaction_history.items():
            amount = ''
            if i[1] < 0:
                amount = '-${}'.format(abs(i[1]))
            else:
                amount = '+${}'.format(abs(i[1]))
            print('{}: {}'.format(i[0], amount))
        print()
    elif usr_input == 'h':
        print(operations_desc)
    elif usr_input == 'q':
        with open("transaction_history.json", "w") as outfile:
            json.dump(transaction_history, outfile)
        break
    else:
        print('Invalid input')
