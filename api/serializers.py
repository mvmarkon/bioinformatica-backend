from rest_framework import serializers

from .models import FastaEntry

class FastaEntrySerializer(serializers.ModelSerializer):

	class Meta:
		model = FastaEntry
		fields = '__all__'