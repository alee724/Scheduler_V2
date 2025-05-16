"""
Alvin Lee

This module is responsible for keeping in track of the price, time span, name, and other attributes
of a service
"""

from ctime import *


class Service:
    def __init__(self, name, price, time_span, abb="", sort="None"):
        """
        Creates a class for services containing all the necessary information for the scheduler

        @parameter name: string
        @parameter price: non-negative integer
        @parameter time_span: a CTime object
        @parameter abb: optional string argument that represents the abbreviation for the name
        """
        assert (
            isinstance(name, str)
            and isinstance(price, int)
            and isinstance(time_span, CTime)
            and isinstance(abb, str)
        )
        assert price >= 0
        assert len(abb) <= 8
        self.name = name
        self.price = price
        self.time = time_span
        self.abbrev = abb
        self.sorted = sort

    def __eq__(self, o):
        """
        Two services are equal if and only if they have the same name
        """
        assert isinstance(o, Service)
        if self.name == o.name:
            return True
        return False

    def toJSON(self):
        json = {
            "name": self.name,
            "price": self.price,
            "time": self.time.toJSON(),
            "abbreviation": self.abbrev,
            "sorted": self.sorted,
        }
        return json

    def fromJSON(self):
        if isinstance(self, str):
            import json

            self = json.loads(self)
        time = CTime.fromJSON(self["time"])

        return Service(
            self["name"], self["price"], time, self["abbreviation"], self["sorted"]
        )

    def toString(self):
        """
        Converts a Service object to a readable string for display
        """
        return f"{self.name}, ${self.price}, {self.time.toString()}, {self.abbrev}, {self.sorted}"

    # ========== Get and Set methods ==========
    def getSort(self): 
        """
        Get the identification for where the service was sorted 
        """
        return self.sorted

    def getName(self):
        """
        Returns the name
        """
        return self.name

    def getPrice(self):
        """
        Returns the price
        """
        return self.price

    def getTime(self):
        """
        Returns the time
        """
        return self.time

    def getAbbrev(self):
        """
        Returns the abbreviation
        """
        return self.abbrev

    def setName(self, new):
        """
        Sets the name as [new]
        """
        assert isinstance(new, str)
        self.name = new

    def setPrice(self, new):
        """
        Sets the price to [new]
        """
        assert isinstance(new, int) and new >= 0
        self.price = new

    def setTime(self, hour, minute):
        """
        Sets the time to a new [hour] and [minute]
        """
        self.time.setTime(hour, minute)

    def setAbbrev(self, new):
        """
        Sets the abbrevitaion to new
        """
        self.abbrev = new
