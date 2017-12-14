from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair, CryptoKeypair
from bigchaindb_driver.offchain import prepare_transfer_transaction
from time import sleep
url = 'https://test.ipdb.io'
tokens = {
    'app_id': '4fe9370d',
    'app_key': '1db08b277688e68153946a5d31da1c2e'
            }
db = BigchainDB(url,headers=tokens)

def create_land(owner, details):
    """Owner is a key pair. Details is a dictionary. Returns txid"""
    # prepare
    land = {'data':{'land':details}}
    prepared_creation_tx = db.transactions.prepare(
        operation='CREATE',
        signers=owner.public_key,
        asset=land)
    # fulfill
    fulfilled_creation_tx = db.transactions.fulfill(
        prepared_creation_tx, private_keys=owner.private_key)
    # send
    sent_creation_tx = db.transactions.send(fulfilled_creation_tx)
    txid = sent_creation_tx
    return txid
def transfer_land(asset_id, current_owner, new_owner, metadata=None):
    """New owner is a public key"""
    transfer_asset = {'id': asset_id}
    output_index = 0
    #output = asset['outputs'][output_index]
    transactions = db.transactions.get(asset_id=asset_id)
    #print(asset_id)
    #print(transactions)
    last_transaction_id = transactions[-1]['id']
    transfer_input = {
        'fulfillment': {
                    'public_key': current_owner.public_key,
                    'type': 'ed25519-sha-256'},
        'fulfills': {'output_index': output_index,'transaction_id': last_transaction_id,},
        'owners_before': [current_owner.public_key],}
    #print(current_owner)
    #print(new_owner)
    #prepare
    prepared_transfer_tx = db.transactions.prepare(operation='TRANSFER',
                                            asset=transfer_asset,
                                            inputs=transfer_input,
                                            metadata=metadata,
                                            recipients=new_owner,)
    #fulfill
    fulfilled_transfer_tx = db.transactions.fulfill(prepared_transfer_tx,
                                            private_keys=current_owner.private_key)
    #send
    txid = db.transactions.send(fulfilled_transfer_tx)
    return txid

def get_transactions(asset_id):
    transactions = db.transactions.get(asset_id=asset_id)
    return transactions

def pretty_print_transactions(asset_id):
    transactions = get_transactions(asset_id)
    for txn in transactions:
        print("{}:{}:{}".format(txn['operation'],txn['outputs'][0]['condition']['details']['public_key'],txn.get('metadata','')))
    print(('-'*60))
    print("Current Owner:{}".format(transactions[-1]['outputs'][0]['condition']['details']['public_key']))

