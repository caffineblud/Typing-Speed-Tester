import time


start_time = None


def start_timer():
    global start_time
    start_time = time.time()


def calculate_wpm(typed_text):
    if start_time is None:
        return 0

    elapsed_time = time.time() - start_time

    minutes = elapsed_time / 60

    if minutes == 0:
        return 0

    words = len(typed_text) / 5

    wpm = words / minutes

    return round(wpm)


def calculate_accuracy(original, typed):
    if len(typed) == 0:
        return 0

    correct_chars = 0

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(typed)) * 100

    return round(accuracy)