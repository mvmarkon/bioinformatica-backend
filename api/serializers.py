from rest_framework import serializers

from .models import FastaEntry, Sequence


class FastaEntrySerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		fasta = FastaEntry.objects.create(**validated_data)
		# Esto es donde llamamos a la util o ALGO que devuelva la data de las secuencias como diccionarios
		# aca lo mockee 
		seqs = [{'fasta':fasta, 'sequence':'AAA', 'latitude':0.1, 'longitude':0.2},
            {'fasta':fasta, 'sequence':'AAT', 'latitude':0.1, 'longitude':0.2},
            {'fasta':fasta, 'sequence':'ATA', 'latitude':0.1, 'longitude':0.2},
            {'fasta':fasta, 'sequence':'TAA', 'latitude':0.1, 'longitude':0.2},
            {'fasta':fasta, 'sequence':'TAT', 'latitude':0.1, 'longitude':0.2}]
		for seq in seqs:
			Sequence.objects.create(**seq)
		return fasta

	class Meta:
		model = FastaEntry
		fields = '__all__'


class SequenceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sequence
		fields = '__all__'
