from django.db import models

class FastaEntry(models.Model):
	nombre = models.CharField(max_length=60)
	detalles = models.TextField()
	fasta_file = models.FileField(upload_to='fastas')

	def __str__(self):
		return self.nombre