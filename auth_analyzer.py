import csv
from os.path import join

def get_file(path_to_file):
    with open(path_to_file, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_total_attempts(file):
    extract_attempts = file
    total_attempts = 0
    for row in extract_attempts:
        total_attempts += 1
    return total_attempts

def get_success_count(file):
    extract_success = file
    total_success = 0
    for row in extract_success:
        if row["result"] == "OK":
            total_success += 1
    return total_success

def get_failure_count(file):
    extract_fail = file
    total_fail = 0
    for row in extract_fail:
        if row["result"] == "FAIL":
            total_fail += 1
    return total_fail

def get_unique_users(file):
    get_users = file
    users_logging_in = []
    for row in get_users:
        if row["user"] not in users_logging_in:
            users_logging_in.append(row["user"])
    return len(users_logging_in)

def get_unique_ip(file):
    get_ips = file
    ips_attempt = []
    for row in get_ips:
        if row["ip"] not in ips_attempt:
            ips_attempt.append(row["ip"])
    return len(ips_attempt)

def get_top_failed_users(file):
    get_users = file
    failed_login_attempts = {}
    for row in get_users:
        if row["result"] == "FAIL":
            if row["user"] not in failed_login_attempts:
                failed_login_attempts.update({row["user"]:1})
            else:
                failed_login_attempts[row["user"]] += 1
    return failed_login_attempts

def get_top_failed_ips(file):
    get_ips = file
    failed_ip_attempts = {}
    for row in get_ips:
        if row["result"] == "FAIL":
            if row["ip"] not in failed_ip_attempts:
                failed_ip_attempts.update({row["ip"]:1})
            else:
                failed_ip_attempts[row["ip"]] += 1
    return failed_ip_attempts

def sort_by_top(dictonary_to_sort):
    sorted_dictonary = {}
    for key in sorted(dictonary_to_sort, key=dictonary_to_sort.get, reverse=True):
        sorted_dictonary[key] = dictonary_to_sort[key]
    return sorted_dictonary



#def print_analysis(attempts, success, failure, users, ip, failed, lock, suspicious):

def main():
    file = get_file("test1.csv")
    attempts_login = get_total_attempts(file)
    success_login = get_success_count(file)
    failure_count = get_failure_count(file)
    unique_users = get_unique_users(file)
    unique_ip = get_unique_ip(file)
    top_failed_users = sort_by_top(get_top_failed_users(file))
    print(f"Total attempts: {attempts_login}")
    print(f"Total Success Count: {success_login}")
    print(f"Total Fail Count: {failure_count}")
    print(f"Total Unique Users: {unique_users}")
    print(f"Total Unique IP: {unique_ip}")
    print(f"failed users attempts: {top_failed_users}")


main()
