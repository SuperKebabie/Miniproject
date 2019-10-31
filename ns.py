import http.client, urllib.parse, json

key = {'Ocp-Apim-Subscription-Key': 'fdc36c2430d041938b742ca56631d7d0'}

params = urllib.parse.urlencode({
    'maxJourneys': '25',
    'station': 'Ut'
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    print(data)
    conn.close()
except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))