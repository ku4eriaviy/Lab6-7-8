from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .models import Event, Participation, UserProfile
from .serializers import UserSerializer, RegisterSerializer, EventSerializer, ParticipationSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_active=True).order_by("-date_start")
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def participate(self, request, pk=None):
        event = self.get_object()
        if event.participations.filter(user=request.user).exists():
            return Response({"detail": "Вы уже подали заявку"}, status=status.HTTP_400_BAD_REQUEST)

        participation = Participation.objects.create(
            user=request.user,
            event=event,
            comment=request.data.get("comment", "")
        )
        return Response(ParticipationSerializer(participation).data)


class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Participation.objects.all()
        return Participation.objects.filter(user=self.request.user)