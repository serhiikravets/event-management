from rest_framework import serializers
from eventapp.models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'organizer']
