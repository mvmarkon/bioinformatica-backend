from django.urls import path
from . import views

#router = routers.DefaultRouter()
#router.register(r'fastaentries', views.FastaEntryViewSet)

urlpatterns = [
#    path('', include(router.urls)),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('fastas/', views.FastaEntryView.as_view(), name= 'fastas_list'),
]