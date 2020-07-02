from rest_framework.views import APIView


from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from rest_framework import status

from .serializers import FastaEntrySerializer
from .models import FastaEntry


class FastaEntryView(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def get(self, request, *args, **kwargs):
		fastas = FastaEntry.objects.all()
		serializer = FastaEntrySerializer(fastas, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		fastas_serializer = FastaEntrySerializer(data=request.data)
		if fastas_serializer.is_valid():
			fastas_serializer.save()
			return Response(fastas_serializer.data, status=status.HTTP_201_CREATED)
		else:
			print('error', fastas_serializer.errors)
			return Response(fastas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
