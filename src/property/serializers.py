from rest_framework.serializers import ModelSerializer
from .models import Propriety
#from core.models import Propriety

class ProprietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriety
        fields = ['id', 
                  'street_address', 
                  'address_number', 
                  'city',
                  'province_state',
                  'coutry']