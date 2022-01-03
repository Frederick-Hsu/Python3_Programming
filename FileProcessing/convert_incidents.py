# -*- coding: UTF-8 -*-
#
# File name     : convert_incidents.py
#
#

'''
Usage: convert_incidents.py [options] infile outfile

Read aircraft incident data from infile and writes the data to outfile.
The data formats used depend on the file extensions:

.aix is XML
.ait is text (UTF-8 encoding)
.aib is binary
.aip is pickle
and 
.html is HTML (only allowed for the outfile).

All formats are platform-independent.

Options:
    -h, --help      show this help message and exit
    -f, --force     write the outfile even if it exists [default: OFF]
    -v, --verbose   report results [default: OFF]
    -r READER, --reader=READER
                    reader(XML): 'dom', 'd', 'etree', 'e', 'sax', 's'
                    reader(text): 'manual', 'm', 'regex', 'r'
                    [default: etree for XML, manual for text]
    -w WRITER, --writer=WRITER
                    writer(XML): 'dom', 'd', 'etree', 'e', 'manual', 'm'
                    [default: manual]
    -Z, --conpress  compress .aib/.aip outfile [default: OFF]
    -t, --test      execute doctests and exit (use with -v for verbose)

'''

import datetime

class IncidentError(Exception):
    pass

class Incident:
    def __init__(self,  report_id,
                        date,
                        airport,
                        aircraft_id,
                        aircraft_type,
                        pilot_percent_hours_on_type,
                        pilot_total_hours,
                        midair,
                        narrative = ""):
        assert len(report_id) >= 8 and len(report_id.split()) == 1, "Invalid report ID"
        self.__report_id = report_id
        self.date = date
        self.airport = airport
        self.aircraft_id = aircraft_id
        self.aircraft_type = aircraft_type
        self.pilot_percent_hours_on_type = pilot_percent_hours_on_type
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        assert isinstance(date, datetime.date), "Invalid date"
        self.__date = date
    
    @property
    def airport(self):
        return self.__airport
    
    @airport.setter
    def airport(self, airport):
        assert len(airport) > 0, "Invalid airport name"
        self.__airport = airport
    

class IncidentCollection(dict):
    def values(self):
        for report_id in self.keys():
            yield self[report_id]
    
    def items(self):
        for report_id in self.keys():
            yield (report_id, self[report_id])
    
    def __iter__(self):
        for report_id in sorted(super().keys()):
            yield report_id
    
    keys = __iter__