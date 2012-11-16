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


class FieldnamesTestCase(unittest.TestCase):
    """Testing CSV without fieldnames.

    """
    @classmethod
    def setUpClass(cls):
        cls.tests_dir = os.path.dirname(os.path.abspath(__file__))

    def test_csv(self):
        """Test CSV parser.

        """
        samples_filename = os.path.join(self.tests_dir,
                'samples/fieldnames.csv')
        parser = jtl.create_parser(samples_filename, fieldnames=(
            'timeStamp', 'elapsed', 'label', 'responseCode', 'responseMessage',
            'threadName', 'dataType', 'success', 'bytes', 'Latency'))
        samples = list(parser.itersamples())
        self.assertEqual(len(samples), 1)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(),
                bytes_received=64653,
                children=(),
                cookies={},
                data_encoding='',
                data_type='text',
                elapsed_time=timedelta(0, 1, 336000),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='"Home" page',
                latency_time=timedelta(0, 0, 851000),
                method='',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers={'status_line': '', 'headers': {}},
                response_message='OK',
                sample_count=0,
                success=True,
                tag_name='',
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 20, 42, 8, 465000),
                url='',
                )
        self.assertEqual(samples[0], test_sample)


if __name__ == '__main__':
    unittest.main()
