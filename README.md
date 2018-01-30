# OSM Data from Overpass API

### Steps
1.  Download the data.  
* San Francisco  
In terminal, run the following commands
    - echo "data=[out:json][bbox:37.6040,-123.0137,37.8324,-122.3549];way[highway];(._;>;);out;" > query.osm
    - curl -o target.osm -X POST -d @query.osm "http://overpass-api.de/api/interpreter"
based on http://overpass-api.de/command_line.html
2. Run converter.py
3. Visulize in Sierra-Charlie