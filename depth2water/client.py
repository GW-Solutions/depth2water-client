import json
import logging
from urllib.parse import urlunparse

import requests


logger = logging.getLogger(__name__)
log_debug = logger.debug
log_info = logger.info
log_warning = logger.warning
log_error = logger.error


def create_client(username, password, client_id, client_secret, *, host='localhost:8000', scheme='http'):
    client = Depth2WaterClient(username, password, client_id, client_secret, host=host, scheme=scheme)
    client.get_and_set_token()
    client.get_and_set_user()
    log_info(f'Created client: {client}')
    return client


class Depth2WaterClient:
    """Main client class for depth2water API"""

    TOKEN_PATH = '/o/token/'
    FILE_UPLOAD_PATH = '/api/v1/upload/groundwater'
    SOURCE_FILE_PATH = '/api/v1/sourcefile/'
    CURRENT_USER_PATH = '/api/user/'
    USER_DETAIL_PATH = '/api/v1/users/{}/'
    STATION_PATH = '/api/v1/stations/'
    TIME_SERIES_PATHS = {
        'GROUNDWATER': '/api/v1/groundwater/',
        'SURFACE_WATER': '/api/v1/surfacewater/',
        'CLIMATE': '/api/v1/climate/'
    }


    def __init__(self, username, password, client_id, client_secret, *, host='localhost:8000', scheme='http'):
        self._username = username
        self._password = password
        self._client_id = client_id
        self._client_secret = client_secret
        self._host = host
        self._scheme = scheme
        self._token = None
        self._user_id = None

    def __str__(self):
        return f'<Depth2WaterClient: {self._username}>'



    def _request_response_handler(func):
        def wrapper(self, *args, **kwargs):
            if 'headers' in kwargs:
                kwargs['headers'].update({'Authorization': f'Bearer {self._token}'})
            else:
                kwargs['headers'] = {'Authorization': f'Bearer {self._token}'}
            response = func(self, *args, **kwargs)
            if response.status_code > 204:
                log_info(f'Got response with status: {response.status_code} - {response.text}')
                response.raise_for_status()
            else:
                log_info(f'Got response with status: {response.status_code} - {response.text}')
            return response
        return wrapper

    @_request_response_handler
    def post(self, *args, **kwargs):
        return requests.post(*args, **kwargs)

    @_request_response_handler
    def get(self, *args, **kwargs):
        return requests.get(*args, **kwargs)

    def get_and_set_token(self):
        resp = self.post(
            self._build_url(self.TOKEN_PATH), data=self._get_login_data(), auth=(self._client_id, self._client_secret))
        self._token = resp.json()['access_token']
        log_debug(f'Got client access token {self._token}')
        return self._token

    def get_and_set_user(self):
        response = self.get(self._build_url(self.CURRENT_USER_PATH))
        user = response.json()
        log_debug(f'Got current user {user}')
        self._user_id = user['id']
        return self._user_id

    def post_csv_file(self, filename, mappings):
        if not mappings['owner']:
            mappings['owner'] = self._user_id
        mappings['owner'] = self._build_url(self.USER_DETAIL_PATH.format(mappings['owner']))
        log_info("OWNER URL {}".format(mappings["owner"]))
        log_info(f'POST {filename} to {self._build_url(self.FILE_UPLOAD_PATH)}')
        with open(filename, 'r') as f:
            files = {'blob': f}
            response = self.post(self._build_url(self.FILE_UPLOAD_PATH), files=files, data=mappings)
            if response.status_code != 201:  # this isn't ideal
                raise Exception(response.text)
        return response
    
    def create_station(self, mappings):
        if not mappings['owner']:
            mappings['owner'] = self._user_id
        mappings['owner'] = self._build_url(self.USER_DETAIL_PATH.format(mappings['owner']))
        log_info("OWNER URL {}".format(mappings["owner"]))
        response = self.post(self._build_url(self.STATION_PATH), data=mappings)
        return response.json()
    
    def get_station_by_station_id(self, station_id):
        return self.get_station_by_value('station_id', station_id)

    def get_station_by_value(self, column, value):
        search_params = [
            {'operator': '', 'column': column, 'searchTerm': value, 'orderBy': '', 'direction': ''}]
        resp = self._get_searchable(self.STATION_PATH, search_params)
        results = resp.json().get('results', [])
        return results

    def get_groundwater_data(self, station_id=None, start_date=None, end_date=None):
        return self.get_time_series_data(
            'GROUNDWATER', station_id=station_id, start_date=start_date, end_date=end_date)

    def get_surface_water_data(self, station_id=None, start_date=None, end_date=None):
        return self.get_time_series_data(
            'SURFACE_WATER', station_id=station_id, start_date=start_date, end_date=end_date)

    def get_climate_data(self, station_id=None, start_date=None, end_date=None):
        return self.get_time_series_data(
            'CLIMATE', station_id=station_id, start_date=start_date, end_date=end_date)

    def get_time_series_data(self, monitoring_type, station_id=None, start_date=None, end_date=None):
        path = self.TIME_SERIES_PATHS[monitoring_type.upper()]
        search_params = []
        if station_id:
            search_params.append({
                'operator': '',
                'column': 'station.station_id',
                'searchTerm': station_id,
                'orderBy': False,
                'direction': ''})
        if start_date:
            search_params.append({
                'operator': 'gte',
                'column': 'datetime',
                'searchTerm': start_date,
                'orderBy': True,
                'direction': 'asc'})
        if end_date:
            search_params.append({
                'operator': 'lte',
                'column': 'datetime',
                'searchTerm': end_date,
                'orderBy': False,
                'direction': ''})
        resp = self._get_searchable(path, search_params=search_params)
        results = resp.json().get('results', [])
        return results



    def _get_searchable(self, path, search_params=[]):
        return self.get(self._build_url(path), params={'searchParams': json.dumps(search_params)})

    def _build_url(self, path):
        return urlunparse((self._scheme, self._host, path, '', '', ''))

    def _get_login_data(self):
        return {
            'grant_type': 'password',
            'username': self._username,
            'password': self._password}


