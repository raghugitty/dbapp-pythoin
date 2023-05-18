import json
from django.shortcuts import HttpResponse

def Response(data, error=True,http_code=200,json_format=True):
    '''
    Json response function
    '''
    if error:
        status = 'ok'
    else:
        status = 'not_ok'
    response_data = {
        "data": data,
        "status": status,
    }
    if json_format:
        response=json.dumps(response_data)

    return HttpResponse(response, content_type='Application/json',status=int(http_code))

