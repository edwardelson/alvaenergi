"""
Update Jakarta API

1. update puskesmas_jkt.html in templates/
2. return 1 cctv streaming data
"""

from flask import url_for, current_app
import os, requests, folium

def updateJKTAPI():
    app = current_app._get_current_object()

    # HEADERS
    headers = {"Authorization": app.config["JAKARTA_API_TOKEN"]}

    #===============
    # PUSKESMAS UPDATE HTML FILE
    #===============
    # puskesmas
    JAKGO_URL = "http://api.jakarta.go.id/v1/puskesmas"
    parameters = {}
    # GET Request
    response = requests.get(JAKGO_URL, params=parameters, headers=headers)
    data = response.json()

    # PUSKESMAS DISPLAY
    map_puskesmas = folium.Map(location=[ -6.2146200, 106.8650])

    for unit in data['data']:
        folium.Marker([unit['location']['latitude'], unit['location']['longitude']], popup=unit["nama_Puskesmas"]).add_to(map_puskesmas)

    # is this a good way to save html file?
    map_puskesmas.save('app/templates/puskesmas_jkt.html')

    #===============
    # CCTV UPDATE
    #===============
    # cctv
    JAKGO_URL = "http://api.jakarta.go.id/v1/cctvbalitower/"
    parameters = {}
    # GET Request
    response = requests.get(JAKGO_URL, params=parameters, headers=headers)
    data = response.json()

    # pick 1st link
    cctvbalitower = {'name':data["data"][0]["id_site"], 'url':data["data"][0]["url"]}

    return cctvbalitower
