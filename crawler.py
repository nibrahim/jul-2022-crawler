import logging

logger = None

def configure_logging(level=logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)


def crawl():
    logger.debug("Crawling starting")
    for i in range(10):
        logger.debug("Fetching URL %s", i)
        print ("https://....")
    logger.debug("Completed crawling")

def main():
    configure_logging()
    logger.debug("Here's a debug message")
    logger.info("Here's an info message!")
    logger.warning("Here's an warning message!")
    logger.critical("Here's an critical message!")
    crawl()


if __name__ == "__main__":
    main()
