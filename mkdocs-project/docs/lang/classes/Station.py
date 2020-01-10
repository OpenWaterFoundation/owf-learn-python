import logging


class Station(object):
    """
    Station at which data are collected.
    """

    def __init__(self, station_id="", latitude=None, longitude=None):
        """
        Create a new Station instance.
        """

        # Station identifier
        self.station_id = station_id

        # Station coordinates
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        """
        Return a string representation of the station.
        """
        return str(self.station_id) + "," + str(self.longitude) + "," + str(self.latitude)

    def check_data(self):
        """
        Check the station data validity.
        """ 

        # Can use a logger or just print a message
        logger = logging.getLogger(__name__)

        error_count = 0
        if (self.station_id == None) or (self.station_id == ""):
            error_count += 1
            message = "station_id is not defined"
            print(message)
            logger.warning(message)
        return error_count
