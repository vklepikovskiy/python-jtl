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


class Sample(namedtuple('Sample', 'by, de, dt, ec, hn, it, lb, lt, na, '
                        'ng, rc, rm, s, sc, t, tn, ts')):
    """The class that stores one sample from the results data in named
    tuple. It has the following fields:
    by -- bytes received
    de -- data encoding
    dt -- data type
    ec -- error count (0 or 1, unless multiple samples are aggregated)
    hn -- hostname where the sample was generated
    it -- idle time = time not spent sampling (milliseconds) (generally
          0)
    lb -- label
    lt -- latency = time to initial response (milliseconds) - not all
          samplers support this
    na -- number of active threads for all thread groups
    ng -- number of active threads in this group
    rc -- response code (e.g. 200)
    rm -- response message (e.g. OK)
    s  -- success flag (true/false)
    sc -- sample count (1, unless multiple samples are aggregated)
    t  -- elapsed time (milliseconds)
    tn -- thread name
    ts -- timestamp (milliseconds since midnight Jan 1, 1970 UTC)

    """
    pass


class BaseParser(object):
    """The base class that implements JTL file parsing functionality.

    """
    def http_samples(self):
        """Generator method which yields HTTP samples from the results.
        Must be redefined in subclasses.

        """
        raise NotImplementedError


class XMLParser(BaseParser):
    """The class that implements JTL (XML) file parsing functionality.

    """
    def __init__(self, source):
        """Initialize the class.

        Arguments:
        source -- filename or file object containing the results data

        """
        self.context = etree.iterparse(source, events=('start', 'end'))
        self.context = iter(self.context)
        event, self.root = self.context.next()

    def http_samples(self):
        """Generator method which yields HTTP samples from the results.

        """
        for event, elem in self.context:
            if event == 'end' and elem.tag == 'httpSample':
                attr_dict = dict((attr, elem.get(attr)) for attr in
                        Sample._fields)
                yield Sample(**attr_dict)
            self.root.clear()


def create_parser(source):
    """The function that determines the format of the results file and
    creates and returns the appropriate parser.

    Arguments:
    source -- name of the file containing the results data

    """
    with open(source) as fp:
        if fp.readline().startswith('<?xml'):
            return XMLParser(source)
        else:
            raise NotImplementedError

