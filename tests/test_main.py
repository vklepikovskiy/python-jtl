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
        self.assertEqual(len(samples), 5)

        sample = samples[0]
        fields_to_replace = {}
        self.assertEqual(len(sample.request_headers), 5)
        assert 'Accept-Language' in sample.request_headers
        self.assertEqual(sample.request_headers['Accept-Language'],
                'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3')
        fields_to_replace['request_headers'] = {}
        self.assertEqual(sample.response_headers['status_line'],
                'HTTP/1.1 200 OK')
        self.assertEqual(len(sample.response_headers['headers']), 12)
        assert 'Server' in sample.response_headers['headers']
        self.assertEqual(sample.response_headers['headers']['Server'],
                'YTS/1.20.10')
        fields_to_replace['response_headers'] = {
                'status_line': '', 'headers': {}}
        sample = sample._replace(**fields_to_replace)

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
                children=(),
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
        self.assertEqual(sample, test_sample)

        test_sample = jtl.Sample(
                all_threads=2,
                assertion_results=(),
                bytes_received=64189,
                children=(),
                cookies={},
                data_encoding='',
                data_type='',
                elapsed_time=timedelta(0, 1, 359000),
                error_count=0,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='Transaction Controller',
                latency_time=timedelta(0, 0, 802000),
                method='',
                query_string='',
                request_headers={},
                response_code='',
                response_data='',
                response_filename='',
                response_headers={'status_line': '', 'headers': {}},
                response_message='Number of samples in transaction : 1, '
                    'number of failing samples : 0',
                sample_count=1,
                success=False,
                tag_name='sample',
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 8, 23, 21, 49, 30, 542000),
                url='',
                )
        self.assertEqual(samples[1], test_sample)

        sample = samples[2]
        fields_to_replace = {}
        self.assertEqual(len(sample.cookies), 7)
        assert 'MSC' in sample.cookies
        self.assertEqual(sample.cookies['MSC'], 't=1345758579X')
        fields_to_replace['cookies'] = {}
        self.assertEqual(len(sample.request_headers), 5)
        assert 'Accept-Encoding' in sample.request_headers
        self.assertEqual(sample.request_headers['Accept-Encoding'],
                'gzip, deflate')
        fields_to_replace['request_headers'] = {}
        hash = hashlib.md5(sample.response_data.encode('utf-8')).hexdigest()
        self.assertEqual(hash, '1d6165ad17ce4278351db7c3993c097f')
        fields_to_replace['response_data'] = ''
        self.assertEqual(sample.response_headers['status_line'],
                'HTTP/1.1 404 Not Found')
        self.assertEqual(len(sample.response_headers['headers']), 9)
        assert 'Content-Type' in sample.response_headers['headers']
        self.assertEqual(sample.response_headers['headers']['Content-Type'],
                'text/html; charset=utf-8')
        fields_to_replace['response_headers'] = {
                'status_line': '', 'headers': {}}
        sample = sample._replace(**fields_to_replace)

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
                children=(),
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
        self.assertEqual(sample, test_sample)

        sample = samples[3]
        fields_to_replace = {}
        self.assertEqual(len(sample.cookies), 4)
        assert 'B' in sample.cookies
        self.assertEqual(sample.cookies['B'], '5vdh93l83d9cc&b=3&s=bs')
        fields_to_replace['cookies'] = {}
        self.assertEqual(len(sample.request_headers), 6)
        assert 'Referer' in sample.request_headers
        self.assertEqual(sample.request_headers['Referer'],
                'http://search.yahoo.com/search;_ylt=A03uoRrUAfZPg18BCCmbvZx4'
                '?p=potato&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-701')
        fields_to_replace['request_headers'] = {}
        self.assertEqual(sample.response_headers['status_line'],
                'HTTP/1.1 200 OK')
        self.assertEqual(len(sample.response_headers['headers']), 9)
        assert 'Date' in sample.response_headers['headers']
        self.assertEqual(sample.response_headers['headers']['Date'],
                'Thu, 23 Aug 2012 21:50:06 GMT')
        fields_to_replace['response_headers'] ={
                'status_line': '', 'headers': {}}
        sample = sample._replace(**fields_to_replace)

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
                children=(),
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
        self.assertEqual(sample, test_sample)

        self.assertEqual(len(samples[4].children), 2)

        sample = samples[4].children[0]
        fields_to_replace = {}
        self.assertEqual(len(sample.cookies), 3)
        assert 'CH' in sample.cookies
        self.assertEqual(sample.cookies['CH'],
                'AgBQnmwQACQFEAAhVBAABrQQABfREAApVRAAIxwQACxvEAA17xAAMJkQABGv')
        fields_to_replace['cookies'] = {}
        self.assertEqual(len(sample.request_headers), 6)
        assert 'Accept-Encoding' in sample.request_headers
        self.assertEqual(sample.request_headers['Accept-Encoding'],
                'gzip, deflate')
        fields_to_replace['request_headers'] = {}
        hash = hashlib.md5(sample.response_data.encode('utf-8')).hexdigest()
        self.assertEqual(hash, 'bfc949a307bf6b89f1e74f343e313eeb')
        fields_to_replace['response_data'] = ''
        self.assertEqual(sample.response_headers['status_line'],
                'HTTP/1.1 200 OK')
        self.assertEqual(len(sample.response_headers['headers']), 10)
        assert 'Keep-Alive' in sample.response_headers['headers']
        self.assertEqual(sample.response_headers['headers']['Keep-Alive'],
                'timeout=60, max=100')
        fields_to_replace['response_headers'] = {
                'status_line': '', 'headers': {}}
        sample = sample._replace(**fields_to_replace)

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
                bytes_received=22073,
                children=(),
                cookies={},
                data_encoding='UTF-8',
                data_type='text',
                elapsed_time=timedelta(0, 1, 401000),
                error_count=0,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='/search;_ylt=A03uoRrUAfZPg18BCCmbvZx4',
                latency_time=timedelta(0, 0, 604000),
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
                timestamp=datetime(2012, 11, 10, 15, 2, 27, 692000),
                url='http://search.yahoo.com/search;_ylt=A03uoRrUAfZPg18BCC'
                    'mbvZx4?p=potato&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-701',
                )
        self.assertEqual(sample, test_sample)

        sample = samples[4].children[1]
        fields_to_replace = {}
        self.assertEqual(len(sample.cookies), 4)
        assert 'sSN' in sample.cookies
        self.assertEqual(sample.cookies['sSN'], 'Xj.um6U2wWEq3sFr6VoZpaSDPhht'
                'y3fGDJ3cvewGeS9SkHOCAXsQjZwDs.T51.GdechtOO0X3bfVvZ6PGRbWhQ--')
        fields_to_replace['cookies'] = {}
        self.assertEqual(len(sample.request_headers), 6)
        assert 'User-Agent' in sample.request_headers
        self.assertEqual(sample.request_headers['User-Agent'],
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 '
                'Firefox/13.0.1')
        fields_to_replace['request_headers'] = {}
        hash = hashlib.md5(sample.response_data.encode('utf-8')).hexdigest()
        self.assertEqual(hash, '30ac686ee464f6cb415a616c2013e63f')
        fields_to_replace['response_data'] = ''
        self.assertEqual(sample.response_headers['status_line'],
                'HTTP/1.1 200 OK')
        self.assertEqual(len(sample.response_headers['headers']), 10)
        assert 'Set-Cookie' in sample.response_headers['headers']
        self.assertEqual(sample.response_headers['headers']['Set-Cookie'],
                'jr=1; path=/')
        fields_to_replace['response_headers'] = {
                'status_line': '', 'headers': {}}
        sample = sample._replace(**fields_to_replace)

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
                bytes_received=21759,
                children=(),
                cookies={},
                data_encoding='UTF-8',
                data_type='text',
                elapsed_time=timedelta(0, 1, 364000),
                error_count=0,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='/search/images;_ylt=A0oG7lg2AvZPowgACQNXNyoA',
                latency_time=timedelta(0, 1, 36000),
                method='GET',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers={'headers': {}, 'status_line': ''},
                response_message='OK',
                sample_count=1,
                success=True,
                tag_name='httpSample',
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 11, 10, 15, 2, 29, 96000),
                url='http://images.search.yahoo.com/search/images;_ylt=A0oG7'
                    'lg2AvZPowgACQNXNyoA?ei=UTF-8&p=potato&fr2=tab-web&fr=yf'
                    'p-t-701',
                )
        self.assertEqual(sample, test_sample)

        sample = samples[4]._replace(children=())
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
                        failure=True,
                        failure_message='Test failed: message expected to '
                            'equal /\n\n****** received  : [[[Number of '
                            'samples in transaction : 2, number of failing '
                            'samples : 0]]]\n\n****** comparison: [[[OK                                                                 ]]]'
                            '\n\n/',
                        name='Response Assertion',
                        ),
                    ),
                bytes_received=43832,
                children=(),
                cookies={},
                data_encoding='',
                data_type='',
                elapsed_time=timedelta(0, 2, 769000),
                error_count=1,
                group_threads=2,
                hostname='hppc',
                idle_time=timedelta(0),
                label='Transaction Controller Search',
                latency_time=timedelta(0),
                method='',
                query_string='',
                request_headers={},
                response_code='200',
                response_data='',
                response_filename='',
                response_headers={'headers': {}, 'status_line': ''},
                response_message='Number of samples in transaction : 2, '
                    'number of failing samples : 0',
                sample_count=1,
                success=False,
                tag_name='sample',
                thread_name='Thread Group 1-1',
                timestamp=datetime(2012, 11, 10, 15, 2, 27, 691000),
                url='',
                )
        self.assertEqual(sample, test_sample)

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
                children=(),
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
                children=(),
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
                children=(),
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
