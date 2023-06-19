import unittest

from unit_test_universal_object import TestNonce, TestNumericNonce, TestUniversalObject
from unit_test_verified_object import TestVerifiedObject


def main():
    # Load test suites
    test_nonce_suite = unittest.TestLoader().loadTestsFromTestCase(TestNonce)
    test_universal_object_suite = unittest.TestLoader().loadTestsFromTestCase(TestUniversalObject)
    test_verified_object_suite = unittest.TestLoader().loadTestsFromTestCase(TestVerifiedObject)
    
    # Run test suites
    unittest.TextTestRunner(verbosity=2).run(test_nonce_suite)
    unittest.TextTestRunner(verbosity=2).run(test_universal_object_suite)
    unittest.TextTestRunner(verbosity=2).run(test_verified_object_suite)


if __name__ == '__main__':
    main()
