from venmo_api import Client
from secrets import access_token


if __name__ == '__main__':
    # Get your access token. You will need to complete the 2FA process
    venmo = Client(access_token=access_token)

    
