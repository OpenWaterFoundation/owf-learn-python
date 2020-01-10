import logging


class Station(object):
    """
    Station at which data are collected.
    """

    # Example of class method

    def __init__(self, station_id="", latitude=None, longitude=None):
        """
        Create a new Station instance.
        """

        # Station identifier
        self.station_id = station_id

        # Station coordinates
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def read_stations(cls, filename)
        """
        Read a list of stations from the file.
        """
        stations = []
        # Here would write code to read a file,
        # declare instances of Station, add to a list, and return the list
        return stations

