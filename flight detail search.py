import requests
access_key = "74070f5c32d113f4c2601fe638efe119"
url="https://api.aviationstack.com/v1/flights"

flight= input("Enter airline:")
params = {
    "access_key": access_key,
    "airline_iata": flight
}
response = requests.get(url, params=params)
#querystring = {"access_key":access_key,"dep_iata":city}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    flights = data.get("data", [])
if not flights:
        print("No flights found for that airline.")
else:
        for f in flights[:5]:  # print only first 5 to keep it short
            print(f"Flight: {f['airline']['name']} {f['flight']['iata']} "
                  f"from {f['departure']['airport']} "
                  f"to {f['arrival']['airport']} "
                  f"Status: {f['flight_status']}")
        else:
          print("Error:", response.status_code, response.text)
    #print["data"]
    #print(flights)
    # for flight in flights:
        

        # print = data["name"]
#      = data["main"]["temp"]
#     weather = data["weather"][0]["description"]
#     print(f"Weather in {city}: {temp}°C, {weather}")
# else:
#     print("Error:", response.status_code, response.text)
 
print(response)