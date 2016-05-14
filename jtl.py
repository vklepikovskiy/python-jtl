# Copyright (C) 2012-2016 Victor Klepikovskiy
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
from datetime import datetime, timedelta
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
            'all_threads', 'assertion_results', 'bytes_received', 'children',
            'cookies', 'data_encoding', 'data_type', 'elapsed_time',
            'error_count', 'group_threads', 'hostname', 'idle_time', 'label',
            'latency_time', 'method', 'query_string', 'request_headers',
            'response_code', 'response_data', 'response_filename',
            'response_headers', 'response_message', 'sample_count', 'success',
            'tag_name', 'thread_name', 'timestamp', 'url',
            ))):
    """The class that stores the single sample from the results data.
    It contains the following fields:

    all_threads       -- number of active threads for all thread groups
    assertion_results -- assertion results
    bytes_received    -- bytes received
    children          -- list of child samples
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
    tag_name          -- sample tag name (XML only)
    thread_name       -- thread name
    timestamp         -- timestamp
    url               -- url

    """
    pass


class BaseParser(object):
    """The base class for JTL parsers.

    """
    def itersamples(self):
        """Generator method which yields samples from the results. Must be
        redefined in subclasses.

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

    def _get_assertion_results(self, elem):
        """Get assertion results from the sample and return them as a list of
        AssertionResult class instances.

        """
        assertion_results = []
        for item in elem.findall('assertionResult'):
            fields = {}
            fields['error'] = bool(item.findtext('error', '') == 'true')
            fields['failure'] = bool(item.findtext('failure', '') == 'true')
            fields['failure_message'] = item.findtext('failureMessage', '')
            fields['name'] = item.findtext('name', '')
            assertion_results.append(AssertionResult(**fields))
        return tuple(assertion_results)

    def _get_cookies(self, elem):
        """Get cookies from the sample and return them as a dictionary.

        """
        return dict([c.split('=', 1)
                for c in elem.findtext('cookies', '').split('; ') if c])

    def _get_request_headers(self, elem):
        """Get request headers from the sample and return them as a
        dictionary.

        """
        return dict([h.split(': ', 1)
                for h in elem.findtext('requestHeader', '').splitlines() if h])

    def _get_response_headers(self, elem):
        """Get response headers from the sample and return them as
        a dictionary.

        """
        response_status_line, response_headers = (elem.findtext(
                'responseHeader', '\n') or '\n').split('\n', 1)
        response_headers = dict([h.split(': ', 1)
                for h in response_headers.splitlines() if h])
        return {'status_line': response_status_line,
                'headers': response_headers}

    def _get_sample(self, elem, children=()):
        """Return the sample data as an instance of Sample class.

        """
        sample = {}
        sample['all_threads'] = int(elem.get('na', 0))
        sample['assertion_results'] = self._get_assertion_results(elem)
        sample['bytes_received'] = int(elem.get('by', 0))
        sample['children'] = tuple(children)
        sample['cookies'] = self._get_cookies(elem)
        sample['data_encoding'] = elem.get('de', '')
        sample['data_type'] = elem.get('dt', '')
        sample['elapsed_time'] = timedelta(milliseconds=int(elem.get('t', 0)))
        sample['error_count'] = int(elem.get('ec', 0))
        sample['group_threads'] = int(elem.get('ng', 0))
        sample['hostname'] = elem.get('hn', '')
        sample['idle_time'] = timedelta(milliseconds=int(elem.get('it', 0)))
        sample['label'] = elem.get('lb', '')
        sample['latency_time'] = timedelta(milliseconds=int(elem.get('lt', 0)))
        sample['method'] = elem.findtext('method', '')
        sample['query_string'] = elem.findtext('queryString', '')
        sample['request_headers'] = self._get_request_headers(elem)
        sample['response_code'] = elem.get('rc', '')
        sample['response_data'] = elem.findtext('responseData', '')
        sample['response_filename'] = elem.findtext('responseFile', '')
        sample['response_headers'] = self._get_response_headers(elem)
        sample['response_message'] = elem.get('rm', '')
        sample['sample_count'] = int(elem.get('sc', 0))
        sample['success'] = bool(elem.get('s') == 'true')
        sample['tag_name'] = elem.tag
        sample['thread_name'] = elem.get('tn', '')
        sample['timestamp'] = datetime.utcfromtimestamp(
                int(elem.get('ts', 0)) / 1000.0)
        sample['url'] = elem.findtext('java.net.URL', '')
        return Sample(**sample)

    def itersamples(self):
        """Generator method which yields samples from the results.

        """
        sample_started = False
        sample_children = []
        for event, elem in self.context:
            if event == 'start' and elem.tag == 'sample':
                sample_started = True
                sample_children = []
            elif event == 'end' and elem.tag == 'httpSample':
                sample = self._get_sample(elem)
                if sample_started:
                    sample_children.append(sample)
                else:
                    yield sample
            elif event == 'end' and elem.tag == 'sample':
                sample = self._get_sample(elem, sample_children)
                sample_started = False
                yield sample
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

    def _get_assertion_results(self, row):
        """Get assertion results from the sample and return them as a list of
        AssertionResult class instances.

        """
        assertion_results = []
        if row.get('failureMessage'):
            fields = {}
            fields['error'] = False
            fields['failure'] = True
            fields['failure_message'] = row['failureMessage']
            fields['name'] = ''
            assertion_results.append(AssertionResult(**fields))
        return tuple(assertion_results)

    def _get_sample(self, row):
        """Return the sample data as an instance of Sample class.

        """
        sample = {}
        sample['all_threads'] = int(row.get('allThreads', 0))
        sample['assertion_results'] = self._get_assertion_results(row)
        sample['bytes_received'] = int(row.get('bytes', 0))
        sample['children'] = ()
        sample['cookies'] = {}
        sample['data_encoding'] = row.get('Encoding', '')
        sample['data_type'] = row.get('dataType', '')
        sample['elapsed_time'] = timedelta(
                milliseconds=int(row.get('elapsed', 0)))
        sample['error_count'] = int(row.get('ErrorCount', 0))
        sample['group_threads'] = int(row.get('grpThreads', 0))
        sample['hostname'] = row.get('Hostname', '')
        # workarond for JMeter's bug 53802
        sample['idle_time'] = timedelta(
                milliseconds=int(row.get('IdleTime') or 0))
        sample['label'] = row.get('label', '')
        sample['latency_time'] = timedelta(
                milliseconds=int(row.get('Latency', 0)))
        sample['method'] = ''
        sample['query_string'] = ''
        sample['request_headers'] = {}
        sample['response_code'] = row.get('responseCode', '')
        sample['response_data'] = ''
        sample['response_filename'] = row.get('Filename', '')
        sample['response_headers'] = {'status_line': '', 'headers': {}}
        sample['response_message'] = row.get('responseMessage', '')
        sample['sample_count'] = int(row.get('SampleCount', 0))
        sample['success'] = bool(row.get('success') == 'true')
        sample['tag_name'] = ''
        sample['thread_name'] = row.get('threadName', '')
        sample['timestamp'] = datetime.utcfromtimestamp(
                int(row.get('timeStamp', 0)) / 1000.0)
        sample['url'] = row.get('URL', '')
        return Sample(**sample)

    def itersamples(self):
        """Generator method which yeilds samples from the results.

        """
        with open(self.source, 'rb') as fp:
            reader = csv.DictReader(fp, delimiter=self.delimiter,
                    fieldnames=self.fieldnames)
            for row in reader:
                yield self._get_sample(row)


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
