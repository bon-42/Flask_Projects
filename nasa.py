from flask import Flask
import requests, json
from requests import Response


app = Flask(__name__)

@app.route('/')
def home():
    #ToDo: the "keywords" needs to be a user input
    response = requests.get('https://images-api.nasa.gov/search?keywords=mars&media_type=image')

    #convert response object to json
    results_as_json = response.json()

    #the response json is a dict and each image and their desciptions are
    #burried under a list i.e. "items"
    items = results_as_json['collection']['items']

    #empty list where we will store the filtered data
    # in a dict form
    details = []
    ##iterate through the items from json to get to  the image. Usually it's set to 100 images
    #for each item get the respective info i.e. nasa_id, image_desciption and image_link
    #more can be extracted as needed in the future
    #In the case of api change in the future, this is where we will need to update
    for item in items:      
        data = item.get('data')
        links = item.get('links')
        #create a dict of each detail info that we want to add to the list 
        image_detail = {'title': data[0]['title'], 'description':data[0]['description'],'date_created':data[0]['date_created'], 'image':links[0]['href']}
        details.append(image_detail)
        response_json = json.dumps(details)
    return response_json
