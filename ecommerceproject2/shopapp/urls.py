from django.urls import path

from . import views
app_name='shopapp'
urlpatterns = [
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/',views.AllProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='ProdCatDetail'),
]