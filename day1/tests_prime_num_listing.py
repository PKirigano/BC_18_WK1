import unittest
from prime_num_listing import prime_num_listing


class PrimeNumbersTest(unittest.TestCase):
    """ Test cases for the function to generate prime numbers """

    def test_if_result_is_a_list(self):
        """ Check whether the result is a list """
        result = prime_num_listing(17)
        self.assertTrue(result, list)

    def test_empty_list_if_n_less_than_two(self):
        """ Check whether an empty list is returned if there are no
        prime numbers within the range provided """
        result = prime_num_listing(1)
        self.assertEqual(result, [])

    def test_if_twenty_three_is_prime(self):
        """ Check whether 23 in the list of prime numbers generated """
        result = prime_num_listing(24)
        self.assertIn(17, result)

    def test_no_negative_number_in_primes(self):
        """ Check whether there is no negative values in the generated list"""
        result = prime_num_listing(20)
        self.assertNotIn(-5, result)
        self.assertNotIn(-15, result)
        self.assertNotIn(-19, result)

    def test_no_non_primes_are_returned(self):
        """ Check that the list that is returned does not include numbers
        that are not prime numbers"""
        result = prime_num_listing(32)
        self.assertNotIn(22, result)
        self.assertNotIn(25, result)
        self.assertNotIn(14, result)
        self.assertNotIn(18, result)

    def test_raises_error_if_n_is_list(self):
        """ Check whther an error is raised if n is a list """
        with self.assertRaises(ValueError):
            prime_num_listing([])

    def test_raises_error_if_n_is_a_string(self):
        """ Check whether an error is raised if n is a string """
        with self.assertRaises(ValueError):
            prime_num_listing("n")

if __name__ == "__main__":
unittest.main()