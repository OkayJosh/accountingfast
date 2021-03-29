from django.db import models
from .test_account_info import client

class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.amount}'

class Income(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    comment = models.TextField()  

    def __str__(self):
        return f'{self.name}, {self.amount}'  

class OtherFinancials(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    comment = models.TextField()  

    def __str__(self):
        return f'{self.name}, {self.amount}'  

class AccountInfo(models.Model):
    bitcoin = models.CharField(max_length=200)
    etherum = models.CharField(max_length=200)

accountinfo = AccountInfo.objects.create(etherum=client.get_asset_balance(asset='ETH'), bitcoin=client.get_asset_balance(asset='BTC'))