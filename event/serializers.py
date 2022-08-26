from rest_framework import serializers
from event.models import Event



class EventSerializers(serializers.Serializer):
    id = serializers.CharField(max_length=255, read_only=True)
    name = serializers.CharField(max_length=225)
    description = serializers.CharField(max_length=225)
    location = serializers.CharField(max_length=225)
    date = serializers.DateTimeField()
    cretedBy = serializers.CharField(max_length=225)

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'location', 'date', 'createdBy']

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def list(self, attrs):
        """
        TODO
        """
        

    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.location = validated_data.get('location', instance.location)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.createdBy = validated_data.get('createdBy', instance.createdBy)
    #     instance.save()
    #     return instance


    
        
