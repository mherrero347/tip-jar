from time import sleep
from venmo_api import Client
from gpiozero import LED

OUT_LED = 17


def light_up():
    print("""
 ___________  __    __       __      _____  ___   __   ___   ________       _______   ______     _______       ___________  __    __    _______      ___________  __       _______   ___    ___       ____  ____
("     _   ")/" |  | "\     /""\    (\"   \|"  \ |/"| /  ") /"       )     /"     "| /    " \   /"      \     ("     _   ")/" |  | "\  /"     "|    ("     _   ")|" \     |   __ "\ |"  |  |"  |     ))_ ")(  " \
 )__/  \\__/(:  (__)  :)   /    \   |.\\   \    |(: |/   / (:   \___/     (: ______)// ____  \ |:        |     )__/  \\__/(:  (__)  :)(: ______)     )__/  \\__/ ||  |    (. |__) :)||  |  ||  |    (____(  \__. \
    \\_ /    \/      \/   /' /\  \  |: \.   \\  ||    __/   \___  \        \/    | /  /    ) :)|_____/   )        \\_ /    \/      \/  \/    |          \\_ /    |:  |    |:  ____/ |:  |  |:  |     _____     ) :)
    |.  |    //  __  \\  //  __'  \ |.  \    \. |(// _  \    __/  \\       // ___)(: (____/ //  //      /         |.  |    //  __  \\  // ___)_         |.  |    |.  |    (|  /    _|  /  _|  /      ))_ ") __/ //
    \:  |   (:  (  )  :)/   /  \\  \|    \    \ ||: | \  \  /" \   :)     (:  (    \        /  |:  __   \         \:  |   (:  (  )  :)(:      "|        \:  |    /\  |\  /|__/ \  / |_/ )/ |_/ )    (____( /"   /
     \__|    \__|  |__/(___/    \___)\___|\____\)(__|  \__)(_______/       \__/     \"_____/   |__|  \___)         \__|    \__|  |__/  \_______)         \__|   (__\_|_)(_______)(_____/(_____/           (____/
""")

    for i in range(10):
        led.blink()


def get_newest_transaction(venmo, me):
    return venmo.user.get_user_transactions(user=me, count=1).pop()


if __name__ == '__main__':
    venmo = Client(access_token=access_token)

    me = venmo.user.get_my_profile()
    first_id = get_newest_transaction(venmo, me).id

    led = LED(OUT_LED)

    while True:
        newest = get_newest_transaction(venmo, me)

        if newest.id == first_id or newest.payment_type != 'pay' or newest.target.id != me.id:
            sleep(0.1)
            continue

        light_up(led)
        first_id = newest.id
