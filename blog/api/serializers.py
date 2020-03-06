from rest_framework.serializers import ModelSerializer
from blog.models import Blog

class postlistserializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','title',)

class postdetailserializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class postdeleteserializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class postupdateserializer(ModelSerializer):
    class Meta:
        model = Blog
        #fields = '__all__'
        exclude = ('owner',)

class postcreateserializer(ModelSerializer):
    class Meta:
        model = Blog
        #fields = '__all__'
        exclude = ('owner',)

class postdetailupdateserializer(ModelSerializer):
    class Meta:
        model = Blog
        #fields = '__all__'
        exclude = ('owner',)
    
class postdetaildestroyserializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class postupdatedestroyserializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        
        
        


