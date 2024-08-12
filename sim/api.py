from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from . models import SampleModel

api = NinjaAPI()


@api.get("/add")
def show(request):
    results = SampleModel.objects.all()
    return {"results": [{"id":result.id, "result": result.result} for result in results]}

@api.post("/sub")
def add(request, a: int, b: int):
    instance = SampleModel.objects.create(result=a + b)
    return {"result": instance.result}
