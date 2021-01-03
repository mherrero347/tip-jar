from time import sleep
from venmo_api import Client
from secrets import access_token


def light_up():
    print("Thanks for the tip!! :)")


def get_newest_transaction(venmo, me):
    return venmo.user.get_user_transactions(user=me, count=1).pop()


if __name__ == '__main__':
    venmo = Client(access_token=access_token)

    me = venmo.user.get_my_profile()
    first_id = get_newest_transaction(venmo, me).id

    while True:
        newest = get_newest_transaction(venmo, me)

        if newest.id == first_id or newest.payment_type != 'pay' or newest.target.id != me.id:
            sleep(0.1)
            continue

        light_up()
        first_id = newest.id
