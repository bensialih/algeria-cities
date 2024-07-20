from typing import List, Union, Any, Optional
from algeria_cities.models import CityModel, PostcodeModel

ModelChoice = Union[CityModel, PostcodeModel]
ModelType = Optional[ModelChoice]


def filter_out_entry(key: str, value: Any):
    def _inner(entry: Any):
        test = getattr(entry, key) == value
        return not test
    return _inner

class EntryFilter:
    def __init__(self, entries: List[Union[CityModel, PostcodeModel]]):
        self.entries = entries
        self.indexed = dict()

    def index(self, key: str) -> "EntryFilter":
        # key must be unique
        if getattr(self.entries[0], key) is None:
            raise Exception(f"key {key} does not exist")

        self.indexed = dict()
        for entry in self.entries:
            self.indexed[getattr(entry, key)] = entry
        return self

    def get_entry(self, key_value):
        # leaf: should not be daisy-chained
        return self.indexed.get(key_value)

    def remove(self, key: str, value: Any, model_type: ModelChoice) -> "EntryFilter":
        # assert model_type is what it is
        assert type(self.entries[0]) == model_type

        self.entries = list(filter(filter_out_entry(key, value), self.entries))
        return self

    def find_by(self, key: str, value: Any) -> ModelType:
        for entry in self.entries:
            if getattr(entry, key) == value:
                return entry
