from unittest.mock import patch

from app.services.inventory_service import InventoryItem, fetch_item, transfer_item


def describe_fetch_item():
    def it_returns_none_for_nf_prefix():
        result = fetch_item("nf_123")
        assert result is None

    def it_returns_item_for_itm_prefix():
        result = fetch_item("itm_456")
        assert result is not None
        assert isinstance(result, InventoryItem)
        assert result.id == "itm_456"
        assert result.owner_id.startswith("usr_")
        assert len(result.name) > 0

    def it_returns_none_for_unknown_prefix():
        result = fetch_item("xyz_789")
        assert result is None

    def it_generates_unique_owner_ids():
        item_a = fetch_item("itm_a")
        item_b = fetch_item("itm_b")
        assert item_a is not None
        assert item_b is not None
        assert item_a.owner_id != item_b.owner_id


def describe_transfer_item():
    async def it_returns_none():
        with patch("app.services.inventory_service.asyncio.sleep") as mock_sleep:
            result = await transfer_item("itm_1", "usr_new", 100.0)
            assert result is None
            mock_sleep.assert_called_once()
            sleep_time = mock_sleep.call_args[0][0]
            assert 10 <= sleep_time <= 50
