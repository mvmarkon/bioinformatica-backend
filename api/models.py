
from django.db import models
from datetime import datetime

def get_fasta_path(instance, filename):
	timestamp = datetime.now().strftime("%m%d%y%H%M%S")
	return 'fastas/{}{}'.format(timestamp,filename)


class FastaEntry(models.Model):
	nombre = models.CharField(max_length=60, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	fasta_file = models.FileField(upload_to=get_fasta_path)
	alignament_file = models.CharField(max_length=500, null=True, blank=True)
	newick_tree = models.CharField(max_length=10000, null=True, blank=True)
	
	def __str__(self):
		return self.nombre


class Sequence(models.Model):
	fasta = models.ForeignKey(
		FastaEntry, on_delete=models.CASCADE, related_name='sequences')
	gb_id = models.CharField(max_length=60, null=True, blank=True)
	sequence = models.TextField()
	latitude = models.DecimalField(
		max_digits=11, decimal_places=7, null=True, blank=True)
	longitude = models.DecimalField(
		max_digits=11, decimal_places=7, null=True, blank=True)
