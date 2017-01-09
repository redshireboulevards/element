from rest_framework.generics import CreateAPIView

from .serializers import AnalyticsActivitySerializer


class AnalyticsActivityCreateView(CreateAPIView):

    serializer_class = AnalyticsActivitySerializer
