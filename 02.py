TEST_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def is_safe_report(report):
    # if report[0] == report[1]: return False
    n = len(report)
    increasing = report[0] < report[1]
    for i in range(n - 1):
        if increasing and report[i] < report[i+1]  and 1 <= report[i+1] - report[i] <= 3:
            pass
        elif not increasing and report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3:
            pass
        else:
            return False
    return True


def is_safe_report_with_dampening(report):
    # if report[0] == report[1]: return False
    n = len(report)
    dampening_used = False
    i = 0
    while i < n - 1:
        if report[i] < report[i+1]  and 1 <= abs(report[i+1] - report[i]) <= 3:
            pass
        elif not dampening_used and i < (n - 2) and ((report[i] < report[i+2]  and 1 <= abs(report[i+2] - report[i]) <= 3) ^ (report[i+1] < report[i+2]  and 1 <= abs(report[i+2] - report[i+1]) <= 3)):
            dampening_used = True
            i += 1
        elif not dampening_used and i >= (n - 2):
            return True
        else:
            return False
        i += 1
    return True


inp = open("./02_input.txt").read()

reports = []
for line in inp.strip().split("\n"):
    reports.append(list(map(int, line.split())))

safe_reports_count = sum(1 for report in reports if is_safe_report(report))
print(safe_reports_count)

safe_reports_count2 = sum(1 for report in reports if is_safe_report(report) or any(map(is_safe_report, [report[0:i] + report[i+1:len(report)] for i in range(len(report))])))
print(safe_reports_count2)

#safe_reports_count = sum(1 for report in reports if is_safe_report_with_dampening(report) or is_safe_report_with_dampening(list(map(lambda x: x * -1, report))))
# safe_reports_count = sum(1 for report in reports if is_safe_report_with_dampening(report) or is_safe_report_with_dampening(report[::-1]))
# print(safe_reports_count)
