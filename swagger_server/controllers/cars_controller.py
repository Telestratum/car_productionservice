import connexion
import six
import uuid
from pymongo import MongoClient
from flask import jsonify , request
import ast
import json
import logging,logging.config

from swagger_server.models.carsdetails import Carsdetails  # noqa: E501
from swagger_server.models.carsinfo import Carsinfo  # noqa: E501
from swagger_server.models.model200_car_deleted_response import Model200CarDeletedResponse  # noqa: E501
from swagger_server.models.model201_car_details_response import Model201CarDetailsResponse  # noqa: E501
from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server import util

cluster = MongoClient("localhost",27017)
carDatabase = cluster.carDatabase
cars = carDatabase.cars
car_orders = carDatabase.car_orders

logging.basicConfig(filename="newfile1.log",format="%(filename)s::%(levelname)s:%(message)s",level=logging.DEBUG)


def delete_car(vehicle_id):  # noqa: E501
    """delete_car

    To delete cars # noqa: E501

    :param vehicle_id: 
    :type vehicle_id: str

    :rtype: Model200CarDeletedResponse
    """
    try:
        
        if cars.find_one({"vehicle_id":vehicle_id}):
            cars.delete_one({"vehicle_id":vehicle_id})
            return "successfully deleted",200
        else:
            return "vehicle_id is Not Found",404
    except:
        return "Internal_server_error",500
        

def get_all_cars():  # noqa: E501
    """get_all_cars

    Get details of all cars # noqa: E501


    :rtype: Carsdetails
    """
    try:
        data = cars.find()
        data_list = []
        for i in list(data):
            i["_id"]=str (i["_id"])

            data_list.append(i)
        return data_list,200
    except:
        return "Inetrnal_server_error",500

def get_car_details(model_name):  # noqa: E501
    """get_car_details

    To fetch details of one specified car # noqa: E501

    :param model_name: 
    :type model_name: str

    :rtype: Carsinfo
    """
    try:
        if cars.find({"model_name":model_name}):
            data=cars.find({"model_name":model_name})
            data_list=[]
            for i in data:
                    i["_id"]=str(i["_id"])
                    data_list.append(i)
            return data_list,200
        else:
            return "model_name Not Found",404
    except:
        return "Internal_server_error",500

def post_car(body=None):  # noqa: E501
    """post_car

    Create a new cars # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Model201CarDetailsResponse
    """
    if connexion.request.is_json:
        # body = Carsinfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if cars.find_one({"order_id" : body['order_id']}):
                return "car is already created",401
            else:
                body.update({"vehicle_id" : (uuid.uuid4().hex)})
                cars.insert_one(body)
                return "cars Created", 200
        except:
            return "Internal_server_error",500