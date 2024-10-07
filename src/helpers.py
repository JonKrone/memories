import json
from typing import List

from pydantic import parse_obj_as

from src.models.past_chat import PastChat

# from models.past_chat import PastChat


def load_conversations(path: str) -> List[PastChat]:
    with open(path, "r") as f:
        return json.load(f)


def parse_conversation(conversation: dict) -> PastChat:
    return parse_obj_as(PastChat, conversation)


async def process_conversation(conversation: dict):
    past_chat = parse_conversation(conversation)

    simple_chat = await simplify_past_chat(past_chat)


async def process_conversations(path: str, number: int):
    data = load_conversations(path)

    for conversation in data[:number]:
        await process_conversation(conversation)


# This simplifies the PastChat model by denormalizing it's messages and pruning unnecessary fields.
def simplify_past_chat(past_chat: PastChat):
    return {
        "title": past_chat.title,
        "create_time": past_chat.create_time,
        "update_time": past_chat.update_time,
        "mapping": past_chat.mapping,
        # "moderation_results": past_chat.moderation_results,
        # "current_node": past_chat.current_node,
        # "plugin_ids": past_chat.plugin_ids,
        "conversation_id": past_chat.conversation_id,
        "conversation_template_id": past_chat.conversation_template_id,
        "is_archived": past_chat.is_archived,
        "id": past_chat.id,
    }
