import csv
from csv import DictReader
KEYS = {'index', 'id', 'name', 'synopsis', 'casts', 'creators', 'genres', 'mood_tag', 'image_url', 'netflix_url'}


def write_to_csv(to_csv):
    with open('videos.csv', 'w', encoding='utf8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, KEYS)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


def read_from_csv(csv_file='videos.csv'):
    """
    Read csv into list of dictionaries
    """
    # open file in read mode
    with open(csv_file, 'r', encoding='UTF-8') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        return list_of_dict