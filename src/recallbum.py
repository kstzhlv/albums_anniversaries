#!/usr/bin/env python3

import argparse

from reminder import send_notification
from writer import write_albums_to_txt


def recallbum():
    parser = argparse.ArgumentParser(
        description="Reminds you of anniversaries of your favourite albums."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: parse
    parse_parser = subparsers.add_parser(
        "parse", help="Parse your AOTY page to get favourite albums."
    )
    parse_parser.add_argument("user", type=str, help="AOTY username")
    parse_parser.add_argument("threshold", type=int, help="Minimum rating to include")

    # Subcommand: remind
    remind_parser = subparsers.add_parser(
        "remind", help="Send notifications for album anniversaries."
    )

    args = parser.parse_args()

    if args.command == "parse":
        write_albums_to_txt(args.user, args.threshold)

    elif args.command == "remind":
        send_notification()


if __name__ == "__main__":
    recallbum()
