from rest_framework import serializers
from .models import FastaEntry, Sequence
from .utils import *
from django.core.files.storage import default_storage
from django.core.exceptions import ValidationError


class FastaEntrySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
   
        fastaNew = FastaEntry.objects.create(**validated_data['data'])
        #fastaNew = FastaEntry(nombre = validated_data[0] ,fasta_file =validated_data[1] )
        #fastaNew.save()
        print(validated_data['sequences'])
        print("llamado")
        
        for seq in validated_data['sequences']:
           import pdb; pdb.set_trace()
           nuevaSeq = Sequence(fasta = fastaNew  ,gb_id= getID(seq.header), 
	        sequence = seq.body,
	        latitude = getLatitud(seq.header),	
            longitude = getLongitud(seq.header) )
           nuevaSeq.save()
        print("Estoy imprimiendo")   
        print(fastaNew)
        return fastaNew

    def validate(self, data):

        print("entre aca")
        path = default_storage.save(
            'tmp/{}'.format(data['fasta_file'].name), data['fasta_file'])
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        result = generateAlignamient(tmp_file)
        if(result.isValid):
            data['alignament_file']= result.alignroute
            arrayResult ={ 
                'data': data,
                'sequences': result.sequences
            }
            os.remove(tmp_file)
            return arrayResult
        else:
            os.remove(tmp_file)
            raise ValidationError(
                'Error al validar archivo fasta: {}'.format(result.message))

    class Meta:
        model = FastaEntry
        fields = '__all__'


class SequenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sequence
        fields = '__all__'
