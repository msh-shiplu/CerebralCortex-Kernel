from .context import CerebralCortex

import unittest

class BasicTestSuite(unittest.TestCase):

    def test_cc_creation(self):
        cc = CerebralCortex()
        print(cc)
        assert True


if __name__ == '__main__':
    unittest.main()