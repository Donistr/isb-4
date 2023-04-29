from brute import brute_card_number
from file_manager import FileManager
from vizualization import visualize_statistic
from lunh import luhn_algorithm
from time import time
import argparse
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str, help='Use custom settings file (Specify file path)')
    parser.add_argument('-stt', '--statistic', help='Save statistics to file', action='store_true')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-brt', '--brute', type=int,
                       help='Brute card number from given hash (Specify number of processes)')
    group.add_argument('-lun', '--lunh', help='Check received card number with Luhn algorithm', action='store_true')
    group.add_argument('-vis', '--visualization', help='Visualize data from statistics file', action='store_true')
    args = parser.parse_args()
    if args.settings:
        file_manager = FileManager(args.settings)
    else:
        file_manager = FileManager()
    if args.brute:
        right_hash = file_manager.read_text(file_manager.hash_file_path)
        last_numbers = file_manager.read_text(file_manager.last_numbers_file_path)
        bins = file_manager.read_bins()
        if args.statistic:
            time_1 = time()
            card_number = brute_card_number(right_hash, last_numbers, bins, args.brute)
            time_2 = time()
            file_manager.write_statistic_to_the_end(args.brute, time_2 - time_1)
        else:
            card_number = brute_card_number(right_hash, last_numbers, bins, args.brute)
        if card_number:
            file_manager.write_text(card_number, file_manager.card_number_file_path)
            logging.info(f'The card number matches the given hash was found: {card_number}')
        else:
            logging.info(f'The card number matches the given hash was not found')
    elif args.lunh:
        card_number = file_manager.read_text(file_manager.card_number_file_path)
        if luhn_algorithm(card_number):
            logging.info(f'The card number {card_number} is correct')
        else:
            logging.info(f'The card number {card_number} is not correct')
    elif args.visualization:
        statistic = file_manager.read_statistic()
        visualize_statistic(statistic)
