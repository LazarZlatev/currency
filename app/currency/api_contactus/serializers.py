from rest_framework import serializers
from currency.models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    created = serializers.DateTimeField()
    subject = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return ContactUs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.created = validated_data.get('created', instance.created)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'name',
            'email',
            'created',
            'subject',
            'body',
        )
