import sys

def analyze_log(file_path):
    error = 0
    warning = 0
    info = 0

    with open(file_path, 'r') as f:
        for line in f:
            if "ERROR" in line:
                error += 1
            elif "WARNING" in line:
                warning += 1
            elif "INFO" in line:
                info += 1

    print(f"Errors: {error}")
    print(f"Warnings: {warning}")
    print(f"Info: {info}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <logfile>")
    else:
        analyze_log(sys.argv[1])
