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
import hashlib


class HttpSamplesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tests_dir = os.path.dirname(os.path.abspath(__file__))

    def test_xml_default(self):
        """Test HTTP samples with default settings (XML).

        """
        sample_filename = os.path.join(self.tests_dir, 'samples/1.jtl')
        parser = jtl.create_parser(sample_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)

        test_sample = jtl.Sample(
                ar=(),
                by=61870,
                de='',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='/',
                lt=timedelta(0, 0, 796000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=0,
                ti=timedelta(0, 1, 196000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 5, 21, 31, 28, 836000),
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                ar=(),
                by=2977,
                de='',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='/some_page',
                lt=timedelta(0, 0, 105000),
                na=0,
                ng=0,
                rc='404',
                rd='',
                rf='',
                rh='',
                rm='Not Found',
                su=False,
                sc=0,
                ti=timedelta(0, 0, 105000),
                tn='Thread Group 1-2',
                ts=datetime(2012, 7, 5, 21, 31, 57, 934000),
                )
        self.assertEqual(http_samples[-1], test_sample)

        test_sample = jtl.Sample(
                ar=(),
                by=20155,
                de='',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                lt=timedelta(0, 0, 504000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=0,
                ti=timedelta(0, 0, 666000),
                tn='Thread Group 1-2',
                ts=datetime(2012, 7, 5, 21, 31, 43, 585000),
                )
        self.assertEqual(http_samples[39], test_sample)

    def test_csv_default(self):
        """Test HTTP samples with default settings (CSV).

        """
        sample_filename = os.path.join(self.tests_dir, 'samples/2.jtl')
        parser = jtl.create_parser(sample_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)

        test_sample = jtl.Sample(
                ar=(),
                by=63296,
                de='',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='"Home" page',
                lt=timedelta(0, 0, 803000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=0,
                ti=timedelta(0, 1, 302000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 25, 22, 11, 35, 474000),
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                ar=(),
                by=2977,
                de='',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='fourth sample, last sample',
                lt=timedelta(0, 0, 130000),
                na=0,
                ng=0,
                rc='404',
                rd='',
                rf='',
                rh='',
                rm='Not Found',
                su=False,
                sc=0,
                ti=timedelta(0, 0, 130000),
                tn='Thread Group 1-2',
                ts=datetime(2012, 7, 25, 22, 12, 5, 503000),
                )
        self.assertEqual(http_samples[79], test_sample)

        test_sample = jtl.Sample(
                ar=(),
                by=18731,
                de='',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='/search;_ylt=A03uoRrUAfZPg18BCCmbvZx4',
                lt=timedelta(0, 0, 383000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=0,
                ti=timedelta(0, 1, 77000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 25, 22, 11, 51, 466000),
                )
        self.assertEqual(http_samples[42], test_sample)

    def test_xml_ar_de_ec_sc(self):
        """Test HTTP samples with default settings + ar, de, ec, sc
        fields (XML).

        """
        sample_filename = os.path.join(self.tests_dir, 'samples/3.jtl')
        parser = jtl.create_parser(sample_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 72)

        test_sample = jtl.Sample(
                ar=(
                    jtl.AssertionResult(er=False, fa=False, fm='',
                            na='Response Assertion'),
                    jtl.AssertionResult(er=False, fa=False, fm='',
                            na='Response Assertion'),
                    ),
                by=66580,
                de='utf-8',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='"Home" page',
                lt=timedelta(0, 1, 80000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=1,
                ti=timedelta(0, 1, 863000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 28, 21, 34, 22, 595000),
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                ar=(
                    jtl.AssertionResult(er=False, fa=True,
                            fm='Test failed: code expected to equal /\n\n'
                                '****** received  : [[[404]]]\n\n****** '
                                'comparison: [[[200]]]\n\n/',
                            na='Response Assertion'),
                    jtl.AssertionResult(er=False, fa=True,
                            fm='Test failed: message expected to equal /\n\n'
                                '****** received  : [[[Not Found]]]\n\n****** '
                                'comparison: [[[OK       ]]]\n\n/',
                            na='Response Assertion'),
                    ),
                by=2977,
                de='utf-8',
                dt='text',
                ec=1,
                hn='',
                it=timedelta(0),
                lb='fourth sample, last sample',
                lt=timedelta(0, 0, 160000),
                na=0,
                ng=0,
                rc='404',
                rd='',
                rf='',
                rh='',
                rm='Not Found',
                su=False,
                sc=1,
                ti=timedelta(0, 0, 160000),
                tn='Thread Group 1-2',
                ts=datetime(2012, 7, 28, 21, 34, 56, 237000),
                )
        self.assertEqual(http_samples[71], test_sample)

        test_sample = jtl.Sample(
                ar=(
                    jtl.AssertionResult(er=False, fa=False, fm='',
                            na='Response Assertion'),
                    jtl.AssertionResult(er=False, fa=False, fm='',
                            na='Response Assertion'),
                    ),
                by=21505,
                de='UTF-8',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                lt=timedelta(0, 0, 890000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=1,
                ti=timedelta(0, 1, 193000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 28, 21, 34, 40, 780000),
                )
        self.assertEqual(http_samples[36], test_sample)

    def test_csv(self):
        """Test HTTP samples with default settings + ar, de, ec, sc
        fields and custom delimiter character (CSV).

        """
        sample_filename = os.path.join(self.tests_dir, 'samples/4.jtl')
        parser = jtl.create_parser(sample_filename, delimiter='|')
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 72)

        test_sample = jtl.Sample(
                ar=(),
                by=66714,
                de='utf-8',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='"Home" page',
                lt=timedelta(0, 1, 127000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=1,
                ti=timedelta(0, 1, 605000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 7, 28, 21, 35, 29, 19000),
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                ar=(
                    jtl.AssertionResult(er=False, fa=True,
                            fm='Test failed: code expected to equal /\n\n'
                               '****** received  : [[[404]]]\n\n****** '
                               'comparison: [[[200]]]\n\n/',
                            na=''),
                    ),
                by=2976,
                de='utf-8',
                dt='text',
                ec=1,
                hn='',
                it=timedelta(0),
                lb='fourth sample, last sample',
                lt=timedelta(0, 0, 239000),
                na=0,
                ng=0,
                rc='404',
                rd='',
                rf='',
                rh='',
                rm='Not Found',
                su=False,
                sc=1,
                ti=timedelta(0, 0, 239000),
                tn='Thread Group 1-2',
                ts=datetime(2012, 7, 28, 21, 36, 1, 340000),
                )
        self.assertEqual(http_samples[71], test_sample)

        test_sample = jtl.Sample(
                ar=(),
                by=19272,
                de='UTF-8',
                dt='text',
                ec=0,
                hn='',
                it=timedelta(0),
                lb='/search;_ylt=A03uoRrUAfZPg18BCCmbvZx4',
                lt=timedelta(0, 0, 533000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=1,
                ti=timedelta(0, 1, 210000),
                tn='Thread Group 1-2',
                ts=datetime(2012, 7, 28, 21, 35, 45, 6000),
                )
        self.assertEqual(http_samples[34], test_sample)

    def test_xml_hn_rd_rf_rh(self):
        """Test hn, rd, rf, rh fields of HTTP samples (XML).

        """
        sample_filename = os.path.join(self.tests_dir, 'samples/5.jtl')
        parser = jtl.create_parser(sample_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 8)

        self.assertEqual(http_samples[0].hn, 'hppc')
        rh_hash = hashlib.md5(http_samples[0].rh.encode('utf-8')).hexdigest()
        rd_hash = hashlib.md5(http_samples[0].rd.encode('utf-8')).hexdigest()
        self.assertEqual(rh_hash, '2601205232aae2d1b9db4e40442a273f')
        self.assertEqual(rd_hash, 'fc4e078654a3ce52e131aec004a979c3')
        self.assertEqual(http_samples[0].rf, '')

        self.assertEqual(http_samples[7].hn, 'hppc')
        rh_hash = hashlib.md5(http_samples[7].rh.encode('utf-8')).hexdigest()
        rd_hash = hashlib.md5(http_samples[7].rd.encode('utf-8')).hexdigest()
        self.assertEqual(rh_hash, '3eb75abac01f48f1ef537d8fe9b23cf3')
        self.assertEqual(rd_hash, 'dffc36ed460841da29f95ee281595aab')
        self.assertEqual(http_samples[7].rf, '')

        self.assertEqual(http_samples[3].hn, 'hppc')
        rh_hash = hashlib.md5(http_samples[3].rh.encode('utf-8')).hexdigest()
        rd_hash = hashlib.md5(http_samples[3].rd.encode('utf-8')).hexdigest()
        self.assertEqual(rh_hash, 'a2ddb572abec11e5209b030ea706a9c8')
        self.assertEqual(rd_hash, 'd8efeea920a875cffee01aa9912e975c')
        self.assertEqual(http_samples[3].rf, '')

    def test_csv_without_fieldnames_hn(self):
        """Test CSV results without fieldnames and hn field of HTTP
        samples.

        """
        sample_filename = os.path.join(self.tests_dir, 'samples/6.jtl')
        parser = jtl.create_parser(sample_filename, fieldnames=(
            'timeStamp', 'elapsed', 'label', 'responseCode', 'responseMessage',
            'threadName', 'dataType', 'success', 'bytes', 'Filename',
            'Latency', 'Encoding', 'SampleCount', 'ErrorCount', 'Hostname'))
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 100)

        test_sample = jtl.Sample(
                ar=(),
                by=63698,
                de='utf-8',
                dt='text',
                ec=0,
                hn='hppc',
                it=timedelta(0),
                lb='"Home" page',
                lt=timedelta(0, 0, 869000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=1,
                ti=timedelta(0, 1, 370000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 8, 13, 20, 32, 2, 267000),
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                ar=(),
                by=4963,
                de='ISO-8859-1',
                dt='text',
                ec=0,
                hn='hppc',
                it=timedelta(0),
                lb='/themes/cursors/zips/misc/tamagotchi.zip',
                lt=timedelta(0, 0, 387000),
                na=0,
                ng=0,
                rc='200',
                rd='',
                rf='',
                rh='',
                rm='OK',
                su=True,
                sc=1,
                ti=timedelta(0, 0, 387000),
                tn='Thread Group 1-1',
                ts=datetime(2012, 8, 13, 20, 32, 36, 881000),
                )
        self.assertEqual(http_samples[99], test_sample)


if __name__ == '__main__':
    unittest.main()
