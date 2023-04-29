from hashlib import sha1
import multiprocessing as mp
from typing import Optional


def is_card_number_right(right_hash: str, card_number: str) -> bool:
    hash = sha1(card_number.encode()).hexdigest()
    if hash == right_hash:
        return True
    return False


def brute_card_number(right_hash: str, last_numbers: str, bins: list, cores: int = mp.cpu_count()) -> Optional[str]:
    args = list()
    for i in range(1000000):
        for bin in bins:
            args.append((right_hash, f'{bin}{i}{last_numbers}'))
    with mp.Pool(processes=cores) as p:
        for index, result in enumerate(p.starmap(is_card_number_right, args)):
            if result:
                p.terminate()
                return args[index][-1]
    return None
