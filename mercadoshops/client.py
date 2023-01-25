import requests
from mercadoshops import exceptions


class Client(object):
    def __init__(self, access_token):
        self.base_url = 'https://api.mercadolibre.com'
        self.access_token = access_token

    def user_info (self, params=None):
        """List of customers which match a specified criteria. This call returns an array of objects.

        Args:
            params:

        Returns:

        """
        return self._get('users/me', params=params)

    def customers_list(self, params=None):
        """List of customers which match a specified criteria. This call returns an array of objects.

        Args:
            params:

        Returns:

        """
        return self._get('shops/cda/customers', params=params)

    def products_list(self, site_id, params=None):
        """List of products that match specified search criteria. This call returns an array of objects

        Args:
            params:

        Returns:

        """
        return self._get(f'/users/{site_id}/items/search', params=params)

    def orders_list(self, params=None):
        """List of orders that match specified search criteria. This call returns an array of objects.

        Args:
            params:

        Returns:

        """
        return self._get('shops/cda/customers', params=params)

    def _get(self, url, **kwargs):
        return self._request('GET', url, **kwargs)

    def _request(self, method, endpoint, headers=None, **kwargs):
        _headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        if headers:
            _headers.update(headers)
        return self._parse(requests.request(method, self.base_url + endpoint, headers=_headers, **kwargs))

    def _parse(self, response):
        status_code = response.status_code
        if 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            r = response.text
        if status_code in (200, 201, 202):
            return r
        elif status_code == 204:
            return None
        elif status_code == 400:
            raise exceptions.BadRequestError(r)
        elif status_code == 401:
            raise exceptions.UnauthorizedError(r)
        elif status_code == 403:
            raise exceptions.ForbiddenError(r)
        elif status_code == 404:
            raise exceptions.NotFoundError(r)
        elif status_code == 405:
            raise exceptions.NotAllowedError(r)
        elif status_code == 406:
            raise exceptions.NotAcceptableError(r)
        elif status_code == 500:
            raise exceptions.SystemError(r)
        else:
            raise exceptions.UnknownError(r)
