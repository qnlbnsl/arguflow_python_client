# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.api.chunk_collection_api import ChunkCollectionApi


class TestChunkCollectionApi(unittest.TestCase):
    """ChunkCollectionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ChunkCollectionApi()

    def tearDown(self) -> None:
        pass

    def test_add_bookmark(self) -> None:
        """Test case for add_bookmark

        add_bookmark
        """
        pass

    def test_create_chunk_collection(self) -> None:
        """Test case for create_chunk_collection

        create_chunk_collection
        """
        pass

    def test_delete_bookmark(self) -> None:
        """Test case for delete_bookmark

        delete_bookmark
        """
        pass

    def test_delete_chunk_collection(self) -> None:
        """Test case for delete_chunk_collection

        delete_chunk_collection
        """
        pass

    def test_get_all_bookmarks(self) -> None:
        """Test case for get_all_bookmarks

        get_all_bookmarks
        """
        pass

    def test_get_collections_chunk_is_in(self) -> None:
        """Test case for get_collections_chunk_is_in

        """
        pass

    def test_get_logged_in_user_chunk_collections(self) -> None:
        """Test case for get_logged_in_user_chunk_collections

        get_current_user_collections
        """
        pass

    def test_get_specific_user_chunk_collections(self) -> None:
        """Test case for get_specific_user_chunk_collections

        get_user_collections
        """
        pass

    def test_search_collections(self) -> None:
        """Test case for search_collections

        collection_search
        """
        pass

    def test_update_chunk_collection(self) -> None:
        """Test case for update_chunk_collection

        update_chunk_collection
        """
        pass


if __name__ == '__main__':
    unittest.main()
