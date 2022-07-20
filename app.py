# -*- coding: utf-8 -*-

import pickle
from flask import Flask, request

app = Flask(__name__)

classifier_model = pickle.load(open("mushrooms.pkl","rb"))

# http://localhost:5000/mushrooms_predict

@app.route("/mushrooms_predict" , methods = ['GET','POST'])
def index():
    return "CI CD pipeline has been established."
def api_predict():
        data = request.get_json()
                
        capshape = data['cap-shape']
        capsurface = data['cap-surface']
        capcolor = data['cap-color']
        bruises = data['bruises']
        odor = data['odor']
        gillattachment = data['gill-attachment']
        gillspacing = data['gill-spacing']
        gillsize = data['gill-size']
        gillcolor = data['gill-color']
        stalkshape = data['stalk-shape']
        stalkroot = data['stalk-root']
        stalk_surface_above_ring = data['stalk-surface-above-ring']
        stalk_surface_below_ring = data['stalk-surface-below-ring']
        stalk_color_above_ring = data['stalk-color-above-ring']
        stalk_color_below_ring = data['stalk-color-below-ring']
        veilcolor = data['veil-color']
        ringnumber = data['ring-number']
        ringtype = data['ring-type']
        spore_print_color = data['spore-print-color']
        population = data['population']
        habitat = data['habitat']


        input1 = np.array([[capshape,capsurface,capcolor,bruises,odor,gillattachment,gillspacing,gillsize,gillcolor,stalkshape,stalkroot,
                        stalk_surface_above_ring,stalk_surface_below_ring,stalk_color_above_ring,stalk_color_below_ring,veilcolor,
                        ringnumber,ringtype,spore_print_color,population,habitat]])

        prediction = classifier_model.predict(input1)
        return str(prediction)

if __name__ == '__main__':
        app.run(debug=True)


"""import requests
url = "http://localhost:5000/mushrooms_predict"
data = {
    'cap-shape' : 4,
    'cap-surface': 3,
    'cap-color': 8,
    'bruises': 1,
    'odor': 0,
    'gill-attachment': 1,
    'gill-spacing': 0,
    'gill-size': 1,
    'gill-color': 7,
    'stalk-shape': 1,
    'stalk-root': 3,
    'stalk-surface-above-ring': 3,
    'stalk-surface-below-ring': 3,
    'stalk-color-above-ring': 3,
    'stalk-color-below-ring': 3,
    'veil-color': 0,
    'ring-number': 1,
    'ring-type': 4,
    'spore-print-color': 7,
    'population': 4,
    'habitat': 6

}

r=requests.post(url, json=data)
print(r)
print(r.text)"""