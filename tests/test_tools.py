#!/usr/bin/env python


import unittest
import imp

tools = imp.load_source('tools', '../tools.py')


class Testconnections(unittest.TestCase):

    def setUp(self):
        self.test_instance = tools.Connections()

    def test_is_active(self):
        pass

    def test_parse_response(self):
        pass

    def test_post(self):
        pass


class Testdatabase_helper(unittest.TestCase):

    def setUp(self):
        self.test_instance = toolset.database_helper()


if __name__ == '__main__':
    unittest.main()
