#!/usr/bin/env python3

import argparse

from src.writer import write_albums_to_txt
from src.reminder import remind


def recallbum():
    parser = argparse.ArgumentParser(description="Reminds you of anniversaries of your favourite albums.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    web_parser = subparsers.add_parser("parse", help="Parse the page of any AOTY user to get their favourite albums. Args: username, threshold (minimum rating to parse).")
    web_parser.add_argument("username", type=str, help="AOTY username")
    web_parser.add_argument("threshold", type=int, help="Minimum rating to parse")

    reminder = subparsers.add_parser("remind", help="Send a notification (or notifications) about today's albums anniversaries.")

    args = parser.parse_args()

    if args.command == "parse":
        write_albums_to_txt(args.username, args.threshold)
    elif args.command == "remind":
        remind()

if __name__ == "__main__":
    recallbum()
