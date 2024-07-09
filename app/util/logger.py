"""
Module for setting up logging configuration for the application.

This module provides functions to create log directories, configure file and stream handlers,
load logging configurations from a parser module, and initialize the root logger.

Functions:
- _create_logs_directory(): Creates a 'logs' directory if it doesn't exist.
- _setup_file_handler(log_file, file_formatter): Sets up a file handler for logging to a file.
- _setup_stream_handler(stream_formatter): Sets up a stream handler for logging to console.
- _load_logging_config(): Loads logging configurations from a 'config' file using a Parser.
- _configure_root_logger(log_file): Configures the root logger based on loaded configurations.
- initialize_logging(): Initializes logging for the application.
"""

import ast
import logging
import os
from datetime import datetime

from app.util.parser import Parser


def _create_logs_directory():
    """
    Creates a 'logs' directory if it doesn't already exist.

    Returns:
        str: Path to the created or existing 'logs' directory.
    """
    logs_directory = "logs"
    os.makedirs(logs_directory, exist_ok=True)
    return logs_directory


def _setup_file_handler(log_file, file_formatter):
    """
    Sets up a file handler for logging to a specified log file.

    Args:
        log_file (str): Path to the log file.
        file_formatter (logging.Formatter): Formatter for log messages.

    Returns:
        logging.FileHandler: File handler object configured for logging.
    """
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(file_formatter)
    return file_handler


def _setup_stream_handler(stream_formatter):
    """
    Sets up a stream handler for logging to the console.

    Args:
        stream_formatter (logging.Formatter): Formatter for log messages.

    Returns:
        logging.StreamHandler: Stream handler object configured for logging.
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)
    return stream_handler


def _load_logging_config():
    """
    Loads logging configurations from a 'config' file using a Parser.

    Returns:
        dict: Dictionary containing logging configurations.
    """
    config_parser = Parser("config")
    configs = config_parser.get_configs("app_config")
    return configs


def _configure_root_logger(log_file):
    """
    Configures the root logger based on loaded configurations.

    Args:
        log_file (str): Path to the log file.
    """
    logger_obj = logging.getLogger()

    configs = _load_logging_config()
    file_formatter = logging.Formatter(
        configs.get("log_file_message_format"), configs.get("log_time_format")
    )
    file_handler = _setup_file_handler(log_file, file_formatter)
    logger_obj.addHandler(file_handler)

    stream_formatter = logging.Formatter(
        configs["log_stream_message_format"], configs["log_time_format"]
    )
    stream_handler = _setup_stream_handler(stream_formatter)
    logger_obj.addHandler(stream_handler)

    logger_obj.setLevel(os.environ.get("LOG_LEVEL", "CRITICAL"))
    critical_log_libs = ast.literal_eval(configs["critical_log_libs"])

    for lib in critical_log_libs:
        logging.getLogger(lib).setLevel(logging.CRITICAL)


def initialize_logging():
    """
    Initializes logging for the application.

    This function sets up logging by creating a 'logs' directory, configuring log file
    and stream handlers based on loaded configurations, and setting log levels for critical libraries.
    """
    logs_directory = _create_logs_directory()
    log_file = f"{logs_directory}/{datetime.now().strftime('%Y_%m_%d.log')}"
    _configure_root_logger(log_file)
