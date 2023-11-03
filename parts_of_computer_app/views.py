from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.

def anakart_view(request):
    anakart = models.Product.objects.filter(category_id = 2)
    anakart_dict={"anakartlar":anakart}
    return render(request, 'parts_of_computer_app/anakart.html', context=anakart_dict)


def bilgisayar_kasalari_view(request):  
    bilgisayar_kasalari = models.Product.objects.filter(category_id = 5)
    bilgisayar_kasalari_dict={"bilgisayar_kasalari": bilgisayar_kasalari}   
    return render(request, 'parts_of_computer_app/bilgisayar-kasalari.html',context=bilgisayar_kasalari_dict)

def ekran_karti_view(request):
    ekran_karti = models.Product.objects.filter(category_id = 4)
    ekran_karti_dict={"ekran_kartlari": ekran_karti}       
    return render(request, 'parts_of_computer_app/ekran-karti.html',context=ekran_karti_dict)

def islemci_view(request):
    islemci = models.Product.objects.filter(category_id = 1)
    islemci_dict={"islemciler": islemci}
    return render(request, 'parts_of_computer_app/islemci.html', context= islemci_dict)

def ram_view(request):
    ram = models.Product.objects.filter(category_id = 3)
    ram_dict={"rams": ram}    
    return render(request, 'parts_of_computer_app/ram.html', context= ram_dict)

def islemci_sogutucular_view(request):
    sogutucu = models.Product.objects.filter(category_id = 6)
    sogutucu_dict={"sogutucular": sogutucu}    
    return render(request, 'parts_of_computer_app/sogutucular.html', context= sogutucu_dict)

def kasa_fanlari_view(request):
    kasa_fanlari = models.Product.objects.filter(category_id = 7)
    kasa_fanlari_dict={"kasa_fanlari": kasa_fanlari}    
    return render(request, 'parts_of_computer_app/kasa-fanlari.html', context= kasa_fanlari_dict)

def termal_macun_view(request):
    termal_macun = models.Product.objects.filter(category_id = 8)
    termal_macun_dict={"termal_macunlar": termal_macun}    
    return render(request, 'parts_of_computer_app/termal-macun.html', context= termal_macun_dict)

def klavye_view(request):
    klavyeler = models.Product.objects.filter(category_id = 9)
    klavyeler_dict={"klavyeler": klavyeler}    
    return render(request, 'parts_of_computer_app/klavye.html', context= klavyeler_dict)

def monitor_view(request):
    monitorler = models.Product.objects.filter(category_id = 10)
    monitorler_dict={"monitorler": monitorler}    
    return render(request, 'parts_of_computer_app/monitor.html', context= monitorler_dict)

def mouse_view(request):
    mouse = models.Product.objects.filter(category_id = 11)
    mouse_dict={"mouseler": mouse}    
    return render(request, 'parts_of_computer_app/mouse.html', context= mouse_dict)

def home_view(request):
    

    """
    if request.method == "GET":
        aranan_metin = request.GET.get('search')
        print(aranan_metin)
        return HttpResponse(f'Aranan metin: {aranan_metin}')
    else:
        """
    products = models.Product.objects.all()
    products_dict = {"products": products}
    return render(request, 'parts_of_computer_app/home.html',context=products_dict)
