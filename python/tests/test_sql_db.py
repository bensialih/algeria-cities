import pytest
from pathlib import Path
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from algeria_cities.models import Base, City, Postcode, CityModel, PostcodeModel
from algeria_cities.search import EntryFilter
from sqlite3 import Cursor
from sqlite3 import Connection
from unittest import TestCase
from algeria_cities.helpers import get_file_content

from random import randrange

BASE_DIR = Path(__file__).parent.parent.parent
SQL_DIR = os.path.join(BASE_DIR, "sql")
JSON_DIR = os.path.join(BASE_DIR, "json")

def seed_database(conn, file_location):
    with open(file_location, "r") as file:
        connection: Connection = conn.raw_connection()
        cursor: Cursor = connection.cursor()
        cursor.executescript(file.read())


class TestCities(TestCase):
    def setUp(self):
        self.conn = create_engine("sqlite://")
        Base.metadata.create_all(self.conn)
        cities_sql = os.path.join(SQL_DIR, "algeria_cities.sql")
        seed_database(self.conn, cities_sql)

        postcode_sql = os.path.join(SQL_DIR, "algeria_postcodes.sql")
        seed_database(self.conn, postcode_sql)
        self.session = Session(self.conn)

    def tearDown(self):
        connection: Connection = self.conn.raw_connection()
        cursor: Cursor = connection.cursor()
        cursor.execute("DELETE FROM algeria_cities")
        cursor.execute("DELETE FROM algeria_postcodes")
        self.session.rollback()
        self.session.close()

    def test_sql_cities_count(self):
        count = self.session.query(City).count()
        assert count == 1541

    def test_sql_postcodes_count(self):
        count = self.session.query(Postcode).count()
        assert count == 3940

    def test_get_json_objects(self):
        file = os.path.join(JSON_DIR, "algeria_cities.json")
        assert os.path.isfile(file)
        entries = get_file_content(file)
        assert isinstance(entries[0], CityModel)

        file = os.path.join(JSON_DIR, "algeria_postcodes.json")
        assert os.path.isfile(file)
        entries = get_file_content(file)
        assert isinstance(entries[0], PostcodeModel)

    def test_random_cities_test(self):
        file = os.path.join(JSON_DIR, "algeria_cities.json")
        assert os.path.isfile(file)
        entries = get_file_content(file)
        filter_obj = EntryFilter(entries)

        for index in range(200):
            pk = randrange(1, 1541)
            entry = filter_obj.find_by("id", pk)
            sql_entry: City = self.session.query(City).get(pk)
            column_names = City.__table__.columns.keys()
            for column_key in column_names:
                assert getattr(entry, column_key) == getattr(sql_entry, column_key)

    def test_random_postcode_test(self):
        file = os.path.join(JSON_DIR, "algeria_postcodes.json")
        assert os.path.isfile(file)
        entries = get_file_content(file)
        filter_obj = EntryFilter(entries)

        for index in range(200):
            random_entry = randrange(1, 3900)
            entry = entries[random_entry]
            if entry.post_code == "":
                continue
            sql_entry: Postcode = self.session.query(Postcode) \
                .filter(Postcode.post_code == entry.post_code) \
                .first()
            column_names = Postcode.__table__.columns.keys()
            column_names.remove("id")
            for column_key in column_names:
                assert getattr(entry, column_key) == getattr(sql_entry, column_key)

    def test_search_by_key_test(self):
        file = os.path.join(JSON_DIR, "algeria_postcodes.json")
        assert os.path.isfile(file)
        entries = get_file_content(file)
        filter_obj = EntryFilter(entries) \
            .remove("post_code", "", PostcodeModel) \
            .index("post_code")

        sql_entries: Postcode = self.session.query(Postcode).all()
        for index in range(200):
            random_entry = randrange(1, 3900)
            entry = sql_entries[random_entry]

            if entry.post_code == "":
                continue

            json_entry = filter_obj.get_entry(entry.post_code)
            column_names = Postcode.__table__.columns.keys()
            column_names.remove("id")

            for column_key in column_names:
                assert getattr(json_entry, column_key) == getattr(entry, column_key)

    def test_for_empty_postcodes(self):
        sql_entry: Postcode = self.session.query(Postcode).filter(Postcode.post_code == "")
        current_empty_postcodes = 91
        assert sql_entry.count() == current_empty_postcodes
