# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from traq.models.stamp_stats import StampStats

class TestStampStats(unittest.TestCase):
    """StampStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StampStats:
        """Test StampStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StampStats`
        """
        model = StampStats()
        if include_optional:
            return StampStats(
                count = 56,
                total_count = 56
            )
        else:
            return StampStats(
                count = 56,
                total_count = 56,
        )
        """

    def testStampStats(self):
        """Test StampStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
