from django.db import models
from datetime import datetime

def get_fasta_path(instance, filename):
	date = datetime.now().strftime("%m-%d-%y")
	time = datetime.now().strftime("%H%M%S")
	return 'fastas/{}/{}/{}'.format(date, time, filename)

class FastaEntry(models.Model):
	nombre = models.CharField(max_length=60)
	detalles = models.TextField()
	fasta_file = models.FileField(upload_to=get_fasta_path)

	def __str__(self):
		return self.nombre