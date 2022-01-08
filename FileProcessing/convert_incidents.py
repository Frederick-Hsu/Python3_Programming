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
import struct
import textwrap

GZIP_MAGIC = b"\x1F\x8B"
MAGIC = b"AIB\x00"
FORMAT_VERSION = b"\x00\x01"

NumbersStruct = struct.Struct("<Idi?")

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

        def export_binary(self, filename, compress=False):

            def pack_string(string):
                data = string.encode("utf8")
                format = "<H{0}s".format(len(data))
                return struct.pack(format, len(data), data)
            
            fh = None
            try:
                if compress:
                    fh = gzip.open(filename, "wb")
                else:
                    fh = open(filename, "wb")
                fh.write(MAGIC)
                fh.write(FORMAT_VERSION)
                for incident in self.values():
                    data = bytearray()
                    data.extend(pack_string(incident.report_id))
                    data.extend(pack_string(incident.airport))
                    data.extend(pack_string(incident.aircraft_id))
                    data.extend(pack_string(incident.aircraft_type))
                    data.extend(pack_string(incident.narrative.strip()))
                    data.extend(NumbersStruct.pack(incident.date.toordinal(),
                                                   incident.pilot_percent_hours_on_type,
                                                   incident.pilot_total_hours,
                                                   incident.midair))
                    fh.write(data)
                return True
            except (EnvironmentError, struct.error) as err:
                print("{0}: pack error: {1}".format(os.path.basename(sys.argv[0]). err))
                return False
            finally:
                if fh is not None:
                    fh.close()
        
        def import_binary(self, filename):

            def unpack_string(fh, eof_is_error = True):
                uint16 = struct.Struct("<H")
                length_data = fh.read(uint16.size)
                if not length_data:
                    if eof_is_error:
                        raise ValueError("missing or corrupt string size")
                    return None
                length = uint16.unpack(length_data)[0]
                if length == 0:
                    return ""
                data = fh.read(length)
                if not data or len(data) != length:
                    raise ValueError("missing or corrupt string")
                format = "<{0}s".format(length)
                return struct.unpack(format, data)[0].decode("utf8")
            
            fh = None
            try:
                fh = open(filename, "rb")
                magic = fh.read(len(GZIP_MAGIC))
                if magic == GZIP_MAGIC:
                    fh.close()
                    fh = gzip.open(filename, "rb")
                else:
                    fh.seek(0)
                magic = fh.read(len(MAGIC))
                if magic != MAGIC:
                    raise ValueError("Invalid .aib file format")
                version = fh.read(len(FORMAT_VERSION))
                if version > FORMAT_VERSION:
                    raise ValueError("Unrecognized .aib file version")
                self.clear()
                while True:
                    report_id = unpack_string(fh, False)
                    if report_id is None:
                        break
                    data = {}
                    data["report_id"] = report_id
                    for name in ("airport", "aircraft_id", "aircraft_type", "narrative"):
                        data[name] = unpack_string(fh)
                    other_data = fh.read(NumbersStruct.size)
                    numbers = NumbersStruct.unpack(other_data)
                    data["date"] = datetime.date.fromordinal(numbers[0])
                    data["pilot_percent_hours_on_type"] = numbers[1]
                    data["pilot_total_hours"] = numbers[2]
                    data["midair"] = numbers[3]
                    incident = Incident(**data)     # 映射拆分语法
                    self[incident.report_id] = incident
                return True
            except (EnvironmentError, pickle.UnpicklingError) as err:
                print("{0}: import binary error: {1}".format(os.path.basename(sys.argv[0]), err))
                return False
            finally:
                if fh is not None:
                    fh.close()
        
        def export_text(self, filename):
            wrapper = textwrap.TextWrapper(initial_indent="    ", subsequent_indent="    ")
            fh = None
            try:
                fh = open(filename, "w", encoding="utf8")
                for incident in self.values():
                    narrative = "\n".join(wrapper.wrap(incident.narrative.strip()))
                    fh.write("[{0.report_id}]\n"
                             "date={0.date!s}\n"
                             "aircraft_id={0.aircraft_id}\n"
                             "aircraft_type={0.aircraft_type}\n"
                             "airport={airport}\n"
                             "pilot_percent_hours_on_type={0.pilot_percent_hours_on_type}\n"
                             "pilot_total_hours={0.pilot_total_hours}\n"
                             "midair={0.midair:d}\n"
                             ".NARRATIVE_START.\n"
                             "{narrative}\n"
                             ".NARRATIVE_END.\n\n".format(incident, 
                                                          airport=incident.airport.strip(),
                                                          narrative=narrative))
                return True
            except (EnvironmentError) as err:
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
