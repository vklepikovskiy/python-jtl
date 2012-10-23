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
from datetime import timedelta, datetime
from xml.etree import cElementTree as etree
import csv


class AssertionResult(namedtuple('AssertionResult', (
            'error', 'failure', 'failure_message', 'name',
            ))):
    """The class that stores the single assertion result. It contains
    the following fields:

    error           -- error flag
    failure         -- failure flag
    failure_message -- failure message
    name            -- assertion name

    """
    pass


class Sample(namedtuple('Sample', (
            'all_threads', 'assertion_results', 'bytes_received', 'cookies',
            'data_encoding', 'data_type', 'elapsed_time', 'error_count',
            'group_threads', 'hostname', 'idle_time', 'label', 'latency_time',
            'method', 'query_string', 'request_headers', 'response_code',
            'response_data', 'response_filename', 'response_headers',
            'response_message', 'sample_count', 'success', 'thread_name',
            'timestamp', 'url',
            ))):
    """The class that stores the single sample from the results data.
    It contains the following fields:

    all_threads       -- number of active threads for all thread groups
    assertion_results -- assertion results
    bytes_received    -- bytes received
    cookies           -- cookies
    data_encoding     -- response data encoding
    data_type         -- response data type
    elapsed_time      -- elapsed time
    error_count       -- error count
    group_threads     -- number of active threads in this group
    hostname          -- hostname where the sample was generated
    idle_time         -- idle time
    label             -- label of the sample
    latency_time      -- latency time
    method            -- HTTP method
    query_string      -- HTTP query string
    request_headers   -- request headers
    response_code     -- response code
    response_data     -- response data
    response_filename -- response filename
    response_headers  -- response headers
    response_message  -- response message
    sample_count      -- sample count
    success           -- success flag
    thread_name       -- thread name
    timestamp         -- timestamp
    url               -- url

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
                            error=bool(as_res.findtext('error', '') == 'true'),
                            failure=bool(
                                as_res.findtext('failure', '') == 'true'),
                            failure_message=as_res.findtext(
                                'failureMessage', ''),
                            name=as_res.findtext('name', ''),
                            ))
                response_status_line, response_headers = elem.findtext(
                        'responseHeader', '\n').split('\n', 1)
                yield Sample(
                        all_threads=int(elem.get('na', 0)),
                        assertion_results=tuple(assertion_results),
                        bytes_received=int(elem.get('by', 0)),
                        cookies=dict([c.split('=', 1)
                            for c in elem.findtext('cookies', '').split('; ')
                            if c]),
                        data_encoding=elem.get('de', ''),
                        data_type=elem.get('dt', ''),
                        elapsed_time=timedelta(
                            milliseconds=int(elem.get('t', 0))),
                        error_count=int(elem.get('ec', 0)),
                        group_threads=int(elem.get('ng', 0)),
                        hostname=elem.get('hn', ''),
                        idle_time=timedelta(
                            milliseconds=int(elem.get('it', 0))),
                        label=elem.get('lb', ''),
                        latency_time=timedelta(
                            milliseconds=int(elem.get('lt', 0))),
                        method=elem.findtext('method', ''),
                        query_string=elem.findtext('queryString', ''),
                        request_headers=dict([h.split(': ', 1)
                            for h in elem.findtext(
                                'requestHeader', '').splitlines()
                            if h]),
                        response_code=elem.get('rc', ''),
                        response_data=elem.findtext('responseData', ''),
                        response_filename=elem.findtext('responseFile', ''),
                        response_headers={'status_line': response_status_line,
                            'headers': dict([h.split(': ', 1)
                                for h in response_headers.splitlines() if h])},
                        response_message=elem.get('rm', ''),
                        sample_count=int(elem.get('sc', 0)),
                        success=bool(elem.get('s') == 'true'),
                        thread_name=elem.get('tn', ''),
                        timestamp=datetime.utcfromtimestamp(
                            int(elem.get('ts', 0)) / 1000.0),
                        url=elem.findtext('java.net.URL', ''),
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
        fieldnames -- names of columns (CSV without fieldnames only);
            valid fieldnames are: allThreads, bytes, dataType, elapsed,
            Encoding, ErrorCount, failureMessage, Filename, grpThreads,
            Hostname, IdleTime, label, Latency, responseCode,
            responseMessage, SampleCount, success, threadName,
            timeStamp, URL

        """
        self.source = source
        self.delimiter = kwargs.get('delimiter', ',')
        self.fieldnames = kwargs.get('fieldnames', None)

    def http_samples(self):
        """Generator method which yeilds HTTP samples from the results.

        """
        with open(self.source, 'rb') as fp:
            reader = csv.DictReader(fp, delimiter=self.delimiter,
                    fieldnames=self.fieldnames)
            for row in reader:
                if row.get('failureMessage'):
                    assertion_results = [AssertionResult(
                            error=False,
                            failure=True,
                            failure_message=row['failureMessage'],
                            name='',
                            )]
                else:
                    assertion_results = []
                yield Sample(
                        all_threads=int(row.get('allThreads', 0)),
                        assertion_results=tuple(assertion_results),
                        bytes_received=int(row.get('bytes', 0)),
                        cookies={},
                        data_encoding=row.get('Encoding', ''),
                        data_type=row.get('dataType', ''),
                        elapsed_time=timedelta(
                            milliseconds=int(row.get('elapsed', 0))),
                        error_count=int(row.get('ErrorCount', 0)),
                        group_threads=int(row.get('grpThreads', 0)),
                        hostname=row.get('Hostname', ''),
                        # workarond for JMeter's bug 53802
                        idle_time=timedelta(
                            milliseconds=int(row.get('IdleTime') or 0)),
                        label=row.get('label', ''),
                        latency_time=timedelta(
                            milliseconds=int(row.get('Latency', 0))),
                        method='',
                        query_string='',
                        request_headers={},
                        response_code=row.get('responseCode', ''),
                        response_data='',
                        response_filename=row.get('Filename', ''),
                        response_headers={'status_line': '', 'headers': {}},
                        response_message=row.get('responseMessage', ''),
                        sample_count=int(row.get('SampleCount', 0)),
                        success=bool(row.get('success') == 'true'),
                        thread_name=row.get('threadName', ''),
                        timestamp=datetime.utcfromtimestamp(
                            int(row.get('timeStamp', 0)) / 1000.0),
                        url=row.get('URL', ''),
                        )


def create_parser(source, **kwargs):
    """The function that determines the format of the results file and
    creates and returns the appropriate parser.

    Arguments:
    source -- name of the file containing the results data

    Keyword arguments:
    delimiter -- custom delimiter character (CSV only)
    fieldnames -- names of columns (CSV without fieldnames only);
        valid fieldnames are: allThreads, bytes, dataType, elapsed,
        Encoding, ErrorCount, failureMessage, Filename, grpThreads,
        Hostname, IdleTime, label, Latency, responseCode,
        responseMessage, SampleCount, success, threadName,
        timeStamp, URL

    """
    with open(source) as fp:
        if fp.readline().startswith('<?xml'):
            return XMLParser(source, **kwargs)
        else:
            return CSVParser(source, **kwargs)
