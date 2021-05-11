from rest_framework import serializers
from ads.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'date_posted', 'author', 'image']
        read_only_fields = ['date_posted']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)