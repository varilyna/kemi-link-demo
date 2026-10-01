from rest_framework import mixins, viewsets

from .models import Inquiry
from .serializers import InquirySerializer


class InquiryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
