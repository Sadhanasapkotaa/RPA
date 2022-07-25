from rest_framework import serializers
from video_streaming.models import Video



class HomeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    

    def validate(self, attrs):
        data = attrs['videofile']
        if not data:
            raise serializers.ValidationError('No Video')
        if data.size < 400:
            raise serializers.ValidationError('This field must be an less than 400 number.')
        return attrs