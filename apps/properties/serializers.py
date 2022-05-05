import imp
from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyViews


class PropertySerializer(Serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        fields = ['user', 'title', 'slug', 'ref_code', 'description', 'country', 'city',
            'postal_code', 'street_address', 'property_number', 'price', 'tax', 'plot_area',
            'total_floors', 'bedrooms', 'bathrooms', 'advert_type', 'property_type', 'cover_photo',
            'photo1', 'photo2', 'photo3', 'photo4', 'views', 'published', 'final_property_price']

        def get_ser(self, obj):
            return obj.user.username


class PropertyCreateSerializer(serializers.ModelSerializer):

    class meta:
        model = PropertyViews
        exclude = ["updated_at", "pkid"]