from django.urls import path
from .views import CursoViewSet, WeekViewSet, CursoWeekViewSet,CursoRetrieveAPIView, UnitViewSet, UnitRetrieveAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('detallecurso/<int:id>', CursoWeekViewSet.as_view(), name='weekcurso'),
    path('curso', CursoViewSet.as_view(), name='curso'),
    path('curso/<int:id>', CursoRetrieveAPIView.as_view(), name='curso delete, update, search'),
    path('unit', UnitViewSet.as_view(), name='Unit'),
    path('unit/<int:id>', UnitRetrieveAPIView.as_view(), name='unit delete, update, search'),
    path('week', WeekViewSet.as_view(), name='curso'),
    
] 


