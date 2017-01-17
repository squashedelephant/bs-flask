
from flask import Blueprint
from logging import getLogger

from app.common.settings import config
from app.shared.task import Task
from utils.decorator import retry, timeit

host, port = config['service']['ms'][1].split(':')
api_version = config['ms']['po_api_version']
api_name = 'po'
api_prefix = '/v{}/{}'.format(config['flask']['api_version'], api_name)
apis = Blueprint(api_name, __name__, url_prefix=api_prefix)

log = getLogger(__name__)
log.info('Listening on {}'.format(api_prefix))

@apis.route('/', methods=['POST'])
@timeit
@retry
def submit(**kwargs):
    """
    submit a new PurchaseOrder object
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dict with keys:
                      po_id, account_id, items, total, submitted,
                      filled, canceled
                  and items is a dict with keys: item_id, name, sku,
                      price, quantity
    """
    url = 'http://{}:{}/v{}/po/'.format(host,
                                        port,
                                        api_version)
    return Task.forward(url, 'POST')

@apis.route('/list', methods=['PUT'])
@timeit
@retry
def get_active(**kwargs):
    """
    get active PurchaseOrder objects
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is a list of dict with keys:
                      po_id, account_id, items, total, submitted,
                      filled, canceled
                  and items is a dict with keys: item_id, name, sku,
                      price, quantity
    """
    url = 'http://{}:{}/v{}/po/list'.format(host,
                                            port,
                                            api_version)
    return Task.forward(url, 'PUT')

@apis.route('/<po_id>', methods=['GET'])
@timeit
@retry
def get_by_id(po_id, **kwargs):
    """
    get existing PurchaseOrder object
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dict with keys:
                      po_id, account_id, items, total, submitted,
                      filled, canceled
                  and items is a dict with keys: item_id, name, sku,
                      price, quantity
    """
    url = 'http://{}:{}/v{}/po/{}'.format(host,
                                          port,
                                          api_version,
                                          po_id)
    return Task.forward(url, 'GET')

@apis.route('/<po_id>/update', methods=['PUT'])
@retry
@timeit
def update(po_id, **kwargs):
    """
    modify an existing PurchaseOrder object updating key, value pairs from form data
    assume validation of optional args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dict with keys:
                      po_id, account_id, items, total, submitted,
                      filled, canceled
                  and items is a dict with keys: item_id, name, sku,
                      price, quantity
    """
    url = 'http://{}:{}/v{}/po/{}/update'.format(host,
                                                 port,
                                                 api_version,
                                                 po_id)
    return Task.forward(url, 'PUT')

@apis.route('/<po_id>/cancel', methods=['PUT'])
@retry
@timeit
def cancel(po_id, **kwargs):
    """
    cancel an existing PurchaseOrder object updating key: canceled
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is an empty list
    """
    url = 'http://{}:{}/v{}/po/{}/cancel'.format(host,
                                                 port,
                                                 api_version,
                                                 po_id)
    return Task.forward(url, 'PUT')
