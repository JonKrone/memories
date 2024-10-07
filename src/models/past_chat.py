from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Author(BaseModel):
    role: str
    name: Optional[str] = None
    metadata: dict


class Content(BaseModel):
    content_type: str
    parts: List[Union[str, dict]]


class Message(BaseModel):
    id: str
    author: Author
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    content: Content
    status: str
    end_turn: Optional[bool] = None
    weight: float
    metadata: dict
    recipient: str


class MappingEntry(BaseModel):
    id: str
    message: Optional[Message] = None
    parent: Optional[str]
    children: List[str]


class PastChat(BaseModel):
    title: str
    create_time: datetime
    update_time: datetime
    mapping: Dict[str, MappingEntry]
    moderation_results: List[
        dict
    ]  # Assuming this is a list of dictionaries without specific structure
    current_node: str
    plugin_ids: Optional[List[str]] = None
    conversation_id: str
    conversation_template_id: Optional[str] = None
    gizmo_id: Optional[str] = None
    is_archived: bool
    safe_urls: List[str]
    default_model_slug: str
    id: str
