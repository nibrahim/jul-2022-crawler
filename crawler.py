import argparse
import logging

import requests
from bs4 import BeautifulSoup

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    
    subcommands = parser.add_subparsers(help="Commands")
    subcommands.add_parser("initdb", help="Initialise the database")
    subcommands.add_parser("crawl", help="Perform a crawl")
    subcommands.add_parser("web", help="Start web server")
    subcommand
    return parser.parse_args()

def configure_logging(level=logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)


def get_artists(base):
    logger.debug("Crawling starting")
    resp = requests.get(base)
    soup = BeautifulSoup(resp.content)
    tracklist = soup.find("table", attrs={ "class": "tracklist"})
    artist_links = tracklist.find_all("a")
    for link in artist_links:
        img = link.find("img")
        if not img:
            logger.info(link.text)
    logger.debug("Completed crawling")

def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    get_artists("https://www.songlyrics.com/top-artists-lyrics.html")


if __name__ == "__main__":
    main()
