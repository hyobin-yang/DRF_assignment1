from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 요청자(request.user)가 객체인 board인 유저와 동일한지 확인
        return obj.user == request.user