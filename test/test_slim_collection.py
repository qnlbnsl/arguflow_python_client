# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.slim_collection import SlimCollection

class TestSlimCollection(unittest.TestCase):
    """SlimCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlimCollection:
        """Test SlimCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlimCollection`
        """
        model = SlimCollection()
        if include_optional:
            return SlimCollection(
                author_id = '',
                id = '',
                name = '',
                of_current_user = True
            )
        else:
            return SlimCollection(
                author_id = '',
                id = '',
                name = '',
                of_current_user = True,
        )
        """

    def testSlimCollection(self):
        """Test SlimCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
