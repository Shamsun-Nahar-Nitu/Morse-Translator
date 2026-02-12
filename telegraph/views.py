# telegraph/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .logic import translate_to_morse

def index(request):
    return render(request, 'index.html')

def download_telegram(request):
    if request.method == "POST":
        raw_text = request.POST.get('text', 'No Content')
        morse = translate_to_morse(raw_text)
        
        # Professional ASCII Telegram Header
        telegram_content = (
            "=========================================\n"
            "       VICTORIAN TELEGRAPH COMPANY       \n"
            "=========================================\n\n"
            f"MESSAGE: {raw_text}\n"
            f"SIGNAL:  {morse}\n\n"
            "-----------------------------------------\n"
            "STOP. END OF TRANSMISSION. STOP."
        )
        
        response = HttpResponse(telegram_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="telegram.txt"'
        return response