from unittest.mock import MagicMock, call
import pytest

from src.app import actions, models


class TestActions(object):
    @pytest.fixture()
    def mocked_database(self):
        return MagicMock()

    def test_create_new_item_should_call_db_methods(self, mocked_database):
        new_item = actions.create_new_item(db=mocked_database, title="test_title", description="test_description")
        mocked_model = models.Item(title="test_title", description="test_description")

        mocked_database.add.assert_called_once()
        mocked_database.commit.assert_called_once()
        mocked_database.refresh.assert_called_once()

        assert new_item.description == mocked_model.description
        assert new_item.title == mocked_model.title

    def test_get_items_should_call_db_methods(self, mocked_database):
        actions.get_items(db=mocked_database, offset=0, limit=100)

        assert mocked_database.mock_calls[0] == call.query(models.Item)
        assert mocked_database.mock_calls[1] == call.query().offset(0)
        assert mocked_database.mock_calls[2] == call.query().offset().limit(100)
        assert mocked_database.mock_calls[3] == call.query().offset().limit().all()

    def test_get_items_by_id_should_call_db_methods(self, mocked_database):
        actions.get_item_by_id(db=mocked_database, item_id=1)

        assert mocked_database.mock_calls[0] == call.query(models.Item)
        assert mocked_database.mock_calls[2] == call.query().filter().first()

    def test_delete_item_by_id_should_call_db_methods(self, mocked_database):
        actions.delete_item_by_id(db=mocked_database, item_id=1)

        assert mocked_database.mock_calls[2] == call.query().filter().delete(synchronize_session=False)
        mocked_database.commit.assert_called_once()
