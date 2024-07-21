import json
from typing import Union, List
from algeria_cities.models import CityModel, PostcodeModel

def get_file_content(file_location: str) -> List[Union[CityModel, PostcodeModel]]:
    model = CityModel
    with open(file_location, "r") as fl:
        data = json.load(fl)
        try:
            model(**data[1])
        except:
            # failed to parse data in CityModel will default to PostcodeModel
            model = PostcodeModel

        return [model(**row) for row in data]
