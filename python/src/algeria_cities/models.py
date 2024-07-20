from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Union, List, Any
Base = declarative_base()

class City(Base):
    __tablename__ = "algeria_cities"

    id = Column(Integer(), primary_key = True)
    commune_name = Column(String(255))
    commune_name_ascii = Column(String(100))
    daira_name = Column(String(255))
    daira_name_ascii = Column(String(100))
    wilaya_code = Column(String(4))

    wilaya_name = Column(String(255))
    wilaya_name_ascii = Column(String(100))
    osm_id = Column(Integer())


class Postcode(Base):
    __tablename__ = "algeria_postcodes"

    id = Column(Integer(), primary_key = True)
    post_code = Column(String(255))
    post_name = Column(String(100))
    post_name_ascii = Column(String(255))
    post_address = Column(String(255))
    post_address_ascii = Column(String(255))
    commune_id = Column(Integer())
    commune_name = Column(String(255))
    commune_name_ascii = Column(String(100))
    daira_name = Column(String(255))
    daira_name_ascii = Column(String(100))
    wilaya_code = Column(String(4))
    wilaya_name = Column(String(255))
    wilaya_name_ascii = Column(String(100))


class CityModel(BaseModel):
    id: int
    commune_name: str
    commune_name_ascii: str
    daira_name: str
    daira_name_ascii: str
    wilaya_code: str
    wilaya_name: str
    wilaya_name_ascii: str
    osm_id: int

class PostcodeModel(BaseModel):
    post_code: str
    post_name: str
    post_name_ascii: str
    post_address: str
    commune_id: int
    commune_name: str
    commune_name_ascii: str
    daira_name: str
    daira_name_ascii: str
    wilaya_code: str
    wilaya_name: str
    wilaya_name_ascii: str
    # TODO: will need to look at empty field in JSON
    post_address_ascii: str = ''
