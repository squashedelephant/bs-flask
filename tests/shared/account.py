
from ujson import load

class Account:
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
    def get_new_account():
        fixture = '../../fixtures/account/new_account.json'
        return Account._load_fixture(fixture)
