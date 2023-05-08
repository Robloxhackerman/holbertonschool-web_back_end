#!/usr/bin/env python3
"""
aaaaaa
"""
import re
from os import getenv
from typing import List
import logging

import mysql.connector

PII_FIELDS = ('name', 'email', 'ssn', 'password', 'phone')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """

    :param fields:
    :param redaction:
    :param message:
    :param separator:
    :return:
    """
    pepe = message
    for field in fields:
        pepe = re.sub(field + "=.*?" + separator,
                      field + "=" + redaction + separator, pepe)
    return pepe


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """

        :param record:
        :return:
        """
        return filter_datum(self.fields, self.REDACTION, super(
            RedactingFormatter, self).format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """

    :return:
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stremManoteador = logging.StreamHandler()
    stremManoteador.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stremManoteador)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """

    :return:
    """
    connection_db = mysql.connector.connection.MySQLConnection(
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME'))

    return connection_db
