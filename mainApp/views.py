from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, ListView , UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, UserEditForm, AvatarForm
from .models import EstacionesTransformadoras, EquipoRed, EquipoProteccion, EquipoTelecontrol, Avatar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, "mainApp/home.html" )

def home(request):
    return render(request, "mainApp/home.html" )

def aboutMe(request):
    return render(request, "mainApp/aboutMe.html" )

#_____________________________ Estaciones TRansformadoras

class EstacionesTransformadorasList(ListView):
    model = EstacionesTransformadoras

class EstacionesTransformadorasCreate(LoginRequiredMixin, CreateView):
    model = EstacionesTransformadoras
    fields = ['nombre', 'codificacion', 'ubicacion', 'nivelTension']
    success_url = reverse_lazy('estacionesTransformadoras')

class EstacionesTransformadorasUpdate(LoginRequiredMixin, UpdateView):
    model = EstacionesTransformadoras
    fields = ['nombre', 'codificacion', 'ubicacion', 'nivelTension']
    success_url = reverse_lazy('estacionesTransformadoras') 

class EstacionesTransformadorasDelete(LoginRequiredMixin, DeleteView):
    model = EstacionesTransformadoras
    success_url = reverse_lazy('estacionesTransformadoras')

@login_required    
def verDetalleEETT(request, nombre):
    equipoRed = EquipoRed.objects.filter(estacionTransformadora__nombre = nombre)
    equipoTelecontrol = EquipoTelecontrol.objects.filter(estacionTransformadora__nombre = nombre)
    equipoProteccion = EquipoProteccion.objects.filter(estacionTransformadora__nombre = nombre)

    context = {'nombre':nombre ,'equiposRed': equipoRed,'equiposTelecontrol': equipoTelecontrol, 'equiposProteccion': equipoProteccion }
    return render(request, "mainApp/verDetalleEETT.html", context)

#_____________________________ Equipos de Red
class EquipoRedList(LoginRequiredMixin, ListView):
    model = EquipoRed

class EquipoRedCreate(LoginRequiredMixin, CreateView):
    model = EquipoRed
    fields = ['nombre', 'descripcion', 'nivel_tension', 'edificio', 'gabinete', 'ip', 'mask', 'defGw', 'estacionTransformadora']
    success_url = reverse_lazy('equiposRed')

class EquipoRedUpdate(LoginRequiredMixin, UpdateView):
    model = EquipoRed
    fields = ['nombre', 'descripcion', 'nivel_tension', 'edificio', 'gabinete', 'ip', 'mask', 'defGw', 'estacionTransformadora']
    success_url = reverse_lazy('equiposRed') 

class EquipoRedDelete(LoginRequiredMixin, DeleteView):
    model = EquipoRed
    success_url = reverse_lazy('equiposRed')

#_____________________________ Equipos de Telecontrol
class EquipoTelecontrolList(LoginRequiredMixin, ListView):
    model = EquipoTelecontrol

class EquipoTelecontrolCreate(LoginRequiredMixin, CreateView):
    model = EquipoTelecontrol
    fields = ['nombre', 'descripcion', 'nivel_tension', 'edificio', 'gabinete', 'ip', 'mask', 'defGw', 'estacionTransformadora']
    success_url = reverse_lazy('equiposTelecontrol')

class EquipoTelecontrolUpdate(LoginRequiredMixin, UpdateView):
    model = EquipoTelecontrol
    fields = ['nombre', 'descripcion', 'nivel_tension', 'edificio', 'gabinete', 'ip', 'mask', 'defGw', 'estacionTransformadora']
    success_url = reverse_lazy('equiposTelecontrol')

class EquipoTelecontrolDelete(LoginRequiredMixin, DeleteView):
    model = EquipoTelecontrol
    success_url = reverse_lazy('equiposTelecontrol')

#_____________________________ Equipos de Proteccion
class EquipoProteccionList(LoginRequiredMixin, ListView):
    model = EquipoProteccion

class EquipoProteccionCreate(LoginRequiredMixin, CreateView):
    model = EquipoProteccion
    fields = ['nombre', 'descripcion', 'nivel_tension', 'edificio', 'gabinete', 'ip', 'mask', 'defGw', 'estacionTransformadora']
    success_url = reverse_lazy('equiposProteccion')

class EquipoProteccionUpdate(LoginRequiredMixin, UpdateView):
    model = EquipoProteccion
    fields = ['nombre', 'descripcion', 'nivel_tension', 'edificio', 'gabinete', 'ip', 'mask', 'defGw', 'estacionTransformadora']
    success_url = reverse_lazy('equiposProteccion')

class EquipoProteccionDelete(LoginRequiredMixin, DeleteView):
    model = EquipoProteccion
    success_url = reverse_lazy('equiposProteccion')

#_____________________________ Login/Register
def userLogin(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            userName = miForm.cleaned_data.get('username')
            passWord = miForm.cleaned_data.get('password')
            user = authenticate(username=userName, password=passWord)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session['avatar'] = avatar

                return render(request, "mainApp/home.html")
            else:
                return render(request, 'mainApp/userLogin.html', {'form':miForm})
        else:
            return render(request, 'mainApp/userLogin.html', {'form':miForm})
    
    miForm = AuthenticationForm()
    return render(request, 'mainApp/userLogin.html', {'form':miForm})

def userRegister(request):
    if request.method == "POST":
        miForm = RegistroUsuarioForm(request.POST)
        if miForm.is_valid():
            username=miForm.cleaned_data.get('username')
            password=miForm.cleaned_data.get('password1')
            miForm.save()
            return redirect('/userLogin/')
    else:
        miForm = RegistroUsuarioForm()
    return render(request, "mainApp/UserRegister.html", {'form':miForm} )

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST) 
        if form.is_valid():
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.save()
            return render(request, "mainApp/home.html")
        else:
            return render(request, "mainApp/editProfile.html", {'form': UserEditForm(instance=usuario)})
    else:
        return render(request, "mainApp/editProfile.html", {'form': UserEditForm(instance=usuario)})
            
@login_required
def editAvatar(request):
    usuario = request.user
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)
            
            #____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            #____ Guardo avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #____ Hago que la url de la imagen viaje por en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request, "mainApp/editAvatar.html", {'form': form }) 
    else:
        form = AvatarForm()
        return render(request, "mainApp/editAvatar.html", {'form': form })
    
def search(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        searchResultRed = EquipoRed.objects.filter(nombre__icontains=patron)
        searchResultTelecontrol = EquipoTelecontrol.objects.filter(nombre__icontains=patron)
        searchResultProteccion = EquipoProteccion.objects.filter(nombre__icontains=patron)
    else:
        patron ='Buscar todo'
        searchResultRed = EquipoRed.objects.all()
        searchResultTelecontrol = EquipoTelecontrol.objects.all()
        searchResultProteccion = EquipoProteccion.objects.all()   
    context = {'resultRed':searchResultRed,
                'resultTelecontrol':searchResultTelecontrol, 
                'resultProteccion':searchResultProteccion,
                'patron':patron}
    return render(request, 'mainApp/listSearchResults.html', context)


