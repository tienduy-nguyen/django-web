from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):
  """
    A viewset for viewing and editing lead instances.
  """
  queryset = Lead.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LeadSerializer
