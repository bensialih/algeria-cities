from pydantic import BaseModel


class City(BaseModel):
    id: int
    commune_name_ascii: str
    commune_name: str
    daira_name_ascii: str
    daira_name: str
    wilaya_code: str
    wilaya_name_ascii: str
    wilaya_name: str
    osm_id: int

    def __str__(self):
        return str(self.commune_name_ascii)


class NotFound(BaseModel):
    city: City

    def __str__(self):
        return str(self.city)
