from django.db import models


class City(models.Model):

	id = models.IntegerField(primary_key=True)
	commune_name = models.CharField(max_length=255)
	commune_name_ascii = models.CharField(max_length=255)
	daira_name = models.CharField(max_length=255)
	daira_name_ascii = models.CharField(max_length=255)
	wilaya_code = models.CharField(max_length=4)
	wilaya_name = models.CharField(max_length=255)
	wilaya_name_ascii = models.CharField(max_length=255)

	class Meta:
		db_table = 'algeria_cities'

	def __str__(self):
		return self.commune_name_ascii

	def search(self):
		return f'{self.commune_name_ascii}, {self.daira_name_ascii}, {self.wilaya_name_ascii}, {self.wilaya_code}, Algeria'


