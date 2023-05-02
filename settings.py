import json

settings = {
    'hash_file': 'files/hash_file.txt',
    'last_numbers_file': 'files/last_numbers_file.txt',
    'bins_file': 'files/bins_file.txt',
    'card_number_file': 'files/card_number_file.txt',
    'statistic_file': 'files/statistic_file.csv'
}

if __name__ == "__main__":
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)
