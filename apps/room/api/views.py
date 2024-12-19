from rest_framework.viewsets import ModelViewSet
from apps.room.api.serializer import ChatRoomSerializer
from apps.room.models import ChatRoomModel
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import render
from django.http.response import HttpResponseNotFound


class ChatRoomViewSet(ModelViewSet):
    queryset = ChatRoomModel.objects.all()
    serializer_class = ChatRoomSerializer
    # permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            # Permitir acceso sin restricciones para solicitudes GET
            return [AllowAny()]
        # Aplicar permisos normales para otros métodos
        return [IsAdminUser()]



def register(request):
    return render(request, 'chat/chat.html')


def room(request, room_id):
    try:
        room = ChatRoomModel.objects.get(id=room_id)
    except Exception:
        return HttpResponseNotFound('Room not found')
    
    name = request.GET.get('name')
    context = {
        'room': room,
        'name': name,
    }  
    return render(request, 'chat/room.html', context)
