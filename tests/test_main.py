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
import hashlib
import jtl
import os.path
import unittest


class MainTestCase(unittest.TestCase):
    """python-jtl main tests.

    """
    @classmethod
    def setUpClass(cls):
        cls.tests_dir = os.path.dirname(os.path.abspath(__file__))

    def test_xml(self):
        """Test XML parser.

        """
        samples_filename = os.path.join(self.tests_dir,
                'samples/main.xml')
        parser = jtl.create_parser(samples_filename)
        samples = list(parser.itersamples())
        self.assertEqual(len(samples), 3)

        self.assertEqual(len(samples[0].request_headers), 5)
        assert 'Accept-Language' in samples[0].request_headers
        self.assertEqual(samples[0].request_headers['Accept-Language'],
                'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3')
        self.assertEqual(samples[0].response_headers['status_line'],
                'HTTP/1.1 200 OK')
        self.assertEqual(len(samples[0].response_headers['headers']), 12)
        assert 'Server' in samples[0].response_headers['headers']
        self.assertEqual(samples[0].response_headers['headers']['Server'],
                'YTS/1.20.10')
        samples[0] = samples[0]._replace(request_headers={},
                response_headers={'status_line': '', 'headers': {}})

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
                response_headers={'status_line': '', 'headers': {}},
                response_message='OK',
                sample_count=1,
                success=True,
                tag_name='httpSample',
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 21, 49, 21, 246000),
                url='http://www.yahoo.com/',
                )
        self.assertEqual(samples[0], test_sample)

        self.assertEqual(len(samples[1].cookies), 7)
        assert 'MSC' in samples[1].cookies
        self.assertEqual(samples[1].cookies['MSC'], 't=1345758579X')
        self.assertEqual(len(samples[1].request_headers), 5)
        assert 'Accept-Encoding' in samples[1].request_headers
        self.assertEqual(samples[1].request_headers['Accept-Encoding'],
                'gzip, deflate')
        self.assertEqual(samples[1].response_headers['status_line'],
                'HTTP/1.1 404 Not Found')
        self.assertEqual(len(samples[1].response_headers['headers']), 9)
        assert 'Content-Type' in samples[1].response_headers['headers']
        self.assertEqual(
                samples[1].response_headers['headers']['Content-Type'],
                'text/html; charset=utf-8')
        samples[1] = samples[1]._replace(cookies={},
                request_headers={}, response_data='',
                response_headers={'status_line': '', 'headers': {}})

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
                response_headers={'status_line': '', 'headers': {}},
                response_message='Not Found',
                sample_count=1,
                success=False,
                tag_name='httpSample',
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 21, 49, 40, 553000),
                url='http://www.yahoo.com/some_page',
                )
        self.assertEqual(samples[1], test_sample)

        self.assertEqual(len(samples[2].cookies), 4)
        assert 'B' in samples[2].cookies
        self.assertEqual(samples[2].cookies['B'],
                '5vdh93l83d9cc&b=3&s=bs')
        self.assertEqual(len(samples[2].request_headers), 6)
        assert 'Referer' in samples[2].request_headers
        self.assertEqual(samples[2].request_headers['Referer'],
                'http://search.yahoo.com/search;_ylt=A03uoRrUAfZPg18BCCmbvZx4'
                '?p=potato&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-701')
        self.assertEqual(samples[2].response_headers['status_line'],
                'HTTP/1.1 200 OK')
        self.assertEqual(len(samples[2].response_headers['headers']), 9)
        assert 'Date' in samples[2].response_headers['headers']
        self.assertEqual(samples[2].response_headers['headers']['Date'],
                'Thu, 23 Aug 2012 21:50:06 GMT')
        samples[2] = samples[2]._replace(cookies={},
                request_headers={},
                response_headers={'status_line': '', 'headers': {}})

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
                response_headers={'status_line': '', 'headers': {}},
                response_message='OK',
                sample_count=1,
                success=True,
                tag_name='httpSample',
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 21, 50, 4, 17000),
                url='http://images.search.yahoo.com/search/images;'
                    '_ylt=A0oG7lg2AvZPowgACQNXNyoA?ei=UTF-8&p=potato'
                    '&fr2=tab-web&fr=yfp-t-701',
                )
        self.assertEqual(samples[2], test_sample)

    def test_csv(self):
        """Test CSV parser.

        """
        samples_filename = os.path.join(self.tests_dir,
                'samples/main.csv')
        parser = jtl.create_parser(samples_filename)
        samples = list(parser.itersamples())
        self.assertEqual(len(samples), 3)

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
                response_headers={'status_line': '', 'headers': {}},
                response_message='OK',
                sample_count=1,
                success=True,
                tag_name='',
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 21, 53, 59, 670000),
                url='http://www.yahoo.com/',
                )
        self.assertEqual(samples[0], test_sample)

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
                response_headers={'status_line': '', 'headers': {}},
                response_message='Not Found',
                sample_count=1,
                success=False,
                tag_name='',
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 21, 54, 18, 365000),
                url='http://www.yahoo.com/some_page',
                )
        self.assertEqual(samples[1], test_sample)

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
                response_headers={'status_line': '', 'headers': {}},
                response_message='OK',
                sample_count=1,
                success=True,
                tag_name='',
                thread_name='Thread Group 1-2',
                timestamp=datetime(2012, 8, 23, 21, 54, 33, 601000),
                url='http://images.search.yahoo.com/search/images;'
                    '_ylt=A0oG7lg2AvZPowgACQNXNyoA?ei=UTF-8&p=potato'
                    '&fr2=tab-web&fr=yfp-t-701',
                )
        self.assertEqual(samples[2], test_sample)


if __name__ == '__main__':
    unittest.main()
