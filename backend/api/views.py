import json
from django.http import JsonResponse



def api_home(request,*args, **kwargs):
    print(request.GET) #url query paramets
    print(request.POST)
    body=request.body #byte string of json data
    data={}
    try:
        data = json.loads(body) #string of json data -> py dict
    except:
        pass
    print(data)
    #data['headers'] = request.headers
    print(request.headers)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)