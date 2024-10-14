import unittest
from custom_list import CustomList


# pylint: disable=too-many-instance-attributes
class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.custom_list_0 = CustomList([])
        self.custom_list_1 = CustomList([1])
        self.custom_list_2 = CustomList([1, 2])
        self.custom_list_3 = CustomList([1, 2, 3])
        self.custom_list_4 = CustomList([1, 2, 3, 4])
        self.custom_list_5 = CustomList([1, 2, 3, 4, 5])

        self.list_0 = []
        self.list_1 = [5]
        self.list_2 = [5, 4]
        self.list_3 = [5, 4, 3]

        self.int_0 = 0
        self.int_1 = 3
        self.int_2 = -3

    def test_add_with_custom_lists(self):
        result = self.custom_list_0 + self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_0 + self.custom_list_1
        self.assertEqual(result, CustomList([1]))

        result = self.custom_list_1 + self.custom_list_1
        self.assertEqual(result, CustomList([2]))

        result = self.custom_list_1 + self.custom_list_2
        self.assertEqual(result, CustomList([2, 2]))

        result = self.custom_list_2 + self.custom_list_2
        self.assertEqual(result, CustomList([2, 4]))

        result = self.custom_list_2 + self.custom_list_3
        self.assertEqual(result, CustomList([2, 4, 3]))

        result = self.custom_list_4 + self.custom_list_3
        self.assertEqual(result, CustomList([2, 4, 6, 4]))

        result = self.custom_list_5 + self.custom_list_3
        self.assertEqual(result, CustomList([2, 4, 6, 4, 5]))

        result = self.custom_list_5 + self.custom_list_5
        self.assertEqual(result, CustomList([2, 4, 6, 8, 10]))

    def test_add_with_list_and_custom_list(self):
        result = self.list_0 + self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.list_0 + self.custom_list_3
        self.assertEqual(result, CustomList([1, 2, 3]))

        result = self.list_1 + self.custom_list_1
        self.assertEqual(result, CustomList([6]))

        result = self.list_1 + self.custom_list_3
        self.assertEqual(result, CustomList([6, 2, 3]))

        result = self.list_2 + self.custom_list_1
        self.assertEqual(result, CustomList([6, 4]))

        result = self.list_2 + self.custom_list_2
        self.assertEqual(result, CustomList([6, 6]))

        result = self.list_2 + self.custom_list_3
        self.assertEqual(result, CustomList([6, 6, 3]))

    def test_add_with_custom_list_and_list(self):
        result = self.custom_list_0 + self.list_0
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_3 + self.list_0
        self.assertEqual(result, CustomList([1, 2, 3]))

        result = self.custom_list_1 + self.list_1
        self.assertEqual(result, CustomList([6]))

        result = self.custom_list_3 + self.list_1
        self.assertEqual(result, CustomList([6, 2, 3]))

        result = self.custom_list_1 + self.list_2
        self.assertEqual(result, CustomList([6, 4]))

        result = self.custom_list_2 + self.list_2
        self.assertEqual(result, CustomList([6, 6]))

        result = self.custom_list_3 + self.list_2
        self.assertEqual(result, CustomList([6, 6, 3]))

    def test_add_with_int_and_custom_list(self):
        result = self.int_0 + self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.int_1 + self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.int_2 + self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.int_0 + self.custom_list_1
        self.assertEqual(result, CustomList([1]))

        result = self.int_0 + self.custom_list_2
        self.assertEqual(result, CustomList([1, 2]))

        result = self.int_1 + self.custom_list_1
        self.assertEqual(result, CustomList([4]))

        result = self.int_1 + self.custom_list_2
        self.assertEqual(result, CustomList([4, 5]))

        result = self.int_2 + self.custom_list_1
        self.assertEqual(result, CustomList([-2]))

        result = self.int_2 + self.custom_list_2
        self.assertEqual(result, CustomList([-2, -1]))

    def test_add_with_custom_list_and_int(self):
        result = self.custom_list_0 + self.int_0
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_0 + self.int_1
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_0 + self.int_2
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_1 + self.int_0
        self.assertEqual(result, CustomList([1]))

        result = self.custom_list_2 + self.int_0
        self.assertEqual(result, CustomList([1, 2]))

        result = self.custom_list_1 + self.int_1
        self.assertEqual(result, CustomList([4]))

        result = self.custom_list_2 + self.int_1
        self.assertEqual(result, CustomList([4, 5]))

        result = self.custom_list_1 + self.int_2
        self.assertEqual(result, CustomList([-2]))

        result = self.custom_list_2 + self.int_2
        self.assertEqual(result, CustomList([-2, -1]))

    def test_sub_with_custom_lists(self):
        result = self.custom_list_0 - self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_0 - self.custom_list_1
        self.assertEqual(result, CustomList([-1]))

        result = self.custom_list_1 - self.custom_list_0
        self.assertEqual(result, CustomList([1]))

        result = self.custom_list_1 - self.custom_list_1
        self.assertEqual(result, CustomList([0]))

        result = self.custom_list_1 - self.custom_list_2
        self.assertEqual(result, CustomList([0, -2]))

        result = self.custom_list_2 - self.custom_list_1
        self.assertEqual(result, CustomList([0, 2]))

        result = self.custom_list_2 - self.custom_list_2
        self.assertEqual(result, CustomList([0, 0]))

        result = self.custom_list_2 - self.custom_list_3
        self.assertEqual(result, CustomList([0, 0, -3]))

        result = self.custom_list_3 - self.custom_list_2
        self.assertEqual(result, CustomList([0, 0, 3]))

        result = self.custom_list_3 - self.custom_list_4
        self.assertEqual(result, CustomList([0, 0, 0, -4]))

        result = self.custom_list_4 - self.custom_list_3
        self.assertEqual(result, CustomList([0, 0, 0, 4]))

        result = self.custom_list_3 - self.custom_list_5
        self.assertEqual(result, CustomList([0, 0, 0, -4, -5]))

        result = self.custom_list_5 - self.custom_list_3
        self.assertEqual(result, CustomList([0, 0, 0, 4, 5]))

    def test_sub_with_list_and_custom_list(self):
        result = self.list_0 - self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.list_0 - self.custom_list_3
        self.assertEqual(result, CustomList([-1, -2, -3]))

        result = self.list_1 - self.custom_list_1
        self.assertEqual(result, CustomList([4]))

        result = self.list_1 - self.custom_list_3
        self.assertEqual(result, CustomList([4, -2, -3]))

        result = self.list_2 - self.custom_list_1
        self.assertEqual(result, CustomList([4, 4]))

        result = self.list_2 - self.custom_list_2
        self.assertEqual(result, CustomList([4, 2]))

        result = self.list_2 - self.custom_list_3
        self.assertEqual(result, CustomList([4, 2, -3]))

    def test_sub_with_custom_list_and_list(self):
        result = self.custom_list_0 - self.list_0
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_3 - self.list_0
        self.assertEqual(result, CustomList([1, 2, 3]))

        result = self.custom_list_1 - self.list_1
        self.assertEqual(result, CustomList([-4]))

        result = self.custom_list_3 - self.list_1
        self.assertEqual(result, CustomList([-4, 2, 3]))

        result = self.custom_list_1 - self.list_2
        self.assertEqual(result, CustomList([-4, -4]))

        result = self.custom_list_2 - self.list_2
        self.assertEqual(result, CustomList([-4, -2]))

        result = self.custom_list_3 - self.list_2
        self.assertEqual(result, CustomList([-4, -2, 3]))

    def test_sub_with_int_and_custom_list(self):
        result = self.int_0 - self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.int_1 - self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.int_2 - self.custom_list_0
        self.assertEqual(result, CustomList([]))

        result = self.int_0 - self.custom_list_1
        self.assertEqual(result, CustomList([-1]))

        result = self.int_0 - self.custom_list_2
        self.assertEqual(result, CustomList([-1, -2]))

        result = self.int_1 - self.custom_list_1
        self.assertEqual(result, CustomList([2]))

        result = self.int_1 - self.custom_list_2
        self.assertEqual(result, CustomList([2, 1]))

        result = self.int_2 - self.custom_list_1
        self.assertEqual(result, CustomList([-4]))

        result = self.int_2 - self.custom_list_2
        self.assertEqual(result, CustomList([-4, -5]))

    def test_sub_with_custom_list_and_int(self):
        result = self.custom_list_0 - self.int_0
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_0 - self.int_1
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_0 - self.int_2
        self.assertEqual(result, CustomList([]))

        result = self.custom_list_1 - self.int_0
        self.assertEqual(result, CustomList([1]))

        result = self.custom_list_2 - self.int_0
        self.assertEqual(result, CustomList([1, 2]))

        result = self.custom_list_1 - self.int_1
        self.assertEqual(result, CustomList([-2]))

        result = self.custom_list_2 - self.int_1
        self.assertEqual(result, CustomList([-2, -1]))

        result = self.custom_list_1 - self.int_2
        self.assertEqual(result, CustomList([4]))

        result = self.custom_list_2 - self.int_2
        self.assertEqual(result, CustomList([4, 5]))

    def test_equal(self):
        self.assertTrue(self.custom_list_3 == CustomList([1, 1, 1, 1, 2]))
        self.assertTrue(self.custom_list_3 == CustomList([3, 0, 3, 0]))
        self.assertTrue(self.custom_list_3 == CustomList([1, 3, 2]))
        self.assertTrue(self.custom_list_3 == CustomList([3, 3]))
        self.assertTrue(self.custom_list_3 == CustomList([6]))

        self.assertFalse(self.custom_list_3 == CustomList([7]))
        self.assertFalse(self.custom_list_3 == CustomList([2, 3]))
        self.assertFalse(self.custom_list_3 == CustomList([1, 2, -3]))

        self.assertFalse(self.custom_list_3 == 3)
        self.assertFalse(self.custom_list_3 == [3, 3])

    def test_not_equal(self):
        self.assertTrue(self.custom_list_3 != CustomList([1, 1, 1, 1, 1]))
        self.assertTrue(self.custom_list_3 != CustomList([3, 3, 3, 3]))
        self.assertTrue(self.custom_list_3 != CustomList([3, 3, 3]))
        self.assertTrue(self.custom_list_3 != CustomList([-3, -3]))
        self.assertTrue(self.custom_list_3 != CustomList([-6]))

        self.assertFalse(self.custom_list_3 != CustomList([6]))
        self.assertFalse(self.custom_list_3 != CustomList([3, 3]))
        self.assertFalse(self.custom_list_3 != CustomList([3, 3, 0]))

        self.assertFalse(self.custom_list_3 != 3)
        self.assertFalse(self.custom_list_3 != [-3, 3])

    def test_greater_than(self):
        self.assertTrue(self.custom_list_3 > CustomList([3, 3, -3, -3, 3]))
        self.assertTrue(self.custom_list_3 > CustomList([3, 3, -3, -3]))
        self.assertTrue(self.custom_list_3 > CustomList([3, 3, -3]))
        self.assertTrue(self.custom_list_3 > CustomList([-3, -9]))
        self.assertTrue(self.custom_list_3 > CustomList([1]))

        self.assertFalse(self.custom_list_3 > CustomList([6]))
        self.assertFalse(self.custom_list_3 > CustomList([3, 3]))
        self.assertFalse(self.custom_list_3 > CustomList([1, 2, 4]))

        self.assertFalse(self.custom_list_3 > 3)
        self.assertFalse(self.custom_list_3 > [7, 7, 7])

    def test_greater_or_equal(self):
        self.assertTrue(self.custom_list_3 >= CustomList([3, 0, -3, 3, 3]))
        self.assertTrue(self.custom_list_3 >= CustomList([3, 3, -3, 0]))
        self.assertTrue(self.custom_list_3 >= CustomList([3, 3, -1]))
        self.assertTrue(self.custom_list_3 >= CustomList([3, 3]))
        self.assertTrue(self.custom_list_3 >= CustomList([6]))

        self.assertFalse(self.custom_list_3 >= CustomList([7]))
        self.assertFalse(self.custom_list_3 >= CustomList([3, 9]))
        self.assertFalse(self.custom_list_3 >= CustomList([1, 2, 9]))

        self.assertFalse(self.custom_list_3 >= 7)
        self.assertFalse(self.custom_list_3 >= [-7, -7, -7])

    def test_lesser_than(self):
        self.assertTrue(self.custom_list_3 < CustomList([3, 3, 3, 3, 3]))
        self.assertTrue(self.custom_list_3 < CustomList([3, 3, 3, 3]))
        self.assertTrue(self.custom_list_3 < CustomList([3, 3, 3]))
        self.assertTrue(self.custom_list_3 < CustomList([3, 4]))
        self.assertTrue(self.custom_list_3 < CustomList([7]))

        self.assertFalse(self.custom_list_3 < CustomList([6]))
        self.assertFalse(self.custom_list_3 < CustomList([1, 2]))
        self.assertFalse(self.custom_list_3 < CustomList([1, 2, 3]))

        self.assertFalse(self.custom_list_3 < 7)
        self.assertFalse(self.custom_list_3 < [-7, -7, -7])

    def test_lesser_or_equal(self):
        self.assertTrue(self.custom_list_3 <= CustomList([3, 3, 3, 3, -3]))
        self.assertTrue(self.custom_list_3 <= CustomList([3, 3, 3, -3]))
        self.assertTrue(self.custom_list_3 <= CustomList([3, 3, 3]))
        self.assertTrue(self.custom_list_3 <= CustomList([3, 3]))
        self.assertTrue(self.custom_list_3 <= CustomList([6]))

        self.assertFalse(self.custom_list_3 <= CustomList([5]))
        self.assertFalse(self.custom_list_3 <= CustomList([1, 2]))
        self.assertFalse(self.custom_list_3 <= CustomList([1, 2, -3]))

        self.assertFalse(self.custom_list_3 <= 7)
        self.assertFalse(self.custom_list_3 <= [-7, -7, -7])

    def test_to_string(self):
        self.assertEqual(str(self.custom_list_0), "[], sum: 0")
        self.assertEqual(str(self.custom_list_1), "[1], sum: 1")
        self.assertEqual(str(self.custom_list_2), "[1, 2], sum: 3")
        self.assertEqual(str(self.custom_list_3), "[1, 2, 3], sum: 6")
        self.assertEqual(str(self.custom_list_4), "[1, 2, 3, 4], sum: 10")
        self.assertEqual(str(self.custom_list_5), "[1, 2, 3, 4, 5], sum: 15")
