from django.contrib import admin

from .models import Income, Expense, OtherFinancials, AccountInfo

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(OtherFinancials)
admin.site.register(AccountInfo)

