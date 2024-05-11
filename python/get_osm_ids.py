from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import time
from collections.abc import Iterator
from models import City
import os
import json


base_url = 'https://www.openstreetmap.org/search'
def get_driver():
	driver = webdriver.Firefox()
	return driver


def param_encode(name: str) -> str:
	params = dict(query=name)
	return urllib.parse.urlencode(params)


def attempt_location_tag(driver, location_size: str):
	'''the three type of location_sizes are either
	city, town or village.
	capitalized
	'''
	try:
		element = driver.find_element(By.CSS_SELECTOR, f'a[data-prefix="{location_size}"]')
		return element
	except Exception as er:
		return None

def query_openstreet(driver, city: City):
	'''automated script to get osm_id using selenium'''

	driver.get(f'{base_url}?{param_encode(city.commune_name_ascii)}')
	time.sleep(2)

	element = attempt_location_tag(driver, 'City')
	if not element:
		element = attempt_location_tag(driver, 'Town')
	if not element:
		element = attempt_location_tag(driver, 'Village')


	if not element:
		return None
	osm_id = element.get_attribute('data-id')
	city.osm_id = int(osm_id)


def read_json_file(file_location: str, model: City) -> Iterator[City]:
	with open(file_location, 'r') as fl:
		payload: dict = json.load(fl)
		for item in payload:
			yield model(**item)


def write_to_location(file_location: str, payload: dict):
	with open(file_location, 'w+') as fl:
		fl.write(json.dumps(payload))


from pathlib import Path

if __name__ == '__main__':
	current_dir = Path().resolve()
	city_json = os.path.join(current_dir, 'json', 'algeria_cities.json')
	to_city_json = os.path.join(current_dir, 'json', 'algeria_cities_export.json')
	
	# now we have a full working dataset of cities
	items = list(read_json_file(city_json, City))

	# cleaned cities without osm_id
	cleaned_items = [item for item in items if item.osm_id == -1]

	driver = get_driver()

	for item in cleaned_items:
		query_openstreet(driver, item)
		# sleep a bit to stop from getting blocked
		time.sleep(2)


	to_dict = [item.dict() for item in cleaned_items]
	write_to_location(to_city_json, to_dict)

