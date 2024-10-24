# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from marzapi.models.node_modify import NodeModify  # noqa: E501

class TestNodeModify(unittest.TestCase):
    """NodeModify unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeModify:
        """Test NodeModify
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeModify`
        """
        model = NodeModify()  # noqa: E501
        if include_optional:
            return NodeModify(
                name = '',
                address = '',
                port = 56,
                api_port = 56,
                usage_coefficient = 1.337,
                status = 'connected'
            )
        else:
            return NodeModify(
        )
        """

    def testNodeModify(self):
        """Test NodeModify"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()