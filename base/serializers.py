from rest_framework import serializers


class AnotherServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title_en = serializers.CharField(read_only=True)
    title_description_en = serializers.CharField(read_only=True)
    description_en = serializers.CharField(read_only=True)
    price_en = serializers.CharField(read_only=True)
    tax_en = serializers.CharField(read_only=True)

    title_ru = serializers.CharField(read_only=True)
    title_description_ru = serializers.CharField(read_only=True)
    description_ru = serializers.CharField(read_only=True)

    price_ru = serializers.CharField(read_only=True)
    tax_ru = serializers.CharField(read_only=True)


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title_en = serializers.CharField(read_only=True)
    text_en = serializers.CharField(read_only=True)
    price_en = serializers.CharField(read_only=True)

    title_ru = serializers.CharField(read_only=True)
    text_ru = serializers.CharField(read_only=True)
    price_ru = serializers.CharField(read_only=True)
