import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from spring.cloud.dataflow import components

class TestTypes(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0, os.path.abspath('..'))

    def testReflection(self):
        processor = components.Processor()
        for (k,v) in processor.__dict__.iteritems() :

            print k,v

    def testCreateSink(self):
        sink = components.Sink()
        self.assertEquals(components.BindingTarget, sink.input.__class__)

    def testCreateSource(self):
        source = components.Source()
        self.assertEquals(components.BindingTarget, source.output.__class__)


    def testCreateSource(self):
        processor = components.Processor()
        self.assertEquals(components.BindingTarget, processor.input.__class__)
        self.assertEquals('input', processor.input.name)
        self.assertEquals('input', processor.input.type)
        self.assertEquals(components.BindingTarget, processor.output.__class__)
        self.assertEquals('output', processor.output.name)
        self.assertEquals('output', processor.output.type)