from django.urls import path, include

urlpatterns = [
  
    path('dash/', include('dashboard.urls')),
]

