from django.shortcuts import render
from home.models import *

# Create your views here.
def adidas(request):
	sanpham = Sanpham.objects.filter(hang=1)
	context = {
		'thongtin' : sanpham
	}
	return render(request, "home/index.html", context)

def nike(request):
	sanpham = Sanpham.objects.filter(hang=3)
	context = {
		'thongtin' : sanpham
	}
	return render(request, "home/index.html", context)

def bitis(request):
	sanpham = Sanpham.objects.filter(hang=2)
	context = {
		'thongtin' : sanpham
	}
	return render(request, "home/index.html", context)

def non(request):
	sanpham = Sanpham.objects.filter(hang=4)
	context = {
		'thongtin' : sanpham
	}
	return render(request, "home/index.html", context)

def lienhe(request):
	return render(request,"khac/lienhe.html")

def gioithieu(request):
	return render(request,"khac/gioithieu.html")

def tuyendung(request):
	return render(request,"khac/tuyendung.html")

def vanchuyen(request):
	return render(request,"khac/vanchuyen.html")

def chinhsachbaohanh(request):
	return render(request,"khac/chinhsachbaohanh.html")

def doitaccungcap(request):
	return render(request,"khac/doitaccungcap.html")

def chinhsachdoitra(request):
	return render(request,"khac/chinhsachdoitra.html")

def detail(request, id):
	sanpham = Sanpham.objects.get(pk=id)
	context = {
		'thongtin' : sanpham
	}
	return render(request, "home/detail.html", context)

