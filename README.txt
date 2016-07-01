python-jtl
==========

python-jtl provides a module called jtl which can be useful for parsing
JMeter results (so called JTL files). JTL files can be either of XML or
CSV (with or without the fieldnames) file format. jtl module supports
both XML and CSV (with and without the fieldnames) file formats.

The typical usage in general looks like this:

::

        from jtl import create_parser

        parser = create_parser('test_results.xml')
        for sample in parser.itersamples():
            ...

Features
--------

-  Parses JMeter results (JTL) into the iterator of the results samples;

-  Supports both XML and CSV (with and without fieldnames) file formats;

-  Supports custom delimiter character (CSV only);

-  Stores results samples in named tuples;

-  Uses iterative XML parsing for better performance;

-  Automatically detects the file format (XML or CSV).
