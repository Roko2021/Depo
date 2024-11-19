from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SaveData

# تعريف الـ view الذي يعالج النصوص المحفوظة
@csrf_exempt
def save_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        
        # معرفه هل النص موجود ولا لا
        if not SaveData.objects.filter(text=text).exists():
            # فى حاله عدم وجوده
            new_text = SaveData(text=text)
            new_text.save()
            return JsonResponse({'text': new_text.text}, status=200)
        else:
            # فى حاله وجوده
            return JsonResponse({'text': text}, status=200)

    elif request.method == 'GET':
        # الحصول على النصوص من الداتا بيز
        saved_texts = SaveData.objects.all()
        texts = [text.text for text in saved_texts]
        return JsonResponse({'texts': texts}, status=200)

def home(request):
    # فتح الصفحه الرئيسيه

    return render(request, 'home.html', )
