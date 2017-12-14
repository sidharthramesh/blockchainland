from django.db import models
from .bigchainland import get_transactions
from blockchainland.settings import gov_public_key
# Create your models here.
class CryptoUser(models.Model):
    name = models.CharField(max_length=200)
    public_key = models.CharField(max_length=200, unique=True)

class Land(models.Model):
    name = models.CharField(max_length=200)
    asset_id = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    def get_transactions(self):
        all_transactions = get_transactions(self.asset_id)
        return all_transactions
    
    def get_public_key(self, txn):
        return txn['outputs'][0]['public_keys'][0]
    
    def format_public_key(self,txn):
        public_key = self.get_public_key(txn)
        if public_key == gov_public_key:
            return 'Government'
        try:
            user = CryptoUser.objects.get(public_key=public_key)
            return "{} ({})".format(user.name,user.public_key)
        except:     
            return 'Not registered ({})'.format(public_key)
    
    def get_owner(self):
        last_txn = self.get_transactions()[-1]
        return self.format_public_key(last_txn)

    def format_create(self, txn):
        return "<b>Created</b> by Government"

    def format_transfer(self, txn):
        public_key = txn['outputs'][0]['public_keys'][0]
        price = txn.get('metadata','Not mentioned')
        if price is not None:
            price = price.get('price')
        else:
            price = 'Not disclosed'
        s = "<b>Transfered</b> to {}<br><b>Price:</b> {}".format(self.format_public_key(txn), price)
        return s

    def format_transactions(self):
        transactions = get_transactions(self.asset_id)
        all_formated = []
        for txn in transactions:
            op = txn.get('operation')
            if op == "CREATE":
                formated = self.format_create(txn)
            if op == "TRANSFER":
                formated = self.format_transfer(txn)
            all_formated.append(formated)
        print(all_formated)
        return all_formated
        
            

