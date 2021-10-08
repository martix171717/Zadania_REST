# Zadania_REST

Module 9 

Task: Home Library


The library of series to watch

Keeps the list of series to watch with the titles, short descriptions and labels to mark is series already watched or not. It enables to add new series, update or delete selected series. 

The applications  is built on the basis of REST. The data returned by the API is in json format.


To import 

from flask import Flask, jsonify, abort, make_response, request

import json


REST API


Request

Get list of series:

GET  
http://[hostname]/api/v1.0/towatches  -->   to show the current list of series


Add new series:
POST   
http://[hostname]/api/v1.0/towatches/[towatch_id]    --> to  add new series to the list


Get details:
GET    
http://[hostname]/api/v1.0/towatches/[towatch_id]    --> to get details about selected series 


Delete series:
DELETE   
http://[hostname]/api/v1.0/towatches/[towatch_id]   -->  to delete selected series


Update series:
PUT
http://[hostname]/api/v1.0/towatches/[towatch_id]    -->  to update  selected series

