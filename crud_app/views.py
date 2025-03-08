from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

@login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'usuarios/user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'usuarios/user_detail.html', {'user': user})

@login_required
def user_edit(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'usuarios/user_edit.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'usuarios/user_confirm_delete.html', {'user': user})

@login_required
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'roles/role_list.html', {'roles': roles})

@login_required
def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'roles/role_form.html', {'form': form})

@login_required
def role_edit(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/role_form.html', {'form': form})

@login_required
def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list')
    return render(request, 'roles/role_confirm_delete.html', {'role': role})

@login_required
def sub_cat_list(request):
    sub_cat = SubCategory.objects.all()
    return render(request,'sub_categorias/sub_cat_list.html', {'sub_cat': sub_cat})

@login_required
def sub_cat_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sub_cat_list')
    else:
        form = SubCategoryForm()
    return render(request,'sub_categorias/sub_cat_form.html', {'form': form})

@login_required
def sub_cat_edit(request, pk):
    sub_cat = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=sub_cat)
        if form.is_valid():
            form.save()
            return redirect('sub_cat_list')
    else:
        form = SubCategoryForm(instance=sub_cat)
    return render(request,'sub_categorias/sub_cat_form.html', {'form': form})

@login_required
def sub_cat_delete(request, pk):
    sub_cat = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        sub_cat.delete()
        return redirect('sub_cat_list')
    return render(request,'sub_categorias/sub_cat_confirm_delete.html', {'sub_cat': sub_cat})
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categorias/cat_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categorias/cat_form.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categorias/cat_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categorias/cat_confirm_delete.html', {'category': category})

@login_required
def mobiliary_list(request):
    mobiliaries = Moviliario.objects.all()
    return render(request,'mobiliarios/mob_list.html', {'mobiliaries': mobiliaries})

@login_required
def mobiliary_create(request):
    if request.method == 'POST':
        form = MobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobiliary_list')
    else:
        form = MobForm()
    return render(request,'mobiliarios/mob_form.html', {'form': form})

@login_required
def mobiliary_edit(request, pk):
    mobiliary = get_object_or_404(Moviliario, pk=pk)
    if request.method == 'POST':
        form = MobForm(request.POST, instance=mobiliary)
        if form.is_valid():
            form.save()
            return redirect('mobiliary_list')
    else:
        form = MobForm(instance=mobiliary)
    return render(request, 'mobiliarios/mob_form.html', {'form': form})

@login_required
def mobiliary_delete(request, pk):
    mobiliary = get_object_or_404(Moviliario, pk=pk)
    if request.method == 'POST':
        mobiliary.delete()
        return redirect('mobiliary_list')
    return render(request, 'mobiliarios/mob_confirm_delete.html', {'mobiliary': mobiliary})

@login_required
def region_list(request):
    regions = Regional.objects.all()
    return render(request,'regional/reg_list.html', {'regions': regions})

@login_required
def region_create(request):
    if request.method == 'POST':
        form = RegionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('region_list')
    else:
        form = RegionalForm()
    return render(request,'regional/reg_form.html', {'form': form})

@login_required
def region_edit(request, pk):
    region = get_object_or_404(Regional, pk=pk)
    if request.method == 'POST':
        form = RegionalForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('region_list')
    else:
        form = RegionalForm(instance=region)
    return render(request, 'regional/reg_form.html', {'form': form})

@login_required
def region_delete(request, pk):
    region = get_object_or_404(Regional, pk=pk)
    if request.method == 'POST':
        region.delete()
        return redirect('region_list')
    return render(request, 'regional/reg_confirm_delete.html', {'region': region})
@login_required
def center_list(request):
    centers = CentroFormacion.objects.all()
    return render(request, 'centros/cen_list.html', {'centers': centers})
@login_required
def center_create(request):
    if request.method == 'POST':
        form = CentroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')
    else:
        form = CentroForm()
    return render(request, 'centros/cen_form.html', {'form': form})
@login_required
def center_edit(request, pk):
    center = get_object_or_404(CentroFormacion, pk=pk)
    if request.method == 'POST':
        form = CentroForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            return redirect('center_list')
    else:
        form = CentroForm(instance=center)
    return render(request, 'centros/cen_form.html', {'form': form})
