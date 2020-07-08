from .models import Names ,Periods
from rest_framework import serializers






class PeriodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Periods
        fields = ['start', 'end']


class NamesSerializer(serializers.HyperlinkedModelSerializer):
    activity_periods = PeriodsSerializer(many=True, read_only=True)
    class Meta:
        model = Names
        fields = ['id', 'real_name', 'timezone', 'activity_periods']



