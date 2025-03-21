from enum import Enum
import ast

# CURRENTLY UNUSED, NEED TO FINISH OTHER STUFF FIRST

class BoundingBoxType(Enum):
    pass

class DataTypeConverter:
    _converters = {}

    @classmethod
    def register_converter(cls, data_type:str, converter_func):
        cls._converters[data_type] = converter_func

    @classmethod
    def convert(cls, data_type:str, value:any):
        converter = cls._converters.get(data_type, lambda x: x)
        return converter(value)
    
    def convert_float(val):
        return float(val)
    
    def convert_integer(val):
        return int(val)
    
    def convert_boolean(val):
        if isinstance(val, bool):
            return val
        return str(val).lower() in ["true", "1"]
    
    def convert_vector(val):
        if isinstance(val, str):
            try:
                val = ast.literal_eval(val)
            except Exception as e:
                raise ValueError(f"Failed to parse vector: {e}")
        if not isinstance(val, dict):
            raise ValueError("Expected a dictionary for a vector")
        for axis in ("X", "Y", "Z"):
            if axis in val:
                val[axis] = float(val[axis])
        return val
    
    def convert_bounding_box(val):
        if isinstance(val, BoundingBoxType):
            return val
        if isinstance(val, str):
            for member in BoundingBoxType:
                if member.value.lower() == val.lower():
                    return member
        raise ValueError(f"Invalid bounding box type: {val}")
    