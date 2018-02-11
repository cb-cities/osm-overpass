OSM-OVERPASS and SIERRA-CHARLIE Ubuntu installation guide
========

# 1. Start an Ubuntu Instance
- 1a.	Go to Amazon Web Service (AWS) – Cloud Computing Services
[https://aws.amazon.com](https://aws.amazon.com)
- 1b.	Sign in, launch a virtual machine with EC2, selecting an instance Ubuntu Server 16.04 LTS with the default “free tier eligible” settings 
- 1c.	When the instance is running, download and install MobaXterm to have the right terminal. Start the local terminal and run  
`ssh -i path/of/the/key/pair ubuntu@IPv4PublicIP`
to connect to the EC2 instance.

# 2. Downloading OSM Data from Overpass API
- 2a.	To clone Osm-overpass, type:  
`git clone https://github.com/cb-cities/osm-overpass.git`
- 2b. Inside osm-overpass, type:  
`echo "data=[out:json][bbox:37.6040,-123.0137,37.8324,-122.3549];way[highway];(._;>;);out;" > query.osm`  
`curl -o target.osm -X POST -d @query.osm "http://overpass-api.de/api/interpreter` based on http://overpass-api.de/command_line.html
- 2c. After downloading, we need to convert the `target.osm` data into the sierra-charlie (our visualizer) format. Now you have to install Python2.7 that is not present in this package, so type:  
`apt search python`  
`sudo apt install python`  
- 2d. Now you can run `converter.py`:  
`python converter.py`			
Now you have these two new files: `nodes1_drivable_graph.json` and `links1_drivable_graph.json`

# 3. Installing Sierra-Charlie (https://github.com/cb-cities/sierra-charlie)
- 3a.	Clone Sierra-Charlie:  
`git clone https://github.com/cb-cities/sierra-charlie.git`
- 3b. nside sierra charlie, run the following commands:  
		(Installing Nodejs and npm)  
`curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash –`  
`sudo apt-get install -y nodejs`  
		(Installing Purescript)  
`npm install purescript`  
    (Installing Yarn)  
`sudo npm install -g yarn`  
		(Installing Elm)  
`yarn add elm@0.16.0`  
`yarn install`  
- 3c. Now you need to prepare the data for sierra-charlie to visualize. THe data have been downloaded to `osm-overpass` and converted to `nodes1_drivable_graph.json` and `links1_drivable_graph.json`. In order for sierra-charlie to visualize them, the data files still need to be compressed, renamed and moved to the correct location.
Install gzip:  
`sudo apt-get update`  
`sudo apt-get install gzip`  
Go to `osm-overpass` to compress the data files:  
`gzip nodes1_drivable_graph.json`  
`gzip links1_drivable_graph.json`  
You need to rename the resulting files before moving them from `osm-overpass` to the `sierra-charlie` folder:  
`mv nodes1_drivable_graph.json.gz nodes1.json.gz`  
`mv links1_drivable_graph.json.gz links1.json.gz`  
`mv nodes1.json.gz ~/sierra-charlie/json`  
`mv links1.json.gz ~/sierra-charlie/json`  
You need also to move in the same way the file `defs.js` from `osm-overpass` to `sierra-charlie/src/js`:  
`mv defs.js ~/sierra-charlie/src/js`
- 3d.	Before starting with the visualization tool, you must modify the Instance security groups properties. Go to AWS Instance, check the “Security Group” properties at the right side of the instance bar, click on `launch-wizardX`, check `inbound`, click `edit` and `add rule` HTTP leaving the default settings.
- 3e.	Going back to `sierra-charlie`, to visualize the results you need to install `nginx`  
`sudo apt-get install nginx`
Open Google Chrome and type the Public DNS (IPv4) to check installation
- 3f. Go back to the terminal and run  
`sudo rm /etc/nginx/sites-enabled/default`  
`sudo nano /etc/nginx/sites-available/tutorial`  
Now inside this window paste:  

        ```server {
          listen 80;
          server_name tutorial;
          location / {
            proxy_set_header  X-Real-IP  $remote_addr;
           proxy_set_header  Host       $http_host;
            proxy_pass        http://127.0.0.1:3000;
          }
        }
        ```  

To save and close, type:  
`crtl + o`  
Enter  
`Crtl + x`  
`sudo ln -s /etc/nginx/sites-available/tutorial /etc/nginx/sites-enabled/tutorial`  
`sudo service nginx restart`  
- 3g. Now, you are ready to build the project, so run the following commands (inside sierra-charlie):  
`npm run build`  
`npm start`  
- 3h. Refresh the Google Chrome’s window where it was opened nginx, and you will see the San Francisco’s map.
- 3i. To close the session, type:  
`Crtl + c`  
`logout`



