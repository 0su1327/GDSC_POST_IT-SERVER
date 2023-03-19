from rest_framework import serializers
from .models import Users
from .models import Note
from .models import Postit
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'user_email',
          'user_pw',
        )
        model = Users

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user',
            'user_name',
            'description',
        )
        model = Note

class PostitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'note',
            'anonymous',
            'writer',
            'content_text',
        )
        model = Postit