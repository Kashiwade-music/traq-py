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

from traq.models.user_stats_stamp import UserStatsStamp

class TestUserStatsStamp(unittest.TestCase):
    """UserStatsStamp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserStatsStamp:
        """Test UserStatsStamp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserStatsStamp`
        """
        model = UserStatsStamp()
        if include_optional:
            return UserStatsStamp(
                id = '',
                count = 56,
                total = 56
            )
        else:
            return UserStatsStamp(
                id = '',
                count = 56,
                total = 56,
        )
        """

    def testUserStatsStamp(self):
        """Test UserStatsStamp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
