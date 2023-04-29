from hashlib import sha1
import multiprocessing as mp
from typing import Optional
from tqdm import tqdm


def is_card_number_right(right_hash: str, card_number: str) -> bool:
    """
    function checks if the card number matches the given hash
    :param right_hash: given hash
    :param card_number: card number to check
    :return: True - if the card number matches the given hash, False - otherwise
    """
    hash = sha1(card_number.encode()).hexdigest()
    if hash == right_hash:
        return True
    return False


def brute_card_number(right_hash: str, last_numbers: str, bins: list, cores: int = mp.cpu_count()) -> Optional[str]:
    """
    function tries to find a card number that matches the given hash
    :param right_hash: given hash
    :param last_numbers: last 4 digits of the card number
    :param bins: bins
    :param cores: number of cores
    :return: card number - if found, None - if not found
    """
    args = list()
    for i in range(1000000):
        for bin in bins:
            args.append((right_hash, f'{bin}{i}{last_numbers}'))
    with mp.Pool(processes=cores) as p:
        for index, result in enumerate(p.starmap(is_card_number_right, tqdm(args, ncols=120))):
            if result:
                p.terminate()
                return args[index][-1]
    return None
