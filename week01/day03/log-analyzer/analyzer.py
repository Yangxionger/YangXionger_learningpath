def analyze_log(filename):
    dic = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()

            if not clean_line:
                continue

            parts = clean_line.split()
            log_type = parts[0]

            if log_type in dic:
                dic[log_type] += 1

    return dic