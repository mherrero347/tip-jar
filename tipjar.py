from time import sleep
from venmo_api import Client
from secrets import access_token
from gpiozero import LED

OUT_LED = 17


def light_up(led):
    print("thanks for the tip!! :)")

    for i in range(10):
        led.on()
        sleep(.1)
        led.off()
        sleep(.1)


def get_newest_transaction(venmo, me):
    return venmo.user.get_user_transactions(user=me, count=1).pop()


if __name__ == '__main__':
    venmo = Client(access_token=access_token)

    me = venmo.user.get_my_profile()
    first_id = get_newest_transaction(venmo, me).id

    led = LED(OUT_LED)

    print("Waiting for tips...")

    while True:
        newest = get_newest_transaction(venmo, me)

        if newest.id == first_id or newest.payment_type != 'pay' or newest.target.id != me.id:
            sleep(0.1)
            continue

        light_up(led)
        first_id = newest.id
