
from ujson import load

class PurchaseOrder:
    @staticmethod
    def _load_fixture(f):
        try:
            fh = open(f, 'r')
            d = load(fh)
            fh.close()
            return d
        except IOError as e:
            #print(e)
            exit('ERROR: unable to read fixture: {}'.format(f))

    @staticmethod
    def get_new_purchase_order():
        fixture = '../../fixtures/event/new_purchase_order.json'
        return PurchaseOrder._load_fixture(fixture)
