from dataclasses import dataclass, field
from typing import Any, Dict
from components.field import Field

@dataclass
class FieldGroup:
    name: str = "Default"
    fields : Dict[str, Field] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "fields": {key: field_obj.to_dict() for key, field_obj in self.fields.items()}
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FieldGroup":
        group_name = data.get("name", "Default")
        fields_data = data.get("fields", {})
        fields_list = {key: Field.from_dict(field_dict) for key, field_dict in fields_data.items()}
        return cls(name=group_name, fields=fields_list)