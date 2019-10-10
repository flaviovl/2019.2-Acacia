from rest_framework.viewsets import ModelViewSet
from .serializers import ProprietySerializer
from .models import Propriety
#from core.models import Property


class ProprietyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Propriety.objects.all()
    serializer_class = ProprietySerializer