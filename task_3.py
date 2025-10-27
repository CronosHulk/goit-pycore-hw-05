import sys
from collections import Counter


def parse_log_line(line):
    parts = line.strip().split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }


def load_logs(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [parse_log_line(line) for line in file]
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)


def filter_logs_by_level(logs, level):
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))


def count_logs_by_level(logs):
    levels = [log['level'] for log in logs]
    return Counter(levels)


def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python task_3.py /шлях/до/logfile.log [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        print("Файл логів порожній або не вдалося його прочитати.")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        log_level_to_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level_to_filter)

        if filtered_logs:
            print(f"\nДеталі логів для рівня '{log_level_to_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписів з рівнем '{log_level_to_filter.upper()}' не знайдено.")


if __name__ == "__main__":
    main()
