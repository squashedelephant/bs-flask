
from flask import Blueprint
from logging import getLogger

from app.common.settings import config
from app.shared.task import Task
from library.utils.decorator import retry, timeit

host, port = config['service']['ms'][0].split(':')
api_version = config['ms']['api_version']
api_name = 'event'
api_prefix = '/v{}/{}'.format(config['flask']['api_version'], api_name)
apis = Blueprint(api_name, __name__, url_prefix=api_prefix)

log = getLogger(__name__)
log.info('Listening on {}'.format(api_prefix))

@apis.route('/', methods=['POST'])
@timeit
@retry
def create(**kwargs):
    """
    create a new Event object
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dicts with keys:
                      event_id, account_id, user_id, action, message,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/event/'.format(host, port, api_version)
    return Task.forward(url, 'POST')

@apis.route('/list', methods=['PUT'])
@timeit
@retry
def get_active(**kwargs):
    """
    get active Event objects
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is a list of dicts with keys:
                      event_id, account_id, user_id, action, message,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/event/list'.format(host, port, api_version)
    return Task.forward(url, 'PUT')

@apis.route('/<event_id>', methods=['GET'])
@timeit
@retry
def get_by_id(event_id, **kwargs):
    """
    get existing Event object
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dict with keys:
                      event_id, account_id, user_id, action, message,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/event/{}'.format(host,
                                             port,
                                             api_version,
                                             event_id)
    return Task.forward(url, 'GET')

@apis.route('/<event_id>', methods=['PUT'])
@retry
@timeit
def update(event_id, **kwargs):
    """
    modify an existing Event object updating key, value pairs from form data
    assume validation of optional args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is another dict with keys:
                      event_id, account_id, user_id, action, message,
                      status, created, retired, deleted
    """
    url = 'http://{}:{}/v{}/event/{}'.format(host,
                                             port,
                                             api_version,
                                             event_id)
    return Task.forward(url, 'PUT')

@apis.route('/<event_id>', methods=['DELETE'])
@retry
@timeit
def delete(event_id, **kwargs):
    """
    delete an existing Event object updating key: deleted
    assume validation of mandatory args occurs downstream to ease future
    code maintenance
    return value: JSON dict with keys: data, status_code, reason 
                  where data is an empty list
    """
    url = 'http://{}:{}/v{}/event/{}'.format(host,
                                             port,
                                             api_version,
                                             event_id)
    return Task.forward(url, 'DELETE')
