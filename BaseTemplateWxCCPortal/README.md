# GVE Devnet REST Endpoint for Webex CC

## Contacts
* Roaa Alkhalaf

## Solution Components
* Webex Contact Center
* Ngrok
* Flask
* Python

## Installation/Configuration
The following commands are executed in the terminal.

1. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). 

2. (Optional) Set up a Python virtual environment. Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html). 

    2a. Access the created virtual environment folder

        $ cd your_venv

3. Clone this repository

        $ git clone https://wwwin-github.cisco.com/gve/gve_devnet_rest_endpoint_for_webex_cc.git


4. Access the folder `gve_devnet_rest_endpoint_for_webex_cc`

        $ cd gve_devnet_rest_endpoint_for_webex_cc

5. Install the dependencies:

        $ pip3 install -r requirements.txt

## Usage
1. To launch the app, type the following command in your terminal:

        $ python3 main.py

2. To access the app, navigate in a browser to `localhost:5000`. The GUI will look like the following and allow to determine the service information: 

![/IMAGES/GUI.png](/IMAGES/GUI.png)

3. In order to access the services information that was set from the GUI, follow the instructions found [here](https://ngrok.com/docs/getting-started/) to install ngrok agent. This will allow you to access your local service from anywhere. 

4. Once ngrok is setup, type the following command within your terminal:

        $ ngrok http 5000

5. You should see something similar to the following in your terminal, use the forwarding URL/status `url/status` within your Webex CC flow designer to access the service status (GET requests only).

![/IMAGES/ngrok.png](/IMAGES/ngrok.png)

#



# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.