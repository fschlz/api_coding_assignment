import logging


def setup_logging(name: str, log_level: str = "DEBUG") -> logging.Logger:

    LOG_FORMAT = "%(asctime)s [%(levelname)s] - [%(filename)s -> %(funcName)s() -> %(lineno)s] : %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    stream = logging.StreamHandler()
    stream_format = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    stream.setFormatter(stream_format)

    logger.addHandler(stream)

    file = logging.FileHandler("app.log")
    file_format = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    file.setFormatter(file_format)

    logger.addHandler(file)

    return logger
