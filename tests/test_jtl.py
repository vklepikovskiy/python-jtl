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
                by='61870', de=None, dt='text', ec=None, hn=None, it=None,
                lb='/', lt='796', na=None, ng=None, rc='200', rm='OK',
                s='true', sc=None, t='1196', tn='Thread Group 1-1',
                ts='1341523888836')
        self.assertEqual(http_samples[0], test_sample)
        test_sample = jtl.Sample(
                by='2977', de=None, dt='text', ec=None, hn=None, it=None,
                lb='/some_page', lt='105', na=None, ng=None, rc='404',
                rm='Not Found', s='false', sc=None, t='105',
                tn='Thread Group 1-2', ts='1341523917934')
        self.assertEqual(http_samples[-1], test_sample)
        test_sample = jtl.Sample(
                by='20155', de=None, dt='text', ec=None, hn=None, it=None,
                lb='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA', lt='504',
                na=None, ng=None, rc='200', rm='OK', s='true', sc=None,
                t='666', tn='Thread Group 1-2', ts='1341523903585')
        self.assertEqual(http_samples[39], test_sample)

    def test_http_samples_csv(self):
        sample_filename = os.path.join(self.tests_dir, 'samples/2.jtl')
        parser = jtl.create_parser(sample_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)
        test_sample = jtl.Sample(
                by='62552', de=None, dt='text', ec=None, hn=None, it=None,
                lb='/', lt='693', na=None, ng=None, rc='200', rm='OK',
                s='true', sc=None, t='1099', tn='Thread Group 1-1',
                ts='1342987956100')
        self.assertEqual(http_samples[0], test_sample)
        test_sample = jtl.Sample(
                by='2976', de=None, dt='text', ec=None, hn=None, it=None,
                lb='/some_page', lt='497', na=None, ng=None, rc='404',
                rm='Not Found', s='false', sc=None, t='497',
                tn='Thread Group 1-1', ts='1342987983537')
        self.assertEqual(http_samples[79], test_sample)
        test_sample = jtl.Sample(
                by='21476', de=None, dt='text', ec=None, hn=None, it=None,
                lb='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA', lt='751',
                na=None, ng=None, rc='200', rm='OK', s='true', sc=None,
                t='1074', tn='Thread Group 1-1', ts='1342987969778')
        self.assertEqual(http_samples[38], test_sample)


if __name__ == '__main__':
    unittest.main()
