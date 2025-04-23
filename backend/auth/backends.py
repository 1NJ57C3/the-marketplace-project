from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class FlexAuth(ModelBackend):
    login_fields = ['username', 'email']

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        
        # Dynamic Q object to search across all login_fields
        queries = Q()
        for field in self.login_fields:
            queries |= Q(**{f"{field}__iexact": username})

        try:
            user = User.objects.get(queries)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

        if user and user.check_password(password) and user.is_active:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
