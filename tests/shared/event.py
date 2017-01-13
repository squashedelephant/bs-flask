
from ujson import load

class Event:
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
    def get_new_event():
        fixture = '../../fixtures/event/new_event.json'
        return Event._load_fixture(fixture)
