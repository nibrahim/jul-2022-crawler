import argparse
import logging

import requests
from bs4 import BeautifulSoup

import db
import web

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    parser.add_argument("--db", help="Name of database to use", action="store", default="lyrics")
    subcommands = parser.add_subparsers(help="Commands", dest="command")
    subcommands.add_parser("initdb", help="Initialise the database")
    subcommands.add_parser("crawl", help="Perform a crawl")
    subcommands.add_parser("web", help="Start web server")
    args = parser.parse_args()
    if args.command == None:
        parser.error("Subcommand is required")
    return args

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
    logger.debug("Got response %s", resp)
    soup = BeautifulSoup(resp.content)
    tracklist = soup.find("table", attrs={ "class": "tracklist"})
    artist_links = tracklist.find_all("a")
    for link in artist_links:
        img = link.find("img")
        if not img:
            logger.info(link.text)
            db.add_artist(link.text)
    logger.debug("Completed crawling")

def create_tables(db_name):
    conn = db.get_connection(db_name)
    with conn.cursor() as cursor:
        with open("init.sql") as f:
            sql = f.read()
            cursor.execute(sql)
    conn.commit()
    conn.close()
    

def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    if args.command == "crawl":
        logger.info("Crawling")
        get_artists("https://www.songlyrics.com/top-artists-lyrics.html")

    elif args.command == "initdb":
        logger.info("Initialising database")
        create_tables(args.db)
    elif args.command == "web":
        logger.info("Starting webserver")
        web.app.run()
    else:
        logger.warning("%s not implemented", args.command)

if __name__ == "__main__":
    main()
