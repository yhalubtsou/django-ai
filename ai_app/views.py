import openai
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def generate_text(request):
    openai.api_key = settings.OPENAI_API_KEY

    if request.method == 'POST':
        prompt = request.POST.get('prompt', 'Say this is a test')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50
        )

        return JsonResponse({'response': response.choices[0].message['content']}, safe=False)

    return render(request, 'generate_text.html')
