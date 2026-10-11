import re

def slow_db_queries(filename, threshold):
    result = []
    malformed_count = 0

    with open(filename) as logfile:
        for line in logfile:

            if not re.search(r"\bDB_QUERY\b", line):
                continue

            pairs = re.findall(r"(\w+)=(\S+)", line)
            data = dict(pairs)

            try:
                name = data["name"]
                db = data["db"]
                duration = int(data["duration"])
                rows = int(data["rows"])
            except (KeyError, ValueError, TypeError):
                malformed_count += 1
                continue

            if duration >= threshold:
                result.append((name, db, duration))

    result.sort(key=lambda x: x[2], reverse=True)

    return result, malformed_count

print(slow_db_queries("log.dat", 13))

# handle quoted values
# r'(\w+)=(?:"([^"]*)"|(\S+))'