
from flask import Blueprint
from logging import getLogger

from app.common.settings import config
from app.shared.task import Task
from library.utils.decorator import retry, timeit

host, port = config['service']['ms'][0].split(':')
api_version = config['ms']['api_version']
api_name = 'account'
api_prefix = '/v{}/{}'.format(config['flask']['api_version'], api_name)
apis = Blueprint(api_name, __name__, url_prefix=api_prefix)

log = getLogger(__name__)
log.info('Listening on {}'.format(api_prefix))

@apis.route('/', methods=['POST'])
@timeit
@retry
def create(**kwargs):
    """
    create a new Account object
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dicts with keys:
                      account_id, user_id, name, url, api_token,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/account/'.format(host, port, api_version)
    return Task.forward(url, 'POST')

@apis.route('/list', methods=['PUT'])
@timeit
@retry
def get_active(**kwargs):
    """
    get active Account objects
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is a list of dicts with keys:
                      account_id, user_id, name, url, api_token,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/account/list'.format(host, port, api_version)
    return Task.forward(url, 'PUT')

@apis.route('/<account_id>', methods=['GET'])
@timeit
@retry
def get_by_id(account_id, **kwargs):
    """
    get existing Account object
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dict with keys:
                      account_id, user_id, name, url, api_token,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/account/{}'.format(host,
                                             port,
                                             api_version,
                                             account_id)
    return Task.forward(url, 'GET')

@apis.route('/<account_id>', methods=['PUT'])
@retry
@timeit
def update(account_id, **kwargs):
    """
    modify an existing Account object updating key, value pairs from form data
    assume validation of optional args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dict with keys:
                      account_id, user_id, name, url, api_token,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/account/{}'.format(host,
                                             port,
                                             api_version,
                                             account_id)
    return Task.forward(url, 'PUT')

@apis.route('/<account_id>', methods=['DELETE'])
@retry
@timeit
def delete(account_id, **kwargs):
    """
    delete an existing Account object updating key: deleted
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is an empty list
    """
    url = 'http://{}:{}/v{}/account/{}'.format(host,
                                             port,
                                             api_version,
                                             account_id)
    return Task.forward(url, 'DELETE')
