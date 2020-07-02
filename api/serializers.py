from rest_framework import serializers

from .models import FastaEntry, Sequence


class FastaEntrySerializer(serializers.ModelSerializer):

	class Meta:
		model = FastaEntry
		fields = '__all__'


class SequenceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sequence
		fields = '__all__'
