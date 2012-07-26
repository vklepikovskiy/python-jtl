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


import unittest
import jtl
import os.path
from datetime import timedelta, datetime


class JTLTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tests_dir = os.path.dirname(os.path.abspath(__file__))

    def test_http_samples_xml(self):
        sample_filename = os.path.join(self.tests_dir, 'samples/1.jtl')
        parser = jtl.create_parser(sample_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)
        test_sample = jtl.Sample(
                by=61870, de='', dt='text', ec=0, hn='', it=timedelta(0),
                lb='/', lt=timedelta(0, 0, 796000), na=0, ng=0, rc='200',
                rm='OK', su=True, sc=0, ti=timedelta(0, 1, 196000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 5, 21, 31, 28, 836000))
        self.assertEqual(http_samples[0], test_sample)
        test_sample = jtl.Sample(
                by=2977, de='', dt='text', ec=0, hn='', it=timedelta(0),
                lb='/some_page', lt=timedelta(0, 0, 105000), na=0, ng=0,
                rc='404', rm='Not Found', su=False, sc=0,
                ti=timedelta(0, 0, 105000), tn='Thread Group 1-2',
                ts=datetime(2012, 7, 5, 21, 31, 57, 934000))
        self.assertEqual(http_samples[-1], test_sample)
        test_sample = jtl.Sample(
                by=20155, de='', dt='text', ec=0, hn='', it=timedelta(0),
                lb='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                lt=timedelta(0, 0, 504000), na=0, ng=0, rc='200', rm='OK',
                su=True, sc=0, ti=timedelta(0, 0, 666000),
                tn='Thread Group 1-2',
                ts=datetime(2012, 7, 5, 21, 31, 43, 585000))
        self.assertEqual(http_samples[39], test_sample)

    def test_http_samples_csv(self):
        sample_filename = os.path.join(self.tests_dir, 'samples/2.jtl')
        parser = jtl.create_parser(sample_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)
        test_sample = jtl.Sample(
                by=63296, de='', dt='text', ec=0, hn='', it=timedelta(0),
                lb='"Home" page', lt=timedelta(0, 0, 803000), na=0, ng=0,
                rc='200', rm='OK', su=True, sc=0, ti=timedelta(0, 1, 302000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 25, 22, 11, 35, 474000))
        self.assertEqual(http_samples[0], test_sample)
        test_sample = jtl.Sample(
                by=2977, de='', dt='text', ec=0, hn='', it=timedelta(0),
                lb='fourth sample, last sample', lt=timedelta(0, 0, 130000),
                na=0, ng=0, rc='404', rm='Not Found', su=False, sc=0,
                ti=timedelta(0, 0, 130000), tn='Thread Group 1-2',
                ts=datetime(2012, 7, 25, 22, 12, 5, 503000))
        self.assertEqual(http_samples[79], test_sample)
        test_sample = jtl.Sample(
                by=18731, de='', dt='text', ec=0, hn='', it=timedelta(0),
                lb='/search;_ylt=A03uoRrUAfZPg18BCCmbvZx4',
                lt=timedelta(0, 0, 383000), na=0, ng=0, rc='200', rm='OK',
                su=True, sc=0, ti=timedelta(0, 1, 77000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 25, 22, 11, 51, 466000))
        self.assertEqual(http_samples[42], test_sample)


if __name__ == '__main__':
    unittest.main()
