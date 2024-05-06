from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from eventapp.models import Event
from eventapp.permissions import IsOwnerPermission
from eventapp.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'location']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        event = self.get_object()
        event.attendees.add(request.user)
        return Response({'status': 'registered'})

    @action(detail=True, methods=['post'])
    def unregister(self, request, pk=None):
        event = self.get_object()
        if request.user in event.attendees.all():
            event.attendees.remove(request.user)
            return Response({'status': 'unregistered'})
        else:
            return Response({'status': 'not registered'}, status=status.HTTP_400_BAD_REQUEST)
