from rest_framework import serializers
from ads.models import Post
from users.models import CustomUser


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'phone', 'image']


class PostSerializer(serializers.ModelSerializer):

    # author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'date_posted', 'author', 'image']
        read_only_fields = ['date_posted']

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['author'] = instance.author.username
        return rep

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
