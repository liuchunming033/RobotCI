'''
Created on Jan 12, 2015

@author: liu.chunming
'''
import widget
import unittest

class TestWidgetTestCase(unittest.TestCase):
    
    def setUp(self):
        self.widget = widget.Widget()
    
    def test_getSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))
    
    def tearDown(self):
        self.widget = None
     
if __name__ == '__main__':
    unittest.main()
