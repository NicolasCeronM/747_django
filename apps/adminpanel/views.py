from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.product.models import Product
from apps.drop.models import Drop
from apps.orders.models import Order
from apps.user.models import CustomUser
from django.db.models import Q
from apps.product.forms import ProductForm
from apps.product.models import ProductImage, ProductSize
from django.contrib import messages
from apps.talent.models import Talent, TalentSocialLink
from django.http import JsonResponse, Http404
from apps.talent.forms import TalentForm, TalentSocialLinkForm
from django.forms import modelformset_factory

# ====== Dashboard ======
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# ====== Vista productos ======
def productos(request):
    query = request.GET.get("q", "")
    drop_id = request.GET.get("drop", "")

    products = Product.objects.select_related('drop')
    drops = Drop.objects.all()

    if query:
        products = products.filter(
            Q(id__icontains=query) |
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if drop_id:
        products = products.filter(drop_id=drop_id)

    return render(request, 'adminpanel/producto/producto.html', {
        'products': products,
        'drops': drops,
        'query': query,
    })

def product_create(request):
    drops = Drop.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        images = request.FILES.getlist('images')
        sizes = request.POST.getlist('sizes')
        

        if form.is_valid():
            product = form.save()

            # Guardar imágenes
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            # Guardar tallas
            for size in sizes:
                ProductSize.objects.create(product=product, size=size)

            messages.success(request, "✅ Producto creado con éxito.")
            return redirect('adminpanel:producto')

    else:
        form = ProductForm()

    return render(request, 'adminpanel/producto/product_create.html', {
        'form': form,
        'drops': drops,
    })


def eliminar_producto(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, '✅ Producto eliminado correctamente.')
        return redirect('adminpanel:producto')
    return redirect('adminpanel:producto')


# ====== Vista HTMX para búsqueda dinámica ======
def productos_htmx(request):
    query = request.GET.get("q", "")
    drop_id = request.GET.get("drop", "")

    products = Product.objects.select_related('drop')

    if query:
        products = products.filter(
            Q(name__icontains=query)
        )

    if drop_id:
        products = products.filter(drop_id=drop_id)

    products = products.order_by("-id").distinct()

    return render(request, 'adminpanel/producto/include/productos_table.html', {
        'products': products,
    })

# ====== Vista principal de Talentos ======

def talentos(request):

    talents = Talent.objects.all()

    data = {
        'talents': talents,
    }
    
    return render(request, 'adminpanel/talent/talent.html', data)

def talent_detail_json(request, pk):
    talent = get_object_or_404(Talent, pk=pk)
    data = {
        'full_name': talent.full_name,
        'brand_name': talent.brand_name,
        'specialty': talent.specialty,
        'location': talent.location,
        'registered': talent.created_at.strftime('%d/%m/%Y'),
        'biography': talent.biography,
        'contact_email': talent.contact_email,
        'phone_number': talent.phone_number,
        'is_verified': talent.is_verified,
        'image_url': talent.profile_image.url if talent.profile_image else '/static/img/default_avatar.png',
        'video_url': talent.video_url or '',
        'social_links': [
            {'platform': link.get_platform_display(), 'url': link.url}
            for link in talent.social_links.all()
        ]
    }
    return JsonResponse(data)


def talent_create(request):
    SocialLinkFormSet = modelformset_factory(
        TalentSocialLink, form=TalentSocialLinkForm, extra=1, can_delete=True
    )

    if request.method == 'POST':
        form = TalentForm(request.POST, request.FILES)
        formset = SocialLinkFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            talent = form.save()
            for social_form in formset:
                if social_form.cleaned_data and not social_form.cleaned_data.get('DELETE'):
                    social = social_form.save(commit=False)
                    social.talent = talent
                    social.save()
            messages.success(request, "✅ Talento creado con éxito.")
            return redirect('adminpanel:talento')

    else:
        form = TalentForm()
        formset = SocialLinkFormSet(queryset=TalentSocialLink.objects.none())

    return render(request, 'adminpanel/talent/talent_create.html', {
        'form': form,
        'formset': formset,
    })

def eliminar_talento(request, id):
    talent = get_object_or_404(Talent, id=id)
    if request.method == 'POST':
        talent.delete()
        messages.success(request, "Talento eliminado con éxito.")
        return redirect('adminpanel:talento')
    return redirect('adminpanel:talento')

# VISTAS DE DROPS


def drop_list(request):
    drops = Drop.objects.all()
    return render(request, 'drop/drop.html', {
        'drops': drops,
    })


def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order/order.html', {
        'orders': orders,
    })

def user_list(request):
    users = CustomUser.objects.all().order_by('-date_joined')
    return render(request, 'user/user.html', {
        'users': users,
    })