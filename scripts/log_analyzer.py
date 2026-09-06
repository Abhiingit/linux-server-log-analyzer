import re
from collections import Counter

LOG_FILE = "data/server.log"
REPORT_FILE = "reports/python-analysis.txt"

status_codes = Counter()
total_requests = 0

with open(LOG_FILE, "r") as file:
    for line in file:
        match = re.search(r" (\d{3})$", line.strip())

        if match:
            status = match.group(1)
            status_codes[status] += 1
            total_requests += 1

successful = status_codes.get("200", 0)

error_codes = {
    code: count
    for code, count in status_codes.items()
    if code != "200"
}

total_errors = sum(error_codes.values())

with open(REPORT_FILE, "w") as report:
    report.write("PYTHON LOG ANALYSIS REPORT\n")
    report.write("=========================\n\n")

    report.write(f"Total Requests: {total_requests}\n")
    report.write(f"Successful Requests: {successful}\n")
    report.write(f"Total Errors: {total_errors}\n\n")

    report.write("STATUS CODE SUMMARY\n")
    report.write("-------------------\n")

    for code, count in sorted(status_codes.items()):
        report.write(f"{code}: {count}\n")

    report.write("\nERRORS BY TYPE\n")
    report.write("--------------\n")

    for code, count in sorted(error_codes.items()):
        report.write(f"{code}: {count}\n")

    if error_codes:
        most_common_error = max(error_codes, key=error_codes.get)
        report.write(
            f"\nMost Common Error: {most_common_error} "
            f"({error_codes[most_common_error]} occurrences)\n"
        )

print(f"Analysis complete. Report generated: {REPORT_FILE}")