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
import pickle
import gzip
import os
import sys

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
        assert len(report_id) >= 8 and len(report_id.split()) == 1, "Invalid report ID."
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

    @property
    def aircraft_id(self):
        return self.__aircraft_id
    
    @aircraft_id.setter
    def aircraft_id(self, aircraft_id):
        assert len(aircraft_id) > 0, "Invalid aircraft_id number"
        self.__aircraft_id = aircraft_id
    
    @property
    def aircraft_type(self):
        return self.__aircraft_type
    
    @aircraft_type.setter
    def aircraft_type(self, aircraft_type):
        assert len(aircraft_type) > 0, "Invalid aircraft_type name"
        self.__aircraft_type = aircraft_type
    
    @property
    def pilot_percent_hours_on_type(self):
        return self.__pilot_percent_hours_on_type
    
    @pilot_percent_hours_on_type.setter
    def pilot_percent_hours_on_type(self, pilot_percent_hours_on_type):
        assert pilot_percent_hours_on_type > 0.0 and pilot_percent_hours_on_type < 100.0, \
            "Invalid pilot_percent_hours_on_type"
        self.__pilot_percent_hours_on_type = pilot_percent_hours_on_type
    
    @property
    def pilot_total_hours(self):
        return self.__pilot_total_hours
    
    @pilot_total_hours.setter
    def pilot_total_hours(self, pilot_total_hours):
        assert pilot_total_hours > 0, "Invalid pilot_total_hours integral number"
        self.__pilot_total_hours = pilot_total_hours
    
    @property
    def midair(self):
        return self.__midair
    
    @midair.setter
    def midair(self, midair):
        assert midair == True or midair == False, "Invalid midair boolean type"
        self.__midair = midair
    
    @property
    def narrative(self):
        return self.__narrative
    
    @narrative.setter
    def narrative(self, narrative):
        assert len(narrative) > 0 and narrative.contains("\n"), "Invalid narrative multiline string type"
        self.__narrative = narrative
    
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

        GZIP_MAGIC = b"\x1F\x8B"

        def export_pickle(self, filename, compress = False):
            fh = None
            try:
                if compress:
                    fh = gzip.open(filename, "wb")
                else:
                    fh = open(filename, "wb")
                pickle.dump(self, fh, pickle.HIGHEST_PROTOCOL)
                return True
            except (EnvironmentError, pickle.PicklingError) as err:
                print("{0}: export error: {1}".format(os.path.basename(sys.argv[0]), err))
                return False
            finally:
                if fh is not None:
                    fh.close()   

        def import_pickle(self, filename):
            fh = None
            try:
                fh = open(filename, "wb")
                magic = fh.read(len(GZIP_MAGIC))
                if magic == GZIP_MAGIC:
                    fh.close()
                    fh = gzip.open(filename, "wb")
                else:
                    fh.seek(0)
                self.clear()
                self.update(pickle.load(fh))
                return True
            except (EnvironmentError, pickle.UnpicklingError) as err:
                print("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
                return False
            finally:
                if fh is not None:
                    fh.close()


if __name__ == "__main__":
    ba = bytearray()
    ba.append(0x68)
    ba.append(0x10)
    print(ba)

    ba.capitalize()
    print(ba)
