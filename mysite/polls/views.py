import json
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

# view1 return  hello in web browser using template
def index(request):
	myname = "HuyDang"
	myasset = ["dienthoai","may tinh", 5,"Nha ngheo"]
	context = {"name":myname, "asset": myasset}
	return render(request, "polls/index.html", context)

# view2 return  hello in web browser
def haft(request):
	return render(request, "polls/addd/ckeditor.html")
# view2 return  hello in web browser using template

def jsonFileT(request):
	cwd = os.getcwd()
	file_path = os.path.join(cwd, 'polls\\templates\\polls\\addd\\cnv_2022_12_20_c5f712dbd100f70bdfcfg_de-so-1.json')
	with open(file_path, 'r') as file:
		data = file.read()
	return HttpResponse(data, content_type='application/json')

"""def haft(request):
    # Đường dẫn tuyệt đối đến tệp JSON
    # H:\3i-Intern\WarriorBuffaloMetalean\HuyData\djangoProject\editJsontoDatabase\mysite
    cwd = os.getcwd()
    relative_path = "cnv_2022_12_20_c5f712dbd100f70bdfcfg de-so-1.json"
    json_file_path = os.path.join(cwd, relative_path)
    with open(json_file_path) as file:
        data = json.load(file)
    return render(request, "polls/addd/ckeditor.html", {"data": json.dumps(data, ensure_ascii=True)})"""
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        image = request.FILES['upload']
        # Lưu trữ hình ảnh trong thư mục tải lên trên máy chủ
        upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        image_path = os.path.join(upload_path, image.name)
        with open(image_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        
        # Trả về URL của hình ảnh đã tải lên
        image_url = settings.MEDIA_URL + 'uploads/' + image.name
        return JsonResponse({'url': image_url})
    
    return JsonResponse({'error': 'Invalid request'})