
import os
from abc import ABC, abstractmethod
from components.chr_schema import ChrSchema
from components.component import Component, ComponentType

class ComponentParser(ABC):
    @abstractmethod
    def load(self, filepath:str) -> Component:
        pass

    @abstractmethod
    def dump(self, component: Component, filepath:str) -> None:
        pass

class JSONComponentParser(ComponentParser):
    def load(self, filepath:str) -> Component:
        with open(filepath, 'r') as file:
            json_str = file.read()
        return Component.from_json(json_str)
    
    def dump(self, component: Component, filepath:str) -> None:
        with open(filepath, 'w') as file:
            file.write(component.to_json())

class RawComponentParser(ComponentParser):
    EXTENSION_MAP = {
        ".chr": ComponentType.CHR,
        ".bot": ComponentType.BOT,
        ".dodge": ComponentType.DODGE,
    }

    def load(self, filepath:str) -> Component:
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()
        if ext == ".chr":
            component = ChrSchema.chr_schema()
        # write else condiiton later
    
        default_name = os.path.splitext(os.path.basename(filepath))[0]
        component.name = default_name

        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("//"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=",1)
                key = key.strip()
                value = value.strip()

                if key.lower() == "name":
                    if component.name == default_name or not component.name: # had to write this to prevent blank names
                        component.name = value
                else:
                    updated = False
                    for tab in component.tabs.values():
                        for group in tab.groups.values():
                            if key in group.fields:
                                group.fields[key].value = value
                                updated = True
                                break
                        if updated:
                            break
        return component
       
        
    
    def dump(self, component: Component, filepath:str) -> None:
        with open(filepath, 'w') as file:
            file.write(f"Name={component.name}\n")
            for tab in component.tabs.values():
                file.write("\n")
                file.write(f"// Tab: {tab.name}\n")
                for group in tab.groups.values():
                    file.write(f"// Group: {group.name}\n")
                    for key, field_obj in group.fields.items():
                        file.write(f"{key}={field_obj.value}\n")
    

class ComponentFactory:
    _parsers = {}
    
    @classmethod
    def register_parsers(cls, file_type:str, parser: ComponentParser):
        cls._parsers[file_type.lower()] = parser()

    @classmethod
    def create_from_file(cls, file_type:str, filepath:str) -> Component:
        parser = cls._parsers.get(file_type.lower())
        if not parser:
            raise ValueError(f"No parser registered for file type '{file_type}'")
        return parser.load(filepath)
    
    @classmethod
    def dump_to_file(cls, component: Component, file_type:str, filepath:str):
        parser = cls._parsers.get(file_type.lower())
        if not parser:
            raise ValueError(f"No parser registered for file type '{file_type}'")
        parser.dump(component, filepath)

ComponentFactory.register_parsers('json', JSONComponentParser)
ComponentFactory.register_parsers('raw', RawComponentParser)

