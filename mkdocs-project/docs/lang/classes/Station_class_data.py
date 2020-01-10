import logging


class Station(object):
    """
    Station at which data are collected.
    """

    # Example of class data
    default_elevation = 0.0

    def __init__(self, station_id="", latitude=None, longitude=None):
        """
        Create a new Station instance.
        """

        # Station identifier
        self.station_id = station_id

        # Station coordinates
        self.latitude = latitude
        self.longitude = longitude
