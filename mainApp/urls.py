from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', home, name='home'),
    
    path('estacionesTransformadoras/', EstacionesTransformadorasList.as_view(), name="estacionesTransformadoras"),
    path('estacionesTransformadorasCreate/', EstacionesTransformadorasCreate.as_view(), name="estacionesTransformadorasCreate"),
    path('estacionesTransformadorasUpdate/<int:pk>', EstacionesTransformadorasUpdate.as_view(), name="estacionesTransformadorasUpdate"),
    path('estacionesTransformadorasDelete/<int:pk>', EstacionesTransformadorasDelete.as_view(), name="estacionesTransformadorasDelete"),
    path('verDetalleEETT/<nombre>/', verDetalleEETT, name='verDetalleEETT'),

    path('equiposRed/', EquipoRedList.as_view(), name="equiposRed"),
    path('equipoRedCreate/', EquipoRedCreate.as_view(), name="equipoRedCreate"),
    path('equipoRedUpdate/<int:pk>/', EquipoRedUpdate.as_view(), name="equipoRedUpdate"),
    path('equipoRedDelete/<int:pk>/', EquipoRedDelete.as_view(), name="equipoRedDelete"),
    
    path('equiposTelecontrol/', EquipoTelecontrolList.as_view(), name="equiposTelecontrol"),
    path('equipoTelecontrolCreate/', EquipoTelecontrolCreate.as_view(), name="equipoTelecontrolCreate"),
    path('equipoTelecontrolUpdate/<int:pk>/', EquipoTelecontrolUpdate.as_view(), name="equipoTelecontrolUpdate"),
    path('equipoTelecontrolDelete/<int:pk>/', EquipoTelecontrolDelete.as_view(), name="equipoTelecontrolDelete"),
    
    path('equiposProteccion/', EquipoProteccionList.as_view(), name="equiposProteccion"),
    path('equipoProteccionCreate/', EquipoProteccionCreate.as_view(), name="equipoProteccionCreate"),
    path('equipoProteccionUpdate/<int:pk>/', EquipoProteccionUpdate.as_view(), name="equipoProteccionUpdate"),
    path('equipoProteccionDelete/<int:pk>/', EquipoProteccionDelete.as_view(), name="equipoProteccionDelete"),
    
    path('userLogin/', userLogin, name='userLogin'),
    path('userRegister/', userRegister, name='userRegister'),
    path('userLogout/', LogoutView.as_view(template_name="mainApp/userLogout.html"), name="userLogout"),
    path('editProfile/', editProfile, name='editProfile'),
    path('editAvatar/', editAvatar, name='editAvatar'),

    path('listSearchResults/', search, name='listSearchResults'),

    path('aboutMe/', aboutMe ,name="aboutMe"),
]