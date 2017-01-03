import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from oauth2client.client import AccessTokenCredentials
from apiclient import discovery
import httplib2

access_token = "YOUR_ACCESS_TOKEN"
credentials = AccessTokenCredentials(access_token,'my-user-agent/1.0')
http = httplib2.Http()
http = credentials.authorize(http)

service = discovery.build('admin', 'directory_v1', http=http)
print('Getting the first 10 users in the domain')
results = service.users().list(customer='my_customer', maxResults=10,orderBy='email').execute()
users = results.get('users', [])

if not users:
    print('No users in the domain.')
else:
    print('Users:')
    for user in users:
    	print('{0} ({1})'.format(user['primaryEmail'],user['name']['fullName']))


