from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.product.models import Product
from apps.drop.models import Drop  # ← Solo necesitas Product
from django.db.models import Q
from apps.product.forms import ProductForm
from apps.product.models import ProductImage, ProductSize
from django.contrib import messages

# ====== Dashboard ======
@login_required
def dashboard(request):
    return render(request, 'adminpanel/dashboard/dashboard.html')

# ====== Vista principal de productos ======
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

# ====== Eliminar producto ======
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

    products = Product.objects.select_related( 'drop')

    if query:
        products = products.filter(
            Q(name__icontains=query) 
        )

    if drop_id:
        products = products.filter(drop_id=drop_id)

    return render(request, 'adminpanel/includes/producto/productos_table.html', {
        'products': products,
        
    })
