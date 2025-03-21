from dataclasses import dataclass, field
from typing import Dict, Any
from components.field_group import FieldGroup

@dataclass
class Tab:
    name: str = "New Tab"
    groups : Dict[str, FieldGroup] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "groups": {group_name: group.to_dict() for group_name, group in self.groups.items()}
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Tab":
        tab = cls(name=data.get("name", "New Tab"))
        groups_data = data.get("groups", {})
        for group_name, group_dict in groups_data.items():
            tab.groups[group_name] = FieldGroup.from_dict(group_dict)
        return tab
    

    