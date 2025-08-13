Just a simple python script that takes a csv file and then does some analysing of data. 

Threw togather as part of a daily coding challenge after a starting to learn Python.

Example usage: python3 auth_analyzer.py <path_to_log_file>

csv format:
ts	user	ip	result
2025-08-10T09:00:00	alice	10.0.0.1	FAIL
2025-08-10T09:01:00	alice	10.0.0.1	FAIL

Example output:

=== Login Attempt Analysis ===

╒════════════════╤═════════╕
│ Metric         │   Count │
╞════════════════╪═════════╡
│ Total Attempts │      27 │
├────────────────┼─────────┤
│ Total Success  │       9 │
├────────────────┼─────────┤
│ Total Failures │      18 │
├────────────────┼─────────┤
│ Unique Users   │       7 │
├────────────────┼─────────┤
│ Unique IPs     │       6 │
╘════════════════╧═════════╛

Top 3 Failed Users:
+--------+------------+
| User   |   Attempts |
+========+============+
| fred   |          5 |
+--------+------------+
| cara   |          4 |
+--------+------------+
| anna   |          3 |
+--------+------------+

Top 3 Failed IPs:
+--------------+------------+
| IP Address   |   Attempts |
+==============+============+
| 192.168.0.11 |          5 |
+--------------+------------+
| 192.168.0.14 |          5 |
+--------------+------------+
| 192.168.0.12 |          4 |
+--------------+------------+


