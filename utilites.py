import csv
from os.path import join
from tabulate import tabulate
from colorama import Fore, Style

# Opens the CSV file as read only and returns the list to be used in the other get functions
def get_file(path_to_file):
    with open(path_to_file, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

# Returns the total  count from all records in the CSV file
def get_total_attempts(file):
    extract_attempts = file
    total_attempts = 0
    for row in extract_attempts:
        total_attempts += 1
    return total_attempts

# Returns the total success count from all fail records in the CSV file
def get_success_count(file):
    extract_success = file
    total_success = 0
    for row in extract_success:
        if row["result"] == "OK":
            total_success += 1
    return total_success

# Returns the total file count from all fail records in the CSV file
def get_failure_count(file):
    extract_fail = file
    total_fail = 0
    for row in extract_fail:
        if row["result"] == "FAIL":
            total_fail += 1
    return total_fail

# Gets the unique user from the csv file using the ip colum
def get_unique_users(file):
    get_users = file
    users_logging_in = []
    for row in get_users:
        if row["user"] not in users_logging_in:
            users_logging_in.append(row["user"])
    return len(users_logging_in)

# Gets the unique IPs from the csv file using the ip colum
def get_unique_ip(file):
    get_ips = file
    ips_attempt = []
    for row in get_ips:
        if row["ip"] not in ips_attempt:
            ips_attempt.append(row["ip"])
    return len(ips_attempt)

# Gets failed users from the ip colum of the file and total counts
def get_failed_users(file):
    get_users = file
    failed_login_attempts = {}
    for row in get_users:
        if row["result"] == "FAIL":
            if row["user"] not in failed_login_attempts:
                failed_login_attempts.update({row["user"]:1})
            else:
                failed_login_attempts[row["user"]] += 1
    return failed_login_attempts

# Gets failed IPs from the ip colum of the file and total counts
def get_failed_ips(file):
    get_ips = file
    failed_ip_attempts = {}
    for row in get_ips:
        if row["result"] == "FAIL":
            if row["ip"] not in failed_ip_attempts:
                failed_ip_attempts.update({row["ip"]:1})
            else:
                failed_ip_attempts[row["ip"]] += 1
    return failed_ip_attempts

# Sorts the dictonaries returned by get functions filtering down to fail threshold
def sort_by_top(dictonary_to_sort):
    sorted_dictonary = {}
    fail_threshold = 3
    remove_below_threshold = []
    for key in sorted(dictonary_to_sort, key=dictonary_to_sort.get, reverse=True):
        sorted_dictonary[key] = dictonary_to_sort[key]
    
    for key, value in sorted_dictonary.items():
        if value < fail_threshold:
            remove_below_threshold.append(key)
    
    for key in remove_below_threshold:
        del sorted_dictonary[key]
    
    top_three = dict(list(sorted_dictonary.items())[:3])
    return top_three



def print_analysis(attempts, success, failure, users, ip, failed_users, failed_ips):
    # Header title
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== Login Attempt Analysis ==={Style.RESET_ALL}\n")

    # Summary stats table
    table = [
        ["Total Attempts", f"{Fore.YELLOW}{attempts}{Style.RESET_ALL}"],
        ["Total Success", f"{Fore.GREEN}{success}{Style.RESET_ALL}"],
        ["Total Failures", f"{Fore.RED}{failure}{Style.RESET_ALL}"],
        ["Unique Users", f"{Fore.MAGENTA}{users}{Style.RESET_ALL}"],
        ["Unique IPs", f"{Fore.MAGENTA}{ip}{Style.RESET_ALL}"],
    ]
    print(tabulate(table, headers=["Metric", "Count"], tablefmt="fancy_grid"))

    # Top  3 failed users
    print(f"\n{Fore.RED}{Style.BRIGHT}Top 3 Failed Users:{Style.RESET_ALL}")
    failed_users_table = [[user, count] for user, count in failed_users.items()]
    print(tabulate(failed_users_table, headers=["User", "Attempts"], tablefmt="grid"))

    # Top 3 failed IPs
    print(f"\n{Fore.RED}{Style.BRIGHT}Top 3 Failed IPs:{Style.RESET_ALL}")
    failed_ips_table = [[ip, count] for ip, count in failed_ips.items()]
    print(tabulate(failed_ips_table, headers=["IP Address", "Attempts"], tablefmt="grid"))
