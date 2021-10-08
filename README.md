# Zadania_REST

Module 9 

Task: Home Library


The library of series to watch

Keeps the list of series to watch with the titles, short descriptions and labels to mark is series already watched or not. It enables to add new series, update or delete selected series. 

The applications  is built on the basis of REST. The data returned by the API is in json format.


To import 

from flask import Flask, jsonify, abort, make_response, request

import json



The structure of the project:

├── app.py

├── models.py

└── towatches.json

towatches.json – prepared file with initial series. The arguments are the same as  the dict constructor.
e.g.:

[{"id": 1, "title": "The Office", "description": "Sitcom television series that depicts the everyday work lives of office employees in the office of the paper company", "done": false}, {"id": 2, "title": "Game of Thrones", "description": "Series that tells the story of a medieval country's civil war", "done": true}, {"id": 3, "title": "Casa de Papel", "description": "Money Heist", "done": false}]


Attributes

![image](https://user-images.githubusercontent.com/89209334/136543093-fef45089-c3fb-4f0f-a1a3-a67899976e79.png)



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