@login_required
def center_delete(request, pk):
    center = get_object_or_404(CentroFormacion, pk=pk)
    if request.method == 'POST':
        center.delete()
        return redirect('center_list')
    return render(request, 'centros/cen_confirm_delete.html', {'center': center})
@login_required
def list_sede(request):
    sedes = Sede.objects.all()
    return render(request,'sedes/sed_list.html', {'sedes': sedes})
@login_required
def create_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sedes_list')
    else:
        form = SedeForm()
    return render(request,'sedes/sed_form.html', {'form': form})
@login_required
def edit_sede(request, pk):
    sede = get_object_or_404(Sede, pk=pk)
    if request.method == 'POST':
        form = SedeForm(request.POST, instance=sede)
        if form.is_valid():
            form.save()
            return redirect('sedes_list')
    else:
        form = SedeForm(instance=sede)
    return render(request,'sedes/sed_form.html', {'form': form})
@login_required
def delete_sede(request, pk):
    sede = get_object_or_404(Sede, pk=pk)
    if request.method == 'POST':
        sede.delete()
        return redirect('sedes_list')
    return render(request,'sedes/sed_confirm_delete.html', {'sede': sede})

@login_required
def list_programs(request):
    programs = Programa_Formacion.objects.all()
    return render(request, 'programas_formacion/pro_list.html', {'programs': programs})
@login_required
def create_program(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_programs')
    else:
        form = ProgramaForm()
    return render(request, 'programas_formacion/pro_form.html', {'form': form})

@login_required
def edit_program(request, pk):
    program = get_object_or_404(Programa_Formacion, pk=pk)
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('list_programs')
    else:
        form = ProgramaForm(instance=program)
    return render(request, 'programas_formacion/pro_form.html', {'form': form})
@login_required
def delete_program(request, pk):
    program = get_object_or_404(Programa_Formacion, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('list_programs')
    return render(request, 'programas_formacion/pro_confirm_delete.html', {'program': program})
@login_required
def list_fichas(request):
    fichas = Ficha.objects.all()
    return render(request, 'fichas/fic_list.html', {'fichas': fichas})
@login_required
def create_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_fichas')
    else:
        form = FichaForm()
    return render(request, 'fichas/fic_form.html', {'form': form})

@login_required
def edit_ficha(request, pk):
    ficha = get_object_or_404(Ficha, pk=pk)
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('list_fichas')
    else:
        form = FichaForm(instance=ficha)
    return render(request, 'fichas/fic_form.html', {'form': form})

@login_required
def delete_ficha(request, pk):
    ficha = get_object_or_404(Ficha, pk=pk)
    if request.method == 'POST':
        ficha.delete()
        return redirect('list_fichas')
    return render(request, 'fichas/fic_confirm_delete.html', {'ficha': ficha})

@login_required
def mobiliary_protected_list(request):
    mobiliaries = Moviliario.objects.all()
    return render(request,'protegidos/mob_list.html', {'mobiliaries': mobiliaries})

def fichas_protected_list(request):
    fichas = Ficha.objects.all()
    return render(request, 'protegidos/fic_list.html', {'fichas': fichas})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')

@login_required
def ambientes_list(request):
    ambientes = Ambiente.objects.all()
    return render(request, 'ambientes/amb_list.html', {'ambientes': ambientes})

@login_required
def ambiente_create(request):
    if request.method == 'POST':
        form = AmbienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ambientes_list')
    else:
        form = AmbienteForm()
    return render(request, 'ambientes/amb_form.html', {'form': form})

@login_required
def ambiente_edit(request, pk):
    ambiente = Ambiente.objects.get(pk=pk)
    if request.method == 'POST':
        form = AmbienteForm(request.POST, instance=ambiente)
        if form.is_valid():
            form.save()
            return redirect('ambientes_list')
        else:
            form = AmbienteForm(instance=ambiente)
            return render(request, 'ambientes/amb_form.html', {'form': form})

@login_required
def ambiente_delete(request, pk):
    ambiente = Ambiente.objects.get(pk=pk)
    if request.method == 'POST':
        ambiente.delete()
        return redirect('ambientes_list')
    else:
        return render(request, 'ambientes/amb_confirm_delete.html', {'ambiente': ambiente})