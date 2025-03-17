from django.http import HttpResponse, JsonResponse



def home_page(request):
    print("home page request")
    fruits = ["apple", "banana", "watermelon"]
    return JsonResponse(fruits, safe=False)
    # return HttpResponse("This is Home Page")
