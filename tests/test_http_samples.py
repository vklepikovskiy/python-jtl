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
        """Test XML parser using HTTP samples data saved with default
        settings enabled.

        """
        samples_filename = os.path.join(self.tests_dir,
                'http_samples_data/default.xml')
        parser = jtl.create_parser(samples_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    ),
                bytes_received=62874,
                cookies={},
                data_encoding='',
                data_type='text',
                elapsed_time=timedelta(0, 1, 76000),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='"Home" page',
                latency_time=timedelta(0, 0, 668000),
                method='',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='OK',
                sample_count=0,
                success=True,
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 17, 21, 49, 57, 986000),
                url='',
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    ),
                bytes_received=21216,
                cookies={},
                data_encoding='',
                data_type='text',
                elapsed_time=timedelta(0, 1, 67000),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                latency_time=timedelta(0, 0, 739000),
                method='',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='OK',
                sample_count=0,
                success=True,
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 17, 21, 50, 35, 65000),
                url='',
                )
        self.assertEqual(http_samples[47], test_sample)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(
                    jtl.AssertionResult(
                        error=False,
                        failure=True,
                        failure_message='Test failed: code expected to equal '
                            '/\n\n****** received  : [[[404]]]\n\n****** '
                            'comparison: [[[200]]]\n\n/',
                        name='Response Assertion',
                        ),
                    jtl.AssertionResult(
                        error=False,
                        failure=True,
                        failure_message='Test failed: message expected to '
                            'equal /\n\n****** received  : [[[Not Found]]]\n\n'
                            '****** comparison: [[[OK       ]]]\n\n/',
                        name='Response Assertion',
                        ),
                    ),
                bytes_received=2976,
                cookies={},
                data_encoding='',
                data_type='text',
                elapsed_time=timedelta(0, 0, 106000),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='fourth sample, last sample',
                latency_time=timedelta(0, 0, 104000),
                method='',
                query_string='',
                request_headers={},
                response_code='404',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='Not Found',
                sample_count=0,
                success=False,
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 17, 21, 50, 56, 587000),
                url='',
                )
        self.assertEqual(http_samples[79], test_sample)

    def test_xml_all(self):
        """Test XML parser using HTTP samples data saved with all
        settings enabled.

        """
        samples_filename = os.path.join(self.tests_dir,
                'http_samples_data/all.xml')
        parser = jtl.create_parser(samples_filename)
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)

        self.assertEqual(len(http_samples[0].request_headers), 5)
        assert 'Accept-Language' in http_samples[0].request_headers
        self.assertEqual(http_samples[0].request_headers['Accept-Language'],
                'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3')
        response_headers_hash = hashlib.md5(
                http_samples[0].response_headers.encode('utf-8')).hexdigest()
        self.assertEqual(response_headers_hash,
                'e020a373e777cefc230081df26a06a6b')
        http_samples[0] = http_samples[0]._replace(request_headers={},
                response_headers='')

        test_sample = jtl.Sample(
                all_threads=2,
                assertion_results=(
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    ),
                bytes_received=64189,
                cookies={},
                data_encoding='utf-8',
                data_type='text',
                elapsed_time=timedelta(0, 1, 350000),
                error_count=0,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='"Home" page',
                latency_time=timedelta(0, 0, 802000),
                method='GET',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='OK',
                sample_count=1,
                success=True,
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 21, 49, 21, 246000),
                url='http://www.yahoo.com/',
                )
        self.assertEqual(http_samples[0], test_sample)

        self.assertEqual(len(http_samples[39].cookies), 7)
        assert 'MSC' in http_samples[39].cookies
        self.assertEqual(http_samples[39].cookies['MSC'], 't=1345758579X')
        self.assertEqual(len(http_samples[39].request_headers), 5)
        assert 'Accept-Encoding' in http_samples[39].request_headers
        self.assertEqual(http_samples[39].request_headers['Accept-Encoding'],
                'gzip, deflate')
        response_data_hash = hashlib.md5(
                http_samples[39].response_data.encode('utf-8')).hexdigest()
        self.assertEqual(response_data_hash,
                '1d6165ad17ce4278351db7c3993c097f')
        response_headers_hash = hashlib.md5(
                http_samples[39].response_headers.encode('utf-8')).hexdigest()
        self.assertEqual(response_headers_hash,
                '67c76a25b15a057ece26f4d70c426c0a')
        http_samples[39] = http_samples[39]._replace(cookies={},
                request_headers={}, response_data='', response_headers='')

        test_sample = jtl.Sample(
                all_threads=2,
                assertion_results=(
                    jtl.AssertionResult(
                        error=False,
                        failure=True,
                        failure_message='Test failed: code expected to equal '
                            '/\n\n****** received  : [[[404]]]\n\n****** '
                            'comparison: [[[200]]]\n\n/',
                        name='Response Assertion',
                        ),
                    jtl.AssertionResult(
                        error=False,
                        failure=True,
                        failure_message='Test failed: message expected to '
                            'equal /\n\n****** received  : [[[Not Found]]]'
                            '\n\n****** comparison: [[[OK       ]]]\n\n/',
                        name='Response Assertion',
                        ),
                    ),
                bytes_received=2977,
                cookies={},
                data_encoding='utf-8',
                data_type='text',
                elapsed_time=timedelta(0, 0, 137000),
                error_count=1,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='fourth sample, last sample',
                latency_time=timedelta(0, 0, 137000),
                method='GET',
                query_string='',
                request_headers={},
                response_code='404',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='Not Found',
                sample_count=1,
                success=False,
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 21, 49, 40, 553000),
                url='http://www.yahoo.com/some_page',
                )
        self.assertEqual(http_samples[39], test_sample)

        self.assertEqual(len(http_samples[78].cookies), 4)
        assert 'B' in http_samples[78].cookies
        self.assertEqual(http_samples[78].cookies['B'],
                '5vdh93l83d9cc&b=3&s=bs')
        self.assertEqual(len(http_samples[78].request_headers), 6)
        assert 'Referer' in http_samples[78].request_headers
        self.assertEqual(http_samples[78].request_headers['Referer'],
                'http://search.yahoo.com/search;_ylt=A03uoRrUAfZPg18BCCmbvZx4'
                '?p=potato&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-701')
        response_headers_hash = hashlib.md5(
                http_samples[78].response_headers.encode('utf-8')).hexdigest()
        self.assertEqual(response_headers_hash,
                '619795b6767475a1c6f64bde2d034def')
        http_samples[78] = http_samples[78]._replace(cookies={},
                request_headers={}, response_headers='')

        test_sample = jtl.Sample(
                all_threads=1,
                assertion_results=(
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    jtl.AssertionResult(
                        error=False,
                        failure=False,
                        failure_message='',
                        name='Response Assertion',
                        ),
                    ),
                bytes_received=71256,
                cookies={},
                data_encoding='UTF-8',
                data_type='text',
                elapsed_time=timedelta(0, 3, 571000),
                error_count=0,
                group_threads=1,
                hostname='hppc',
                idle_time=timedelta(0),
                label='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                latency_time=timedelta(0, 0, 790000),
                method='GET',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='OK',
                sample_count=1,
                success=True,
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 21, 50, 4, 17000),
                url='http://images.search.yahoo.com/search/images;'
                    '_ylt=A0oG7lg2AvZPowgACQNXNyoA?ei=UTF-8&p=potato'
                    '&fr2=tab-web&fr=yfp-t-701',
                )
        self.assertEqual(http_samples[78], test_sample)

    def test_csv_default(self):
        """Test CSV parser using HTTP samples data saved with default
        settings enabled.

        """
        samples_filename = os.path.join(self.tests_dir,
                'http_samples_data/default.csv')
        parser = jtl.create_parser(samples_filename, fieldnames=(
            'timeStamp', 'elapsed', 'label', 'responseCode', 'responseMessage',
            'threadName', 'dataType', 'success', 'bytes', 'Latency'))
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(),
                bytes_received=64653,
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
                response_headers='',
                response_message='OK',
                sample_count=0,
                success=True,
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 20, 42, 8, 465000),
                url='',
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(),
                bytes_received=21236,
                cookies={},
                data_encoding='',
                data_type='text',
                elapsed_time=timedelta(0, 0, 680000),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                latency_time=timedelta(0, 0, 517000),
                method='',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='OK',
                sample_count=0,
                success=True,
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 20, 42, 23, 796000),
                url='',
                )
        self.assertEqual(http_samples[39], test_sample)

        test_sample = jtl.Sample(
                all_threads=0,
                assertion_results=(),
                bytes_received=2977,
                cookies={},
                data_encoding='',
                data_type='text',
                elapsed_time=timedelta(0, 0, 125000),
                error_count=0,
                group_threads=0,
                hostname='',
                idle_time=timedelta(0),
                label='fourth sample, last sample',
                latency_time=timedelta(0, 0, 125000),
                method='',
                query_string='',
                request_headers={},
                response_code='404',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='Not Found',
                sample_count=0,
                success=False,
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 20, 42, 38, 720000),
                url='',
                )
        self.assertEqual(http_samples[79], test_sample)

    def test_csv_all(self):
        """Test CSV parser using HTTP samples data saved with all
        settings enabled and custom delimiter character.

        """
        samples_filename = os.path.join(self.tests_dir,
                'http_samples_data/all.csv')
        parser = jtl.create_parser(samples_filename, delimiter='|')
        http_samples = list(parser.http_samples())
        self.assertEqual(len(http_samples), 80)

        test_sample = jtl.Sample(
                all_threads=2,
                assertion_results=(),
                bytes_received=64366,
                cookies={},
                data_encoding='utf-8',
                data_type='text',
                elapsed_time=timedelta(0, 1, 152000),
                error_count=0,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='"Home" page',
                latency_time=timedelta(0, 0, 755000),
                method='',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='OK',
                sample_count=1,
                success=True,
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 21, 53, 59, 670000),
                url='http://www.yahoo.com/',
                )
        self.assertEqual(http_samples[0], test_sample)

        test_sample = jtl.Sample(
                all_threads=2,
                assertion_results=(
                    jtl.AssertionResult(
                        error=False,
                        failure=True,
                        failure_message='Test failed: code expected to equal '
                            '/\n\n****** received  : [[[404]]]\n\n****** '
                            'comparison: [[[200]]]\n\n/',
                        name='',
                        ),
                    ),
                bytes_received=2977,
                cookies={},
                data_encoding='utf-8',
                data_type='text',
                elapsed_time=timedelta(0, 0, 109000),
                error_count=1,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='fourth sample, last sample',
                latency_time=timedelta(0, 0, 109000),
                method='',
                query_string='',
                request_headers={},
                response_code='404',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='Not Found',
                sample_count=1,
                success=False,
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 21, 54, 18, 365000),
                url='http://www.yahoo.com/some_page',
                )
        self.assertEqual(http_samples[40], test_sample)

        test_sample = jtl.Sample(
                all_threads=1,
                assertion_results=(),
                bytes_received=21247,
                cookies={},
                data_encoding='UTF-8',
                data_type='text',
                elapsed_time=timedelta(0, 0, 882000),
                error_count=0,
                group_threads=1,
                hostname='hppc',
                idle_time=timedelta(0),
                label='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                latency_time=timedelta(0, 0, 704000),
                method='',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers='',
                response_message='OK',
                sample_count=1,
                success=True,
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 21, 54, 33, 601000),
                url='http://images.search.yahoo.com/search/images;'
                    '_ylt=A0oG7lg2AvZPowgACQNXNyoA?ei=UTF-8&p=potato'
                    '&fr2=tab-web&fr=yfp-t-701',
                )
        self.assertEqual(http_samples[78], test_sample)


if __name__ == '__main__':
    unittest.main()
