from django.urls import path
from . import views

#router = routers.DefaultRouter()
#router.register(r'fastaentries', views.FastaEntryViewSet)

urlpatterns = [
    path('fastas/', views.FastaEntryView.as_view(), name='fastas_list'),
    path('fastas/<int:pk>', views.FastaEntryView.as_view())
]
