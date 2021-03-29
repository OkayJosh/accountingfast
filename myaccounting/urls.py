from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, OtherFinancialsViewSet, AccountInfoViewSet


router = DefaultRouter()
router.register('income', IncomeViewSet, basename='acc-income')
router.register('expense', ExpenseViewSet, basename='acc-expense')
router.register('others', OtherFinancialsViewSet, basename='acc-other')
router.register('info', AccountInfoViewSet, basename='acc-info')

urlpatterns = [
    
] + router.urls