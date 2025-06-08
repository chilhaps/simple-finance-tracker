import json, datetime as dt

transaction_history = {}
changes_logged = False

operations_desc = 'Available operations:\n' \
                    'l: log transaction(s)\n' \
                    'b: display current balance\n' \
                    'h: display transaction history\n' \
                    'o: display this list again\n' \
                    'q: quit program'

try:
    with open('transaction_history.json', 'r') as openfile: transaction_history = json.load(openfile)
except:
    pass

print(operations_desc)

while True:
    print()
    usr_input = input('Please choose an operation: ')

    if usr_input == 'l':
        while True:
            usr_input = input('Please enter transaction amount (or r to return): ')

            try:
                usr_input = round(float(usr_input), 2)
                transaction_history[str(dt.datetime.now())] = usr_input
                changes_logged = True
            except:
                if usr_input == 'r':
                    break
                else:
                    print('Invalid input')
    elif usr_input == 'b':
        print()
        print('Current balance: ${}'.format(sum(transaction_history.values())))
    elif usr_input == 'h':
        print()
        count = 0
        balance = 0

        for i in transaction_history.items():
            count += 1
            balance += i[1]
            balance = round(balance, 2) #Correct floating-point error
            transaction_str = ''
            balance_str = ''

            if i[1] < 0:
                transaction_str = '-${}'.format(abs(i[1]))
            else:
                transaction_str = '+${}'.format(abs(i[1]))
            
            if balance < 0:
                balance_str = '-${}'.format(abs(balance))
            else:
                balance_str = '${}'.format(abs(balance))

            print('{}.\t{}: {}\t-> {}'.format(count, i[0], transaction_str, balance_str))
    elif usr_input == 'o':
        print(operations_desc)
    elif usr_input == 'q':
        if changes_logged:
            while True:
                usr_input = input('Would you like to save changes to transaction history? (y/n): ')

                if usr_input == 'y':
                    with open("transaction_history.json", "w") as outfile:
                        json.dump(transaction_history, outfile)
                    break
                elif usr_input == 'n':
                    break
                else:
                    print('Invalid input')

        break
    else:
        print('Invalid input')
