from rest_framework.permissions import BasePermission,SAFE_METHODS
#SAFE_METHODS contains (GET,HEAD,Option)

class OwnerCanmangeorReadonly(BasePermission):
    message = ''
    def has_permission(self,request,view):
        message = 'your request does not have permission or you are is not'
        if request.method in SAFE_METHODS:
            return True
        elif not request.user.is_anonymous:
            return True
        else:
            return False
            
    def has_object_permission(self,request,view,obj):
        message = 'you must be owner'
        return request.user == obj.owner