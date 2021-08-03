from django.shortcuts import render,redirect
from .models import Category,Pix

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        pixs = Pix.objects.all()
    else:
        pixs = Pix.objects.filter(category__name = category)
    categories = Category.objects.all()
    context = {'categories':categories,'pixs':pixs}
    return render(request,'pix/gallery.html',context)


def viewPix(request,pk):
    pix = Pix.objects.get(id=pk)
    return render(request,'pix/pix.html',{'pix':pix})


def addPix(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data ['category_new'] != '':
            category,created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None


        for image in images:
            pix = Pix.objects.create(
                category= category,
                description = data['description'],
                image = image,
            )
        return redirect('gallery')
    context = {'categories':categories}

    return render(request,'pix/add.html',context)    