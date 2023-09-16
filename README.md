# scan_holiday_commits
Show Git commit history that occurred outside of work hours

# Conditions
Only the following commits will be outputted:
1. Jewish or Israeli Holiday (such as Rosh Ha'shana, Rosh Ha'shana eve)
2. Outside of working hours- 08:00-17:00
3. Weekends (Fridays or Saturdays)

# Example commit_dates.txt
```txt
2023-09-11 17:56:01 - Realized that change streams aren't supported in MongoDB timeseries collections. We're gonna have to use a regular collection and use create_index so that it's optimized for accessing by timestamp.
2023-09-11 09:38:20 - Added debug mode to watch (now need to open in a separate VS Code window)
2023-09-15 12:39:40 - Added useful functionality to DatabaseImpl: summarize
2022-12-18 13:37:08 - feature: create GUI setup
2022-12-17 19:12:12 - refactor: settings file
2022-12-17 18:48:41 - feature: add responsive layout to settings file
2022-12-17 18:09:55 - feature: add routing functionality to home page
2022-12-17 16:33:52 - feature: add settings card in landing page
2022-12-17 15:45:11 - Initial commit
```

# Example filtered_commit_dates.txt
```txt
2023-09-11 17:56:01 (Monday, NOT_HOLIDAY) - Realized that change streams aren't supported in MongoDB timeseries collections. We're gonna have to use a regular collection and use create_index so that it's optimized for accessing by timestamp.
2023-09-15 12:39:40 (Friday, Erev Rosh Hashana) - Added useful functionality to DatabaseImpl: summarize
2022-12-18 13:37:08 (Sunday, Chanukah: 1 Candle) - feature: create GUI setup
2022-12-17 19:12:12 (Saturday, NOT_HOLIDAY) - refactor: settings file
2022-12-17 18:48:41 (Saturday, NOT_HOLIDAY) - feature: add responsive layout to settings file
2022-12-17 18:09:55 (Saturday, NOT_HOLIDAY) - feature: add routing functionality to home page
2022-12-17 16:33:52 (Saturday, NOT_HOLIDAY) - feature: add settings card in landing page
2022-12-17 15:45:11 (Saturday, NOT_HOLIDAY) - Initial commit
```
Notice how the commit "Added debug mode to watch" doesn't exist in the outputted `filtered_commit_dates.txt` file, because it was done within working hours.
