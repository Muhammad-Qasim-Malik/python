import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts <= max_retries:
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
    print("Attempt", attempts, wait_time)
