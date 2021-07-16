from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path("url_check", views.url_check, name="url_check")
    ]

# t=1
# from time import sleep as sleep
# while t<=10:
#     try:
#         x=open("/Users/sa1/Desktop/Github Repos/DjangoPlayground/amazon_reviews/main_thing/t1.txt")
#         x.close()
#         print("File found. Breaking..")
#         break
#     except FileNotFoundError:
#         sleep(1)
#         print(f"Waiting. {t=}")
#         t+=1