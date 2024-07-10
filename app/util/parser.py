"""
Module: ConfigParser Module

This module provides a Parser class for handling configuration files using configparser.
"""

import configparser


class ConfigParserError(Exception):
    """
    Custom exception raised for errors related to configuration parsing.
    """


class Parser:  # pylint: disable=too-few-public-methods
    """
    ConfigParser class for reading and accessing configuration settings from an INI file.

    Attributes:
        _parse (configparser.ConfigParser): Internal configparser instance.
        _filename (str): Name of the configuration file.
        _filepath (str): Full path to the configuration file.

    Methods:
        __init__(self, _file='config.ini'):
            Initializes the Parser instance with the given configuration file.
            Raises ConfigParserError if the file is not found.

        get_configs(self, key):
            Retrieves configuration settings for a specific section as a dictionary.
            Raises ConfigParserError if the section key is not found.
    """

    def __init__(self, _file="config.ini"):
        """
        Initialize the Parser instance with a configuration file.

        Args:
            _file (str): Name of the configuration file (default is 'config.ini').

        Raises:
            ConfigParserError: If the file is not found in the src/config directory.
        """
        self._parse = configparser.ConfigParser()
        self._parse._interpolation = configparser.ExtendedInterpolation()
        self._parse.optionxform = str
        self._filename = _file
        filepath = f"app/config/{_file}"
        self._filepath = filepath if _file.endswith(".ini") else f"{filepath}.ini"
        parse_response = self._parse.read(self._filepath)
        if not parse_response:
            error = f"{self._filename} is not present in src/config."
            raise ConfigParserError(error)

    def get_configs(self, key):
        """
        Retrieve configuration settings for a specific section.

        Args:
            key (str): Section name in the configuration file.

        Returns:
            dict: Dictionary of configuration settings for the specified section.

        Raises:
            ConfigParserError: If the section key is not found in the configuration file.
        """
        if key not in self._parse.sections():
            error = f"{key} is not present in {self._filename}."
            raise ConfigParserError(error)

        return dict(self._parse[key])
