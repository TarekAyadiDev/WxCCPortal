# Webex CC supervisor portal

This portal is an example of how you can enable a supervisor (from the Extended Supervisor Desktop), or a business representative from the web, to manage contact center branch opening hours, closing/alerting message, transfer etc, in a simple manner, without having to connect to the contact center administration portal or changing the call flow.

## Contacts
* Ayadi Tarek

## Solution Components
* Webex Contact Center
* Ngrok
* Flask
* Python
* HTML

## Installation/Configuration
The following commands are executed in the terminal.

1. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). 

2. (Optional) Set up a Python virtual environment. Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html). 

    2a. Create virutal environment example

        $ python3 -m venv BaseTemplatePortalv1
        $ source BaseTemplatePortalv1/bin/activate

    2b. Access the created virtual environment folder

        $ cd BaseTemplatePortalv1

3. Clone the repository

    3a. MAC

        $ git clone https://github.com/teakay101/WxCCPortal.git
        USername: teakay101
        Pwd: TOKEN (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)
        
    3b. Windows

You can download the Git bash from here : https://git-scm.com/downloads 
Use the following command : 

        $ git clone https://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@github.com/TarekAyadiDev/WxCCPortal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

If required, use the access token (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) to authenticate.

4. Access the folder `WxCCPortal`

        $ cd WxCCPortal

5. Install the dependencies:

        $ pip3 install -r requirements.txt

## Usage
1. To launch the app, type the following command in your terminal:

        $ python3 main.py

2. To access the app, navigate in a browser to `localhost:5002`. The GUI will look like the following and allow to determine the service information: 

![/IMAGES/GUI.png](/IMAGES/GUI.png)

3. In order to access the services information that was set from the GUI, follow the instructions found [here](https://ngrok.com/docs/getting-started/) to install ngrok agent. This will allow you to access your local service from anywhere. 

4. Once ngrok is setup, type the following command within your terminal:

        $ ngrok http 5002

5. You should see something similar to the following in your terminal, use the forwarding URL/status `url/status` within your Webex CC flow designer to access the service status (GET requests only).

![/IMAGES/ngrok.png](/IMAGES/ngrok.png)

#



# Screenshots

Once you submit a request, you get a confirmation of the changes made to the Contact Center branch

![/IMAGES/0image.png](/IMAGES/SubmittedClosure.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
