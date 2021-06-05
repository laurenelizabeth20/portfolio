from django.conf.urls import include, url

from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    # Other URL patterns ...
    path('accounts/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # More URL patterns ...
]