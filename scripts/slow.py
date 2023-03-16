import time

import pandas as pd


def process_csv():
    df = pd.read_csv('users.csv')
    time.sleep(2)
    return df.to_dict()


def do_calculation(data):
    time.sleep(0.3)


def main():
    data = process_csv()
    do_calculation(data)
    print('done')


if __name__ == '__main__':
    main()
