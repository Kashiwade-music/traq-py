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

from traq.models.channel_stats import ChannelStats

class TestChannelStats(unittest.TestCase):
    """ChannelStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelStats:
        """Test ChannelStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelStats`
        """
        model = ChannelStats()
        if include_optional:
            return ChannelStats(
                total_message_count = 56,
                stamps = [
                    traq.models.channel_stats_stamp.ChannelStatsStamp(
                        id = '', 
                        count = 56, 
                        total = 56, )
                    ],
                users = [
                    traq.models.channel_stats_user.ChannelStatsUser(
                        id = '', 
                        message_count = 56, )
                    ],
                datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ChannelStats(
                total_message_count = 56,
                stamps = [
                    traq.models.channel_stats_stamp.ChannelStatsStamp(
                        id = '', 
                        count = 56, 
                        total = 56, )
                    ],
                users = [
                    traq.models.channel_stats_user.ChannelStatsUser(
                        id = '', 
                        message_count = 56, )
                    ],
                datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testChannelStats(self):
        """Test ChannelStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
