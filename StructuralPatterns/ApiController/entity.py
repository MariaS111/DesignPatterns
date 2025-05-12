from dataclasses import dataclass
from typing import Optional


@dataclass
class SomeEntity:
    id: int
    name: str
    description: str
    status: str


@dataclass
class SomeImageEntity(SomeEntity):
    image_url: Optional[str] = None
