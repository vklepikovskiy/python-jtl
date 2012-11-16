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


from datetime import datetime, timedelta
import jtl
import os.path
import unittest


class MinimizedTestCase(unittest.TestCase):
    """Testing minimized samples.

    """
    @classmethod
    def setUpClass(cls):
        cls.tests_dir = os.path.dirname(os.path.abspath(__file__))

    def test_xml(self):
        """Test XML parser.

        """
        samples_filename = os.path.join(self.tests_dir,
                'samples/minimized.xml')
        parser = jtl.create_parser(samples_filename)
        samples = list(parser.itersamples())
        self.assertEqual(len(samples), 1)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(),
                bytes_received=0,
                children=(),
                cookies={},
                data_encoding='',
                data_type='',
                elapsed_time=timedelta(0),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='',
                latency_time=timedelta(0),
                method='',
                query_string='',
                request_headers={},
                response_code='',
                response_data='',
                response_filename='',
                response_headers={'status_line': '', 'headers': {}},
                response_message='',
                sample_count=0,
                success=False,
                tag_name='httpSample',
                thread_name='',
                timestamp=datetime(2012, 11, 13, 0, 4, 10, 289000),
                url='',
                )
        self.assertEqual(samples[0], test_sample)

    def test_csv(self):
        """Test CSV parser.

        """
        samples_filename = os.path.join(self.tests_dir,
                'samples/minimized.csv')
        parser = jtl.create_parser(samples_filename)
        samples = list(parser.itersamples())
        self.assertEqual(len(samples), 1)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(),
                bytes_received=0,
                children=(),
                cookies={},
                data_encoding='',
                data_type='',
                elapsed_time=timedelta(0),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='',
                latency_time=timedelta(0),
                method='',
                query_string='',
                request_headers={},
                response_code='',
                response_data='',
                response_filename='',
                response_headers={'status_line': '', 'headers': {}},
                response_message='',
                sample_count=0,
                success=False,
                tag_name='',
                thread_name='',
                timestamp=datetime(2012, 11, 13, 0, 32, 16, 306000),
                url='',
                )
        self.assertEqual(samples[0], test_sample)


if __name__ == '__main__':
    unittest.main()
