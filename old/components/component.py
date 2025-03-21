from dataclasses import dataclass, field
from typing import Any, Dict
import json
from enum import Enum
from components.tab import Tab

class ComponentType(Enum):
    CHR = "chr"
    BOT = "bot"
    DODGE = "dodge"

@dataclass
class Component:
    name: str = "New Component" # edit this later
    type: ComponentType = ComponentType.CHR
    tabs: dict[str, Tab] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.type.value,
            "tabs": {tab_name: tab.to_dict() for tab_name, tab in self.tabs.items()}
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Component":
        comp = cls(
            name=data.get("name", "New Component"),
            type=ComponentType(data.get("type", "chr"))
        )
        tabs_data = data.get("tabs", {})
        for tab_name, tab_dict in tabs_data.items():
            comp.tabs[tab_name] = Tab.from_dict(tab_dict)
        return comp

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    @classmethod
    def from_json(cls, filename: str) -> "Component":
        data = json.loads(filename)
        return cls.from_dict(data)


    