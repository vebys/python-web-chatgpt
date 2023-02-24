from django.views.generic import View
from django.shortcuts import render
from django.http.response import JsonResponse
import openai

class Chat(View):
  def get(self,request):
      return render(request,'openai_test/chat.html')


  def post(self,request):
    ask = request.POST['new_ask']
    # print(ask)
    openai.api_key = '你的openai api key'
    response = openai.Completion.create(
      model='text-davinci-003',
      prompt=ask,
      temperature=0.6,
      max_tokens=2048,
      top_p=1.0,
      frequency_penalty=1.0,
      presence_penalty=1.0,
    )
    # print(response)
    print(response.choices)
    print(response.choices[0].text)
    return JsonResponse({'code':0,'msg':response.choices[0].text})









