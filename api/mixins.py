from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin():
    user_fields = 'user'
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_fields] = user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff():
            return qs
        return qs.filter(**lookup_data)
