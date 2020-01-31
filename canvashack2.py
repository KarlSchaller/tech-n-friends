from apiclient import discovery
import requests
import uuid

API_KEY = r'AIzaSyD4zSxpZpQf7CJ2C0ng3IAyZbM_dbfEVsM'
drive_service = discovery.build('drive', 'v3', developerKey=API_KEY)
print(drive_service)

#URL = "https://www.googleapis.com/admin/directory/v1/groups"

URL = 'https://www.googleapis.com/admin/directory/v1/groups'
PARAMS = {'email':'canvashack@gmail.com', 'name':'Class Name Here'}
scope = 'https://www.googleapis.com/auth/admin.directory.group'
response = requests.post(url = URL, params = PARAMS)
print(response)
print(response.json())

'''team_drive_metadata = {'name': 'Project Resources'}
request_id = str(uuid.uuid4())
team_drive = drive_service.teamdrives().create(body=team_drive_metadata,
                                               requestId=request_id,
                                               fields='id').execute()
print ('Team Drive ID: %s' % team_drive.get('id'))'''
