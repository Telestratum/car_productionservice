# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.carsdetails import Carsdetails  # noqa: E501
from swagger_server.models.carsinfo import Carsinfo  # noqa: E501
from swagger_server.models.model200_car_deleted_response import Model200CarDeletedResponse  # noqa: E501
from swagger_server.models.model201_car_details_response import Model201CarDetailsResponse  # noqa: E501
from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCarsController(BaseTestCase):
    """CarsController integration test stubs"""

    def test_delete_car(self):
        """Test case for delete_car

        
        """
        response = self.client.open(
            '/carservice/v1/cars/{vehicle_id}'.format(vehicle_id='c1632c60c1164404b23760d362f9b932'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_cars(self):
        """Test case for get_all_cars

        
        """
        response = self.client.open(
            '/carservice/v1/cars',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_car_details(self):
        """Test case for get_car_details

        
        """
        response = self.client.open(
            '/carservice/v1/cars/model_name/{model_name}'.format(model_name='model_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_car(self):
        """Test case for post_car

        
        """
        body = {
                "order_id": "6af804f1fa3d4976abafa9079d150e05"
                }
        response = self.client.open(
            '/carservice/v1/cars',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
