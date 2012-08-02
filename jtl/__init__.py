# Copyright (C) 2012 Victor Klepikovskiy
#
# This file is part of python-jtl.
#
# python-jtl is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# python-jtl is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-jtl. If not, see <http://www.gnu.org/licenses/>.


from collections import namedtuple
from xml.etree import cElementTree as etree
import csv
from datetime import timedelta, datetime


class AssertionResult(namedtuple('AssertionResult', 'er, fa, fm, na')):
    """The class that stores assertion result of the sample. It has the
    following fields:
    er -- error
    fa -- failure
    fm -- failure message
    na -- name

    """
    pass


class Sample(namedtuple('Sample', 'ar, by, de, dt, ec, hn, it, lb, lt, na, '
                        'ng, rc, rm, su, sc, ti, tn, ts')):
    """The class that stores one sample from the results data in named
    tuple. It has the following fields:
    ar -- assertion results
    by -- bytes received
    de -- data encoding
    dt -- data type
    ec -- error count
    hn -- hostname where the sample was generated
    it -- idle time
    lb -- label
    lt -- latency time
    na -- number of active threads for all thread groups
    ng -- number of active threads in this group
    rc -- response code
    rm -- response message
    sc -- sample count
    su -- success flag
    ti -- elapsed time
    tn -- thread name
    ts -- timestamp

    """
    pass


class BaseParser(object):
    """The base class for JTL parsers.

    """
    def http_samples(self):
        """Generator method which yields HTTP samples from the results.
        Must be redefined in subclasses.

        """
        raise NotImplementedError


class XMLParser(BaseParser):
    """The class that implements JTL (XML) file parsing functionality.

    """
    def __init__(self, source, **kwargs):
        """Initialize the class.

        Arguments:
        source -- filename or file object containing the results data

        """
        self.context = etree.iterparse(source, events=('start', 'end'))
        self.context = iter(self.context)
        event, self.root = self.context.next()
        self.version = self.root.get('version')

    def http_samples(self):
        """Generator method which yields HTTP samples from the results.

        """
        for event, elem in self.context:
            if event == 'end' and elem.tag == 'httpSample':
                assertion_results = []
                for as_res in elem.findall('assertionResult'):
                    assertion_results.append(AssertionResult(
                            er=bool(as_res.findtext('error', '') == 'true'),
                            fa=bool(as_res.findtext('failure', '') == 'true'),
                            fm=as_res.findtext('failureMessage', ''),
                            na=as_res.findtext('name', ''),
                            ))
                yield Sample(
                        ar=tuple(assertion_results),
                        by=int(elem.get('by', 0)),
                        de=elem.get('de', ''),
                        dt=elem.get('dt', ''),
                        ec=int(elem.get('ec', 0)),
                        hn=elem.get('hn', ''),
                        it=timedelta(milliseconds=int(elem.get('it', 0))),
                        lb=elem.get('lb', ''),
                        lt=timedelta(milliseconds=int(elem.get('lt', 0))),
                        na=int(elem.get('na', 0)),
                        ng=int(elem.get('ng', 0)),
                        rc=elem.get('rc', ''),
                        rm=elem.get('rm', ''),
                        sc=int(elem.get('sc', 0)),
                        su=bool(elem.get('s') == 'true'),
                        ti=timedelta(milliseconds=int(elem.get('t', 0))),
                        tn=elem.get('tn', ''),
                        ts=datetime.utcfromtimestamp(
                                int(elem.get('ts', 0)) / 1000.0),
                        )
            self.root.clear()


class CSVParser(BaseParser):
    """The class that implements JTL (CSV) file parsing functionality.

    """
    def __init__(self, source, **kwargs):
        """Initialize the class.

        Arguments:
        source -- name of the file containing the results data

        Keyword arguments:
        delimiter -- custom delimiter character (CSV only)

        """
        self.source = source
        self.delimiter = kwargs.get('delimiter', ',')

    def http_samples(self):
        """Generator method which yeilds HTTP samples from the results.

        """
        with open(self.source, 'rb') as fp:
            reader = csv.DictReader(fp, delimiter=self.delimiter)
            for row in reader:
                if row.get('failureMessage'):
                    assertion_results = [AssertionResult(
                            er=False,
                            fa=True,
                            fm=row['failureMessage'],
                            na=''
                            )]
                else:
                    assertion_results = []
                yield Sample(
                        ar=tuple(assertion_results),
                        by=int(row.get('bytes', 0)),
                        de='',
                        dt=row.get('dataType', ''),
                        ec=0,
                        hn='',
                        it=timedelta(0),
                        lb=row.get('label', ''),
                        lt=timedelta(milliseconds=int(row.get('Latency', 0))),
                        na=0,
                        ng=0,
                        rc=row.get('responseCode', ''),
                        rm=row.get('responseMessage', ''),
                        sc=0,
                        su=bool(row.get('success') == 'true'),
                        ti=timedelta(milliseconds=int(row.get('elapsed', 0))),
                        tn=row.get('threadName', ''),
                        ts=datetime.utcfromtimestamp(
                                int(row.get('timeStamp', 0)) / 1000.0))


def create_parser(source, **kwargs):
    """The function that determines the format of the results file and
    creates and returns the appropriate parser.

    Arguments:
    source -- name of the file containing the results data

    Keyword arguments:
    delimiter -- custom delimiter character (CSV only)

    """
    with open(source) as fp:
        if fp.readline().startswith('<?xml'):
            return XMLParser(source, **kwargs)
        else:
            return CSVParser(source, **kwargs)

