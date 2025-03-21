from dataclasses import dataclass, field
from typing import Any, Optional
import ast

@dataclass
class Field:
    in_file_name: str = "InFileName"
    in_game_name: str = "In Game Name"
    data_type: str = "string"
    parent: Optional[str] = None
    _value: Any = field(default=None, repr=False)

    def __post_init__(self):
        if self._value is None:
            if self.data_type == "integer":
                self.value = 0
            elif self.data_type == "float":
                self.value = 0.0
            elif self.data_type == "vector":
                self.value = {"X": 0.0, "Y": 0.0, "Z": 0.0}
            else:
                self.value = ""

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        if self.data_type == "float":
            try:
                self._value = float(new_value)
            except (ValueError, TypeError):
                raise ValueError(f"Field '{self.in_game_name}' expects a float value.")
        elif self.data_type == "vector":
            # If new_value is a string, try to parse it into a dict.
            if isinstance(new_value, str):
                try:
                    new_value = ast.literal_eval(new_value)
                except Exception as e:
                    raise ValueError(f"Field '{self.in_game_name}' could not parse the vector value: {e}")
            if not isinstance(new_value, dict):
                raise ValueError(f"Field '{self.in_game_name}' expects a dictionary for a vector value.")
            for axis in ("X", "Y", "Z"):
                if axis in new_value:
                    try:
                        new_value[axis] = float(new_value[axis])
                    except (ValueError, TypeError):
                        raise ValueError(f"Field '{self.in_game_name}' expects a numeric value for {axis}.")
            self._value = new_value
        else:
            self._value = new_value

    def validate(self) -> None:
        self.value = self.value

    
    def to_dict(self) -> dict:
        return {
            "in_file_name": self.in_file_name,
            "in_game_name": self.in_game_name,
            "data_type": self.data_type,
            "parent": self.value,
            "value": self._value
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Field":
        instance = cls(
            in_game_name=data.get("in_game_name", "New Field"),
            data_type=data.get("data_type", "string"),
            parent=data.get("parent")
        )
        instance.value = data.get("value")
        return instance
    
   

    