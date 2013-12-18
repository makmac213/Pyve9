__author__ = 'Mark Allan B. Meriales'
__email__ = 'mark.meriales@gmail.com'

FIVE9_API_USER_SETTINGS = {
    'username' : 'your@username.com',
    'password' : 'your_very_hard_to_guess_password',
    'email' : 'your@email.com',
}

FIVE9_WSDL = 'https://api.five9.com/wsadmin/v2/AdminWebService?wsdl&user=%s' % FIVE9_API_USER_SETTINGS['email']
