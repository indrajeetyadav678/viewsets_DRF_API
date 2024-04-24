from rest_framework import viewsets
from .models import RegistrationModel
from .serializers import Regist_Serializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = RegistrationModel.objects.all()
    serializer_class = Regist_Serializer