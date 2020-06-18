from rest_framework import serializers

from .models import FastaEntry

class FastaEntrySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = FastaEntry
		fields = '__all__'