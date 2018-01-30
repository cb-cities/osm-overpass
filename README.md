# OSM Data from Overpass API

### Steps
1.  Download the data.  
* San Francisco  
In terminal, run the following commands
    - echo "data=[out:json][bbox:37.6040,-123.0137,37.8324,-122.3549];way[highway];(._;>;);out;" > query.osm
    - curl -o target.osm -X POST -d @query.osm "http://overpass-api.de/api/interpreter"
based on http://overpass-api.de/command_line.html  
* Bay Area
bbox: 36.8931, -123.5337, 38.8643, -121.2082
    - echo "data=[out:json][bbox:36.8931, -123.5337, 38.8643, -121.2082][maxsize:3073741824];way[highway];(._;>;);out;" > query_bay.osm
    - curl -o target_bay.osm -X POST -d @query_bay.osm "http://overpass-api.de/api/interpreter"  
* Los Angeles
bbox: 32.8007, -118.9448, 34.8233, -117.6462
    - echo "data=[out:json][bbox:32.8007, -118.9448, 34.8233, -117.6462][maxsize:3073741824];way[highway];(._;>;);out;" > query_la.osm
    - curl -o target_la.osm -X POST -d @query_la.osm "http://overpass-api.de/api/interpreter"  
2. Run converter.py
3. Visulize in Sierra-Charlie