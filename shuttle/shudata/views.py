from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import provider
from serializers import providerSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def provider_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        providers = provider.objects.all()
        serializer = providerSerializer(providers, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = providerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def provider_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        providers = provider.objects.get(pk=pk)
    except provider.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = providerSerializer(providers)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = providerSerializer(providers, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        providers.delete()
        return HttpResponse(status=204)        
