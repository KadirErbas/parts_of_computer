from django.shortcuts import render

# Create your views here.

def anakart_view(request):
    anakart_dict={
        "anakartlar":{
            "1":{
                "name" : "GIGABYTE B650M S2H 6400(OC) DDR5 Soket AM5 M.2 HDMI DP D-Sub mATX Anakart",
                "price" : "3.788,40 ",
                "image_url": "https://img-itopya.mncdn.com/cdn/250/yeni-proje-2023-09-29t113240092-3df484.jpg"
                },
            "2":{
                "name" : "ASUS EX-B650M-V7 8000MHz(OC) DDR5 Soket AM5 M.2 HDMI mATX Anakart",
                "price" : "6.000,21",
                "image_url": "https://img-itopya.mncdn.com/cdn/250/yeni-proje-2023-09-22t111627711-b41a8a.jpg"
                },
            "3":{
                "name" : "ASUS EX-B650M-V7 8000MHz(OC) DDR5 Soket AM5 M.2 HDMI mATX Anakart",
                "price" : "6.000,21",
                "image_url": "https://img-itopya.mncdn.com/cdn/250/yeni-proje-2023-09-22t111627711-b41a8a.jpg"
                },
             "4":{
                "name" : "ASUS EX-B650M-V7 8000MHz(OC) DDR5 Soket AM5 M.2 HDMI mATX Anakart",
                "price" : "6.000,21",
                "image_url": "https://img-itopya.mncdn.com/cdn/250/yeni-proje-2023-09-22t111627711-b41a8a.jpg"
                },
                  "5":{
                "name" : "ASUS EX-B650M-V7 8000MHz(OC) DDR5 Soket AM5 M.2 HDMI mATX Anakart",
                "price" : "6.000,21",
                "image_url": "https://img-itopya.mncdn.com/cdn/250/yeni-proje-2023-09-22t111627711-b41a8a.jpg"
                },
                  "6":{
                "name" : "ASUS EX-B650M-V7 8000MHz(OC) DDR5 Soket AM5 M.2 HDMI mATX Anakart",
                "price" : "6.000,21",
                "image_url": "https://img-itopya.mncdn.com/cdn/250/yeni-proje-2023-09-22t111627711-b41a8a.jpg"
                },
                  "7":{
                "name" : "ASUS EX-B650M-V7 8000MHz(OC) DDR5 Soket AM5 M.2 HDMI mATX Anakart",
                "price" : "6.000,21",
                "image_url": "https://img-itopya.mncdn.com/cdn/250/yeni-proje-2023-09-22t111627711-b41a8a.jpg"
                },
            }
        }
    return render(request, 'parts_of_computer_app/anakart.html', context=anakart_dict)


def bilgisayar_kasalari_view(request):  
    return render(request, 'parts_of_computer_app/bilgisayar-kasalari.html')

def ekran_karti_view(request):    
    return render(request, 'parts_of_computer_app/ekran-karti.html')

def islemci_view(request):
    return render(request, 'parts_of_computer_app/islemci.html')

def ram_view(request):    
    return render(request, 'parts_of_computer_app/ram.html')

def home_view(request):    
    return render(request, 'parts_of_computer_app/home.html')
