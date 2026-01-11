
import json
import urllib.request
import urllib.parse
import os

def fetch_kathmandu_data():
    print("Fetching Kathmandu Bus Stops from Overpass API...")
    
    # Overpass Query
    query = """
    [out:json][timeout:25];
    (
      node["highway"="bus_stop"](around:5000,27.706,85.315);
    );
    out body;
    """
    
    url = "https://overpass-api.de/api/interpreter"
    data = urllib.parse.urlencode({'data': query}).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            
        print(f"Received {len(result.get('elements', []))} elements.")
        
        stations = []
        for element in result.get('elements', []):
            if element['type'] == 'node':
                name = element.get('tags', {}).get('name', 'Bus Stop')
                stations.append({
                    "name": name,
                    "lat": element['lat'],
                    "lng": element['lon'],
                    "osm_id": str(element['id'])
                })
        
        # Structure matching map.html expectation
        output = {
            "stations": stations,
            "city": "kathmandu",
            "count": len(stations)
        }
        
        # Ensure CityData directory exists in root
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        city_data_dir = os.path.join(base_dir, 'CityData')
        os.makedirs(city_data_dir, exist_ok=True)
        
        stations_file = os.path.join(city_data_dir, 'ktm_stations.json')
        with open(stations_file, 'w') as f:
            json.dump(output, f, indent=2)
            
        print(f"Saved {len(stations)} stations to {stations_file}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_kathmandu_data()
