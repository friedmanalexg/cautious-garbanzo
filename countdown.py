# Let's code a simple countdown timer
import time


def countdown(my_time):
    while my_time >= 0:
        mins, secs = divmod(my_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        my_time -= 1
    print("*Ding-ding-ding!*")


if __name__ == "__main__":
    my_time = int(input('Enter a countdown time in seconds: '))
    countdown(my_time)
