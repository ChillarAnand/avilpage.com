from data import get_data


def fetch_data():
    try:
        data = get_data()
    except Exception:
        data = []
    return data


def process_data(data):
    try:
        squares = [i ** 2 for i in data]
        return squares
    except Exception:
        return []


def main():
    data = fetch_data()
    result = process_data(data)
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
