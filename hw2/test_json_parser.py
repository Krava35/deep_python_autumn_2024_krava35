import io
import unittest
import unittest.mock
from json_parser import parse


class TestParser(unittest.TestCase):

    def test_empty(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            out = 'Wrong input type!\n'
            parse(
                None,
                None,
                None,
                lambda key, token: print(f"{key=}, {token=}")
            )
            self.assertEqual(mock_stdout.getvalue(), out)

    def test_wrong_input(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            out = 'Wrong input type!\n'
            parse(
                1,
                2,
                3,
                lambda key, token: print(f"{key=}, {token=}")
            )

            self.assertEqual(mock_stdout.getvalue(), out)

    def test_wrong_keys_input(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            json_string = {"key1": "Word1 word2", "key2": "word2 word3"}
            out = 'Wrong input type!\n'
            parse(
                json_string,
                2,
                3,
                lambda key, token: print(f"{key=}, {token=}")
            )

            self.assertEqual(mock_stdout.getvalue(), out)

    def test_wrong_tokens_input(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            json_string = '{"key1": "Word1 word2", "key2": "word2 word3"}'
            required_keys = ["key1", "KEY2"]
            out = 'Wrong input type!\n'
            parse(
                json_string,
                required_keys,
                3,
                lambda key, token: print(f"{key=}, {token=}")
            )

            self.assertEqual(mock_stdout.getvalue(), out)

    def test_wrong_tokens_with_no_relavant_keys(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            json_string = '{"key1": "Word1 word2", "key2": "word2 word3"}'
            required_keys = ["KEY1", "KEY2"]
            out = ""
            parse(
                json_string,
                required_keys,
                3,
                lambda key, token: print(f"{key=}, {token=}")
            )

            self.assertEqual(mock_stdout.getvalue(), out)

    def test_example(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            json_string = '{"key1": "Word1 word2", "key2": "word2 word3"}'
            required_keys = ["key1", "KEY2"]
            tokens = ["WORD1", "word2"]
            out = ''.join(["key='key1', token='WORD1'\n",
                           "key='key1', token='word2'\n"])

            parse(
                json_string,
                required_keys,
                tokens,
                lambda key, token: print(f"{key=}, {token=}")
            )

            self.assertEqual(mock_stdout.getvalue(), out)

    def test_schedule_1(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            json_string = '{ \
                            "Group": "B1", \
                            "Monday": ["Russian", "Math", "Reading", "Math"], \
                            "Tuesday": ["Math", "Russian", "World Study"], \
                            "Wednesday": ["Russian", "Math", "Reading"], \
                            "Thursday": ["Russian", "Reading", "World Study"], \
                            "Friday": ["Russian", "Math", "Reading"], \
                            "Russian HW": "ex. 30", \
                            "Math HW": "ex. 35", \
                            "Reading HW": "A. S. Pushkins fairy tails", \
                            "World Study HW": "p. 10-12" \
            }'

            required_keys = ["Monday",
                             "Tuesday",
                             "Wednesday",
                             "Thursday",
                             "Friday"]

            tokens = ["Math", "Reading"]

            out = "".join(["key='Monday', token='Math'\n",
                           "key='Monday', token='Reading'\n",
                           "key='Tuesday', token='Math'\n",
                           "key='Wednesday', token='Math'\n",
                           "key='Wednesday', token='Reading'\n",
                           "key='Thursday', token='Reading'\n",
                           "key='Friday', token='Math'\n",
                           "key='Friday', token='Reading'\n"])

            parse(
                json_string,
                required_keys,
                tokens,
                lambda key, token: print(f"{key=}, {token=}")
            )

            self.assertEqual(mock_stdout.getvalue(), out)

    def test_schedule_2(self):
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:

            json_string = '{ \
                            "Group": "B1", \
                            "Monday": ["Russian", "Math", "Reading", "Math"], \
                            "Tuesday": ["Math", "Russian", "World Study"], \
                            "Wednesday": ["Russian", "Math", "Reading"], \
                            "Thursday": ["Russian", "Reading", "World Study"], \
                            "Friday": ["Russian", "Math", "Reading"], \
                            "Russian HW": "ex. 30", \
                            "Math HW": "ex. 35", \
                            "Reading HW": "A. S. Pushkins fairy tails", \
                            "World Study HW": "p. 10-12" \
            }'

            required_keys = ["Group",
                             "Monday",
                             "Friday"]

            tokens = ["b1", "MATH"]

            out = "".join(["key='Group', token='b1'\n",
                           "key='Monday', token='MATH'\n",
                           "key='Friday', token='MATH'\n"])

            parse(
                json_string,
                required_keys,
                tokens,
                lambda key, token: print(f"{key=}, {token=}")
            )

            self.assertEqual(mock_stdout.getvalue(), out)

    def test_schedule_3(self):

        json_string = '{ \
                        "Group": "B1", \
                        "Monday": ["Russian", "Math", "Reading", "Math"], \
                        "Tuesday": ["Math", "Russian", "World Study"], \
                        "Wednesday": ["Russian", "Math", "Reading"], \
                        "Thursday": ["Russian", "Reading", "World Study"], \
                        "Friday": ["Russian", "Math", "Reading"], \
                        "Russian HW": "ex. 30", \
                        "Math HW": "ex. 35", \
                        "Reading HW": "A. S. Pushkins fairy tails", \
                        "World Study HW": "p. 10-12" \
        }'

        required_keys = ["RU HW",
                         "Math HW",
                         "Reading HW",
                         "World Study HW"]

        tokens = ["ex", ".", "0"]

        lst = []
        res = ["key='Math HW', token='ex'",
               "key='Math HW', token='.'",
               "key='Reading HW', token='.'",
               "key='World Study HW', token='.'",
               "key='World Study HW', token='0'"]

        parse(
            json_string,
            required_keys,
            tokens,
            lambda key, token: lst.append(f"{key=}, {token=}")
        )

        self.assertListEqual(res, lst)
