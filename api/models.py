
from django.db import models
from datetime import datetime

def get_fasta_path(instance, filename):
	date = datetime.now().strftime("%m-%d-%y")
	time = datetime.now().strftime("%H%M%S")
	return 'fastas/{}/{}/{}'.format(date, time, filename)


class FastaEntry(models.Model):
	nombre = models.CharField(max_length=60, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	fasta_file = models.FileField(upload_to=get_fasta_path)

	def __str__(self):
		return self.nombre


class Sequence(models.Model):
	fasta = models.ForeignKey(
		FastaEntry, on_delete=models.CASCADE, related_name='sequences')
	gb_id = models.CharField(max_length=60)
	sequence = models.TextField()
	latitude = models.DecimalField(
		max_digits=11, decimal_places=7, null=True, blank=True)
	longitude = models.DecimalField(
		max_digits=11, decimal_places=7, null=True, blank=True)
