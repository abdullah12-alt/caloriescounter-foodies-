from django.shortcuts import render
import requests
import json
def home(request):
    if request.method=='POST':        
         query = request.POST['query']
         api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
         response = requests.get(api_url, headers={'X-Api-Key': 'KYzU6DBBR9Er5vOwP4OwDQ==0jrT0lyJoAiD1gDJ'})
        #  print(response.text)
         try:
             api =json.loads(response.content)
             print(response.content)
         except Exception as e:
             api='Oops there is an error'
             print(e)
        
         return render(request,'home.html',{'api':api})
    else:
         return render(request,'home.html',{'query':'you entered invalid query'})
             
    # if response.status_code == requests.codes.ok:
    # #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)
       
            