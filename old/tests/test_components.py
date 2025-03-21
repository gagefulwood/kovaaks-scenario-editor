import pytest

# Import the classes from your modules.
# (Make sure your PYTHONPATH is set appropriately so these imports work.)
from components.component import Component, ComponentType
from components.component_factory import ComponentFactory, JSONComponentParser, RawComponentParser
from components.tab import Tab
from components.field_group import FieldGroup
from components.field import Field
from components.chr_schema import ChrSchema

# ----- Field tests -----
def test_field_value_float():
    f = Field(in_file_name="Test", in_game_name="Test Field", data_type="float")
    f.value = "3.14"
    assert isinstance(f.value, float)
    assert f.value == 3.14
    with pytest.raises(ValueError):
        f.value = "not_a_float"

def test_field_value_vector():
    f = Field(in_file_name="TestVec", in_game_name="Test Vector", data_type="vector")
    valid_vector = {"X": "1.0", "Y": 2, "Z": 3.5}
    f.value = valid_vector
    assert isinstance(f.value, dict)
    assert f.value["X"] == 1.0
    # Pass an invalid vector value
    with pytest.raises(ValueError):
        f.value = "invalid_vector"

# ----- Tab and FieldGroup tests -----
def test_tab_serialization():
    # Create a Tab with a FieldGroup and a Field
    tab = Tab(name="Test Tab")
    group = FieldGroup(name="Group1")
    field_obj = Field(in_file_name="Key", in_game_name="Field", data_type="string")
    field_obj.value = "TestValue"
    group.fields[field_obj.in_file_name] = field_obj
    tab.groups[group.name] = group
    
    # Convert to dict and back
    tab_dict = tab.to_dict()
    new_tab = Tab.from_dict(tab_dict)
    
    assert new_tab.name == tab.name
    assert "Group1" in new_tab.groups
    assert new_tab.groups["Group1"].fields["Key"].value == "TestValue"

def test_fieldgroup_serialization():
    # Create a FieldGroup with one Field
    group = FieldGroup(name="GroupTest")
    field_obj = Field(in_file_name="Field1", in_game_name="TestField", data_type="integer")
    field_obj.value = "42"  # Setter should convert to int if applicable, or leave as string if not validated
    group.fields[field_obj.in_file_name] = field_obj

    group_dict = group.to_dict()
    new_group = FieldGroup.from_dict(group_dict)
    assert new_group.name == group.name
    assert "Field1" in new_group.fields

# ----- ChrSchema tests -----
def test_chr_schema_tabs():
    component = ChrSchema.chr_schema()
    # Expected tabs names based on your schema creation:
    expected_tabs = {"Main", "Move", "Boxes", "Abilities", "Spawn", "Effects", "Jetpack"}
    # Since ChrSchema adds tabs via a while loop, we expect these keys.
    assert set(component.tabs.keys()) == expected_tabs

# ----- ComponentFactory / Parser tests -----
def test_component_factory_invalid_parser():
    with pytest.raises(ValueError) as excinfo:
        ComponentFactory.create_from_file("invalid", "dummy_path.txt")
    assert "No parser registered" in str(excinfo.value)

def test_json_parser_round_trip(tmp_path):
    # Create a dummy component.
    # Here we assume that Component has an attribute "name" and implements to_json/from_json.
    component = Component()
    component.name = "TestComponent"
    # (If your Component class has more required fields, initialize them accordingly.)
    
    # Dump the component to a JSON file using the JSONComponentParser.
    json_file = tmp_path / "component.json"
    ComponentFactory.dump_to_file(component, "json", str(json_file))
    
    # Read back the component.
    new_component = ComponentFactory.create_from_file("json", str(json_file))
    assert new_component.name == component.name

def test_raw_parser_round_trip(tmp_path):
    # For this test, use the ChrSchema to generate a component.
    component = ChrSchema.chr_schema()
    # Set a unique name so we can verify it is loaded correctly.
    component.name = "RawTestComponent"
    
    # Dump the component using the RawComponentParser.
    raw_file = tmp_path / "component.chr"
    ComponentFactory.dump_to_file(component, "raw", str(raw_file))
    
    # Now load the component from the raw file.
    loaded_component = ComponentFactory.create_from_file("raw", str(raw_file))
    # The RawComponentParser sets the component name to the file base name if not overridden.
    # Since our dump writes a "Name=" line, we expect that to override the file name.
    # Verify that the name from the file is used.
    with open(raw_file, "r") as f:
        content = f.read()
    # Look for a line like "Name=RawTestComponent"
    assert "Name=RawTestComponent" in content
    assert loaded_component.name == "RawTestComponent"

# ----- Additional tests -----
def test_json_parser_error_on_missing_file(tmp_path):
    missing_file = tmp_path / "nonexistent.json"
    with pytest.raises(FileNotFoundError):
        ComponentFactory.create_from_file("json", str(missing_file))