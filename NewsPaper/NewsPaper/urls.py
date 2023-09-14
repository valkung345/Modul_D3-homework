from django.contrib import admin
from django.urls import path, include # не забываем импортировать include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем наше приложение и не забываем создать urls.py в приложении/папке fastfood
    path('', include('newapp.urls')),# делаем так, чтобы все адреса из нашего приложения (fastfood/urls.py) сами автоматически подключались когда мы их добавим.
]