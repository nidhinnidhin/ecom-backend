from rest_framework import generics,permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
import random
from django.core.mail import send_mail
from.models import ForgetPasswordOTP
from datetime import datetime, timedelta
import string
from django.conf import settings
from django.utils import timezone
from django.http import JsonResponse
from django_otp import user_has_device
from django.utils.crypto import get_random_string
from django.contrib.sessions.backends.db import SessionStore


class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class AccountDetail(APIView):
    def get(self, request):
        user = self.request.user

        data = {
            "firstName":user.first_name,
            "lastName":user.last_name,
            "userName":user.username,
        }

        return Response(data)
    
    permission_classes = [permissions.IsAuthenticated]

class AccountEdit(APIView):
    def put(self, request):
        user = self.request.user
        user.first_name = request.data["firstName"]
        user.last_name = request.data["lastName"]
        user.username = request.data["userName"]

        user.save()

        return Response({"status": "Success"})
    
    permission_classes = [permissions.IsAuthenticated]

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ForgetPasswordGenerateOTP(APIView):
    def post(self, request):
        email = request.data["email"]
        print(email)
        if not User.objects.filter(email = email).exists():
            return Response({"message": "Invalid Email ID."}, status = 400)
        user = User.objects.get(email = email)
        print(user)
        if ForgetPasswordOTP.objects.filter(user = user).exists():
            print("Exists - deleted")
            ForgetPasswordOTP.objects.filter(user = user).delete()
        new_otp = ""
        for i in range(4):
            new_otp += str(random.randint(0,9))
        print(new_otp)
        otp = ForgetPasswordOTP.objects.create(user = user, otp=new_otp, created_on = datetime.now())

        subject = 'OTP for reset password - Click shop'
        message = f'Hi {user.username}, your OTP is {new_otp} for reset your password.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        print(otp.created_on)
        return Response({"status": "Success"})
    
class ResetPassword(APIView):
    def post(self, request):
        email = request.data["email"]
        otp = request.data["otp"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]

        user = User.objects.get(email = request.data["email"])

        if password1 != password2:
            return Response({"message": "Password doesn't match."}, status = 400)
        elif not User.objects.filter(email = request.data["email"]).exists():
            return Response({"message": "Invalid Email ID."}, status = 400)
        elif not ForgetPasswordOTP.objects.filter(user = user).exists():
            return Response({"message": "Generate OTP to change password."}, status = 400)

        otp_obj = ForgetPasswordOTP.objects.get(user = user)
        now_aware = timezone.now()
        difference = now_aware - otp_obj.created_on
        if difference.total_seconds()/60 > 10:
            otp_obj.delete()
            return Response({"message": "OTP expired, generate new to continue."}, status = 400)

        if otp == otp_obj.otp:
            user.set_password(password1)
            user.save()
            otp_obj.delete()
        else:
            return Response({"message": "OTP doesn't match."}, status = 400)

        return Response({"status": "Success"})
    
class EmailUpdateSendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            otp = ''.join(random.choices('0123456789', k=4))
            send_mail(
                'OTP for Email Verification',
                f'Your OTP for email verification is: {otp}',
                'nidhinbabu171@gmail.com',
                [email],
                fail_silently=False,
            )
            # Save OTP in user's profile (you can use user.profile.otp = otp)
            return Response({'success': True})
        else:
            return Response({'error': 'User not found'}, status=400)

class EmailUpdateVerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        user = User.objects.filter(email=email).first()
        if user:
            # Retrieve OTP from user's profile (you can use user.profile.otp)
            saved_otp = user.profile.otp  # Assuming you have a Profile model related to the User model
            if saved_otp == otp:
                # Check if OTP is not expired
                otp_timestamp = user.profile.otp_timestamp  # Assuming you have a timestamp field for OTP creation
                if datetime.now() - otp_timestamp <= timedelta(minutes=5):
                    # OTP is valid and not expired
                    # Perform email verification logic here
                    return Response({'success': True})
                else:
                    return Response({'error': 'OTP expired'}, status=400)
            else:
                return Response({'error': 'Invalid OTP'}, status=400)
        else:
            return Response({'error': 'User not found'}, status=400)
            

