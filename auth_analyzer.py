import csv
import sys
from os.path import join
from tabulate import tabulate
from colorama import Fore, Style
from utilites import *

def main():
    file_path = sys.argv[1]
    file = get_file(file_path)
    attempts_login = get_total_attempts(file)
    success_login = get_success_count(file)
    failure_count = get_failure_count(file)
    unique_users = get_unique_users(file)
    unique_ip = get_unique_ip(file)
    top_failed_users = sort_by_top(get_failed_users(file))
    top_failed_ips = sort_by_top(get_failed_ips(file))


    print_analysis(
        attempts_login,
        success_login,
        failure_count,
        unique_users,
        unique_ip,
        top_failed_users,
        top_failed_ips
    )

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(f"Usage: python3 auth_analyzer.py <path_to_log_file>")
    print(f"Example: python3 auth_analyzer.py /path/to/log.csv")
else:
    main()
