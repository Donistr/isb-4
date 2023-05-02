import json
import logging
import csv

logger = logging.getLogger()
logger.setLevel('INFO')


class FileManager:
    @staticmethod
    def read_settings(file_name: str = 'settings.json') -> dict:
        """
        method reads the settings file
        :param file_name: name of the settings file
        :return: settings
        """
        settings = None
        try:
            with open(file_name) as json_file:
                settings = json.load(json_file)
                logging.info(f'Settings read from {file_name}')
        except OSError as err:
            logging.warning(f'{err} - error reading settings from file {file_name}')
        return settings

    def __init__(self, settings_file_name: str = 'settings.json'):
        settings = self.read_settings(settings_file_name)
        self.__hash_file_path = settings['hash_file']
        self.__last_numbers_file_path = settings['last_numbers_file']
        self.__bins_file_path = settings['bins_file']
        self.__card_number_file_path = settings['card_number_file']
        self.__statistic_file_path = settings['statistic_file']

    @property
    def hash_file_path(self):
        return self.__hash_file_path

    @property
    def last_numbers_file_path(self):
        return self.__last_numbers_file_path

    @property
    def bins_file_path(self):
        return self.__bins_file_path

    @property
    def card_number_file_path(self):
        return self.__card_number_file_path

    @property
    def statistic_file_path(self):
        return self.__statistic_file_path

    @staticmethod
    def read_text(file_path: str) -> str:
        """
        method reads the text file
        :param file_path: path to the file
        :return: text from the file
        """
        try:
            with open(file_path, mode='r') as text_file:
                text = text_file.read()
            logging.info(f'File {file_path} was read')
        except OSError as err:
            logging.warning(f'{err} - error reading file {file_path}')
        return text

    @staticmethod
    def write_text(text: str, file_path: str) -> None:
        """
        method writes the text into the file
        :param text: text
        :param file_path: path to the file
        :return: None
        """
        try:
            with open(file_path, mode='w') as text_file:
                text_file.write(text)
            logging.info(f'Text was written to file {file_path}')
        except OSError as err:
            logging.warning(f'{err} - error writing to file {file_path}')

    def read_bins(self):
        """
        method reads the file containing bins
        :return: bins
        """
        try:
            with open(self.__bins_file_path, mode='r') as text_file:
                text = text_file.readlines()
                bins = list(map(int, text))
            logging.info(f'File {self.__bins_file_path} was read')
        except OSError as err:
            logging.warning(f'{err} - error reading file {self.__bins_file_path}')
        return bins

    def read_statistic(self) -> dict:
        """
        method reads the file containing statistic
        :return: statistic
        """
        try:
            with open(self.__statistic_file_path, mode='r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                lines = list(reader)
        except OSError as err:
            logging.warning(f'{err} - error reading statistic from file {self.__statistic_file_path}')
        statistic = dict()
        for line in lines:
            cores, time = line
            statistic[int(cores)] = float(time)
        logging.info(f'Statistic were read from the file {self.__statistic_file_path}')
        return statistic

    def write_statistic_to_the_end(self, cores: int, time: float) -> None:
        """
        method appends statistic data to the end of the file
        :param cores: number of cores
        :param time: time
        :return: None
        """
        try:
            with open(self.__statistic_file_path, mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([cores, time])
            logging.info(f'Statistic written to file {self.__statistic_file_path}')
        except OSError as err:
            logging.warning(f'{err} - error writing statistic to file {self.__statistic_file_path}')
