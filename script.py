from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

address = "127.0.0.1" # Local API IP address (if you work from another PC on the same network or a port is open in the router settings, you can access the local API remotely and this address will need to be changed)
port_from_settings_browser = '25325' # Local API port (can be found in the program settings)
chrome_driver_path = "chromedriver.exe" # Path to chromedriver for v110
ser = Service(chrome_driver_path) 
chrome_options = Options()
list_response = requests.get(f'http://{address}:{port_from_settings_browser}/list').json()['data'] # Send a request to the local API to get a list of profiles
profile_id = ''

for key, value in list_response.items(): # Loop through the list of profiles and run them one by one
        if value['folder'] == 'test': # Here you can add a check to run only the profiles you need (in this example, we run the profiles that are in the 'test' folder)
            profile_id = key
            if value['status'] == 'Available': # If the profile is not running, then run the profile and take the debug_port
                start_profile_response = requests.get(f'http://{address}:{port_from_settings_browser}/profile/start/{profile_id}', timeout=5).json()['data']
                debug_port = start_profile_response['debug_port']
            if value['status'] == 'Started': # If the profile is running, then we simply take the debug_port from the available data
                debug_port = value['debug_port']
            if value['status'] == 'Locked': # If the profile is Locked, then skip
                continue
            if debug_port: # We check if the browser has a connection port (WebEngine profiles doesnt have ports, so we close them immediately)
                chrome_options.debugger_address = f'{address}:{debug_port}'
                driver = webdriver.Chrome(service=ser, options=chrome_options, executable_path=chrome_driver_path)
                driver.get("https://whoer.net/") # Open whoer.net in active tab
                driver.switch_to.new_window('tab') # Create a new tab and switch to it
                driver.get(url='https://browserleaks.com/js') # Open browserleaks.com/js in active tab
                # You can add any other actions here      
            sleep(5) # Wait 5 sec
            requests.get(f'http://{address}:{port_from_settings_browser}/profile/stop/{profile_id}') # Stop profile
