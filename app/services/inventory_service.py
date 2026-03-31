import asyncio
import random
import uuid
from dataclasses import dataclass

from faker import Faker

fake = Faker()


@dataclass
class InventoryItem:
    id: str
    owner_id: str
    name: str


def fetch_item(item_id: str) -> InventoryItem | None:
    if item_id.startswith("nf_"):
        return None

    if item_id.startswith("itm_"):
        adjective = fake.word(ext_word_list=None)
        obj = fake.word(ext_word_list=None)
        return InventoryItem(
            id=item_id,
            owner_id=f"usr_{uuid.uuid4()}",
            name=f"{adjective} {obj}",
        )

    return None


async def transfer_item(item_id: str, new_owner_id: str, price: float) -> None:
    sleep_time = random.uniform(10, 50)
    await asyncio.sleep(sleep_time)
