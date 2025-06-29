import argparse

from writer import write_albums_to_txt


def alban():
    parser = argparse.ArgumentParser(description="Remind you of anniversaries of your favourite albums.")
    parser.add_argument("-p", "--parse", help="Parse your AOTY page to get your favourite albums and save them to a txt.")
    parser.add_argument("-s", "--start", help="Remind you of your favourite albums' anniversaries.")