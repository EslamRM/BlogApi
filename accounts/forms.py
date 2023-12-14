from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """creation form for creat new user."""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",)


class CustomUserChangeForm(UserChangeForm):
    """A form used in the admin interface to change a user’s information and permissions."""

    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
