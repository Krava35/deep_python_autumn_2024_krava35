import unittest
from unittest.mock import patch
from retry_deco import retry_deco


@retry_deco(2)
def empty():
    pass


@retry_deco(3)
def add(a, b):
    return a + b


@retry_deco(5, [IndexError, TypeError])
def insert(area, obj, index=None):
    if index:
        area[index] = obj
    else:
        area.append(obj)
    return area


class TestParser(unittest.TestCase):

    @patch('builtins.print')
    def test_empty(self, mock_print):
        self.assertEqual(None, empty())

        mock_print.assert_any_call("".join(["run 'empty' - ",
                                            "with possitional arguments (); ",
                                            "with keyword kwargs {}:"]))
        mock_print.assert_any_call("    attemp=1 | res=None")

    @patch('builtins.print')
    def test_add_1(self, mock_print):
        self.assertEqual(35, add(30, 5))

        mock_print.assert_any_call("".join(["run 'add' - ",
                                            "with possitional arguments ",
                                            "(30, 5); ",
                                            "with keyword kwargs {}:"]))
        mock_print.assert_any_call("    attemp=1 | res=35")

    @patch('builtins.print')
    def test_add_2(self, mock_print):
        self.assertEqual(30, add(a=10, b=20))

        mock_print.assert_any_call("".join(["run 'add' - ",
                                            "with possitional arguments (); ",
                                            "with keyword kwargs ",
                                            "{'a': 10, 'b': 20}:"]))
        mock_print.assert_any_call("    attemp=1 | res=30")

    @patch('builtins.print')
    def test_add_3(self, mock_print):
        self.assertEqual('Who am I?', add('Who', ' am I?'))

        mock_print.assert_any_call("".join(["run 'add' - ",
                                            "with possitional arguments ",
                                            "('Who', ' am I?'); ",
                                            "with keyword kwargs {}:"]))
        mock_print.assert_any_call("    attemp=1 | res='Who am I?'")

    @patch('builtins.print')
    def test_add_4(self, mock_print):
        self.assertEqual(None, add('I am I', 2044.2043))

        mock_print.assert_any_call("".join(["run 'add' - ",
                                            "with possitional arguments "
                                            "('I am I', 2044.2043); ",
                                            "with keyword kwargs {}:"]))
        mock_print.assert_any_call("    attemp=1 | TypeError")
        mock_print.assert_any_call("    attemp=2 | TypeError")
        mock_print.assert_any_call("    attemp=3 | TypeError")

    @patch('builtins.print')
    def test_insert_1(self, mock_print):
        self.assertEqual([35], insert([], 35))

        mock_print.assert_any_call("".join(["run 'insert' - ",
                                            "with possitional arguments "
                                            "([], 35); ",
                                            "with keyword kwargs {}:"]))
        mock_print.assert_any_call("    attemp=1 | res=[35]")

    @patch('builtins.print')
    def test_insert_2(self, mock_print):
        self.assertEqual(None, insert([1, 2], 3, 2))

        mock_print.assert_any_call("".join(["run 'insert' - ",
                                            "with possitional arguments "
                                            "([1, 2], 3, 2); ",
                                            "with keyword kwargs {}:"]))
        mock_print.assert_any_call("    attemp=1 | IndexError")

    @patch('builtins.print')
    def test_insert_3(self, mock_print):
        self.assertEqual(None, insert(area={1, 2}, obj=3))

        mock_print.assert_any_call("".join(["run 'insert' - ",
                                            "with possitional arguments (); ",
                                            "with keyword kwargs "
                                            "{'area': {1, 2}, 'obj': 3}:"]))
        mock_print.assert_any_call("    attemp=1 | AttributeError")
        mock_print.assert_any_call("    attemp=2 | AttributeError")

    @patch('builtins.print')
    def test_insert_4(self, mock_print):
        self.assertEqual(None, insert(area={1, 2}, obj=3, index=1))

        mock_print.assert_any_call("".join(["run 'insert' - ",
                                            "with possitional arguments (); ",
                                            "with keyword kwargs "
                                            "{'area': {1, 2}, ",
                                            "'obj': 3, ",
                                            "'index': 1}:"]))
        mock_print.assert_any_call("    attemp=1 | TypeError")

    @patch('builtins.print')
    def test_insert_5(self, mock_print):
        self.assertEqual(None, insert(area=None, obj=1, index=0))

        mock_print.assert_any_call("".join(["run 'insert' - ",
                                            "with possitional arguments (); ",
                                            "with keyword kwargs "
                                            "{'area': None, ",
                                            "'obj': 1, ",
                                            "'index': 0}:"]))
        mock_print.assert_any_call("    attemp=1 | AttributeError")
        mock_print.assert_any_call("    attemp=2 | AttributeError")
