VISUALIZER GUIDE for MacOS
======

### 1. Retrieving OpenStreetMap data from OSM-OVERPASS

##### Create OSM-OVERPASS folder  

Open terminal and run the following command to clone the OSM-OVERPASS repo from github:  

`git clone https://github.com/cb-cities/osm-overpass.git`  

This create a folder called “osm-overpass” with 3 files in it:
- converter.py  
- defs.js (define the boundaries of the map)  
- README.md

##### Retrieving data from OpenStreetMap
Change directory inside the `osm-overpass`. Run the following commands inside “osm-overpass”  folder. 

`echo "data=[out:json][bbox:37.6040,-123.0137,37.8324,-122.3549];way[highway];(._;>;);out;" > query.osm`  

[37.6040,-123.0137,37.8324,-122.3549] is the bounding box of the Bay Area. The above command create a file called `query.osm` (with 1 line of script inside).

`curl -o target.osm -X POST -d @query.osm "http://overpass-api.de/api/interpreter" based on http://overpass-api.de/command_line.html`  

This create a file called `target.osm` (nodes and links data of the Bay Area roads). However, the data inside `target.osm` need to be converted so as to be visualized in our visualizer [sierra-charlie](https://github.com/cb-cities/sierra-charlie). In order to do the conversion, `target.osm` needs to be in the same folder as `converter.py`, e.g., inside the “osm-overpass” folder:  
- converter.py
- defs.js
- README.md
- query.osm
- target.osm  

To run `converter.py`, the latest release of Python 2.7 needs to be installed, e.g., from the website [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/).

Run “converter.py”:  

`python converter.py`  

This command creates 2 files called `links1_drivable_graph.json` and `nodes1_drivable_graph.json` with the nodes and links data of the Bay Area road network inside and formated for sierra-charlie.  

Then, compress the 2 files with the `gzip`:  

`gzip links1_drivable_graph.json`  
`gzip nodes1_drivable_graph.json`



### 2. Visualzing network using SIERRA-CHARLIE  

Leave folder “osm-overpass” with the command `cd ..` and then run the command below to clone the sierra-charlie repo from github:  

`git clone https://github.com/cb-cities/sierra-charlie.git`    

Move or copy the two gzip files created in `osm-overpass` inside `sierra-charlie/json/` and RENAME THEM as:
- links1.json.gz
- nodes1.json.gz

Also, move or copy the file `osm-overpass/defs.js` to `../sierra-charlie/src/js/` and overwrite any existing file with the same name.

##### Installing SIERRA-CHARLIE

Based on the hard way documented in [sierra-charlie/README.md](https://github.com/cb-cities/sierra-charlie/blob/master/README.md)

Portions of the code are written in [PureScript](http://www.purescript.org/) and [Elm](http://elm-lang.org/).  Compilers for both languages and the [Node.js](https://nodejs.org/) runtime must be installed on the local machine.

The project is developed on OS X, but may support other UNIX platforms.  On OS X, system-level dependencies should be installed with the [`brew`](http://brew.sh/) tool.  

Install Homebrew (taken from the website: https://brew.sh)

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

Open the terminal and change directory inside `../sierra-charlie`. Run the following command to install `node.js` and `purescript`: 

`brew install node purescript`  

[Webpack](https://webpack.github.io/) is used to structure the project, supporting development and production mode builds.  ES2015 syntax is translated to JavaScript using [Babel](http://babeljs.io/).  Code quality is monitored using [JSHint](http://jshint.com/).

Use [`yarn`](https://yarnpkg.com/lang/en/) tool to install project-level dependencies.

This project was built for elm version `0.16`. `yarn` may be used to install it.  

`brew install yarn`  

`yarn add elm@0.16.0`  

The above commands create folder `node_modules`, `elm-stuff`, the file `package.json` and `yarn.lock`. 

Also increase the kernel limits on OS X.  

`sudo bash -c 'echo "kern.maxfiles=65536" >>/etc/sysctl.conf'`  

`sudo bash -c 'echo "kern.maxfilesperproc=65536" >>/etc/sysctl.conf'`  

`echo "ulimit -n 65536" >>~/.bash_profile`  

This may require you to restart your computer.  

##### Building, running and stopping SIERRA-CHARLIE

The same `npm` tool is also used to build the project, and to simplify other project-related tasks.  

To build the project, give the following command:  

`npm run build`

This creates the folder `out`, `build-artifacts` inside `elm-stuff`

If the build is successful, the project is ready to run:

`npm start`  

Finally, navigate to the following address in a web browser:  

`http://localhost:3000`  

Always in the end kill the process with: `control+C`  
For updating at the last version: `Git pull`  


