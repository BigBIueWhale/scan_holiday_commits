import requests
import os
from datetime import datetime

# Fetch Jewish and Israeli holidays
def fetch_holidays(year):
    url = f"https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year={year}&month=x&ss=on&mf=on&c=on&geo=none&geonameid=293397&m=50&s=on"
    response = requests.get(url)
    data = response.json()
    holidays = {}
    for item in data["items"]:
        if item["category"] == "holiday":
            holiday_date = datetime.fromisoformat(item["date"]).date()
            holidays[holiday_date] = item["title"]
    return holidays

# Filter commits based on criteria
def filter_commits(lines, holidays):
    filtered_commits = []
    for line in lines:
        date_str, message = line.split(" - ", 1)
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        weekday = date_obj.weekday()
        time = date_obj.time()

        holiday_name = "NOT_HOLIDAY"

        # Check for holidays
        if date_obj.date() in holidays:
            holiday_name = holidays[date_obj.date()]
            filtered_commits.append((line.strip(), holiday_name))
            continue

        # Check for weekends
        if weekday in [4, 5]:  # Friday and Saturday
            filtered_commits.append((line.strip(), holiday_name))
            continue

        # Check for time outside of working hours
        if time < datetime.strptime("08:00:00", "%H:%M:%S").time() or time > datetime.strptime("17:00:00", "%H:%M:%S").time():
            filtered_commits.append((line.strip(), holiday_name))
            continue

    return filtered_commits

# Add weekdays and holidays to filtered commits
def add_weekdays_and_holidays(filtered_commits):
    result = []
    for line, holiday_name in filtered_commits:
        date_str, message = line.split(" - ", 1)
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        weekday_str = date_obj.strftime("%A")
        new_line = f"{date_str} ({weekday_str}, {holiday_name}) - {message}"
        result.append(new_line)
    return result

def main():
    # Check if commit_dates.txt exists, if not inform the user to generate it
    if not os.path.exists("commit_dates.txt"):
        print("commit_dates.txt not found.")
        print('Run the following command to generate commit_dates.txt:')
        print('git log --pretty=format:"%ad - %s" --date=format:"%Y-%m-%d %H:%M:%S" > commit_dates.txt')
        exit(1)

    # Fetch Jewish and Israeli holidays for the past 20 years
    holidays = {}
    current_year = datetime.now().year
    for year in range(current_year - 19, current_year + 1):
        holidays.update(fetch_holidays(year))

    # Read commit data from the file
    with open("commit_dates.txt", "r") as f:
        lines = f.readlines()

    # Filter commits based on conditions
    filtered_commits = filter_commits(lines, holidays)

    # Add weekdays and holidays to filtered commits
    result = add_weekdays_and_holidays(filtered_commits)

    # Write the filtered commits to a new text file
    with open("filtered_commit_dates.txt", "w") as f:
        for line in result:
            f.write(f"{line}\n")

if __name__ == "__main__":
    main()
