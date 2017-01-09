from rest_framework import serializers

from .models import AnalyticsActivity


class AnalyticsActivitySerializer(serializers.ModelsSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AnalyticsActivity
        fields = ('user', 'graph', 'accessed_via', 'time_spent', 'score')
        read_only_fields = ('score')
