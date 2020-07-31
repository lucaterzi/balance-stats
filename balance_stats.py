import csv
import datetime
import json
import os
import sys

from io import StringIO

def generate_date_interval(start_date, end_date):
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    date_interval = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days + 1)]
    days = [d.strftime('%Y-%m-%d') for d in date_interval]
    return days

def read_transactions_from_csv(csvfile):
    with open(csvfile, 'r') as f:
        content = f.read()
    buffer = StringIO(content)
    reader = csv.reader(buffer, delimiter=',')
    transactions = {row[0]:row[1] for row in reader}
    return transactions

def get_daily_balances(start_date, end_date, transactions):
    days = generate_date_interval(start_date, end_date)
    balances = []
    last_transaction = '0'
    for d in days:
        if d in transactions:
            balances.append({'date': d, 'balance': transactions[d]})
            last_transaction = transactions[d]
        else:
            balances.append({'date': d, 'balance': last_transaction})
    return balances

def get_average_balance(balances):
    balance_list = list(map(lambda x: float(x['balance']), balances))
    return sum(balance_list) / len(balance_list)

def get_max_balance(balances):
    balance_list = list(map(lambda x: float(x['balance']), balances))
    return max(balance_list)

def get_min_balance(balances):
    balance_list = list(map(lambda x: float(x['balance']), balances))
    return min(balance_list)

def get_balance_stats(start_date, end_date, transactions_csv):
    transactions = read_transactions_from_csv(transactions_csv)
    daily_balances = get_daily_balances(start_date, end_date, transactions)
    average_balance = get_average_balance(daily_balances)
    max_balance = get_max_balance(daily_balances)
    min_balance = get_min_balance(daily_balances)
    balance_stats = {
        'start_date': start_date,
        'end_date': end_date,
        'average_balance': '{:.2f}'.format(average_balance),
        'maximum_balance': '{:.2f}'.format(max_balance),
        'minimum_balance': '{:.2f}'.format(min_balance)
    }
    return balance_stats

def print_help():
    program = sys.argv[0]
    program_name = os.path.basename(program)
    print(f'Usage: python {program_name} [START_DATE] [END_DATE] [TRANSACTIONS_CSV]\n')
    print('[START_DATE]: first day of the date range for which to calculate the balance statistics, in YYYY-MM-DD format')
    print('[END_DATE]: last day of the date range for which to calculate the balance statistics, in YYYY-MM-DD format')
    print('[TRANSACTIONS_CSV]: path to the CSV files that contains the list of financial transactions to parse')
    print('')
    print(f'Example: python {program_name} 2019-01-01 2019-12-31 ./examples/examples_transactions.csv')

def execute():
    if len(sys.argv) < 4:
        print_help()
        return 1
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    transactions_csv = sys.argv[3]
    balance_stats = get_balance_stats(start_date, end_date, transactions_csv)
    print(json.dumps(balance_stats))
    return 0

def main():
    sys.exit(execute())

if __name__ == '__main__':
    main()