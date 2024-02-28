from django.urls import path
from .views import Register, ForgetPasswordGenerateOTP, AccountDetail, ResetPassword, AccountEdit, BlacklistTokenUpdateView, EmailUpdateSendOTPView, EmailUpdateVerifyOTPView


app_name = "user"    

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("account-detail/", AccountDetail.as_view(), name = "account-detail"),
    path("account-edit/", AccountEdit.as_view(), name = "account-edit"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
    name='blacklist'),
    path('generate-otp/', ForgetPasswordGenerateOTP.as_view(), name = "generate-otp"),
    path('reset-password/', ResetPassword.as_view(), name = "reset-password"),
    path("update-email-send-otp/", EmailUpdateSendOTPView.as_view(), name="update-email-send-otp"),
    path("update-email-verify-otp/", EmailUpdateVerifyOTPView.as_view(), name="update-email-verify-otp"),
]