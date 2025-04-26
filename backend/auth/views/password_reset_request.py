from django.contrib.auth.forms import PasswordResetForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CustomPasswordResetRequestView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        form = PasswordResetForm(data=request.data)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name="registration/password_reset_email.html",
            )
        return Response({"detail": "If an account exists, password reset instructions have been sent."}, status=status.HTTP_200_OK)
