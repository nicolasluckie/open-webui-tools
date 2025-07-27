# Time Calculator Tool

A comprehensive time calculation tool for Open WebUI that provides natural language time operations, duration calculations, and timestamp conversions.

## Tool Information

- **Name:** Time Calculator
- **ID:** `time_calculator`
- **Version:** 1.0.0
- **Author:** Nicolas Luckie
- **Repository:** https://github.com/nicolasluckie/open-webui-tools

## Description

The Time Calculator is a powerful tool that enables users to perform various time-related calculations using natural language queries. It can add or subtract durations from specific times, calculate differences between dates, convert between time units, and parse human-readable time expressions into precise timestamps.

## Features

### 🕐 Natural Language Time Parsing
- Parse queries like "calculate the time 2 hours from now. the current time is 12:55 PM"
- Automatically extract base times and durations from conversational text
- Support for both 12-hour (AM/PM) and 24-hour time formats

### ➕ Time Addition & Subtraction
- Add or subtract durations from any base time
- Support for years, months, weeks, days, hours, minutes, and seconds
- Handle edge cases like month overflow and day transitions

### 📊 Time Difference Calculations
- Calculate precise differences between two dates/times
- Display results in multiple formats (seconds, minutes, hours, days)
- Show direction and magnitude of time differences

### 🔄 Duration Conversions
- Convert between different time units
- Support for complex durations (e.g., "2 hours 30 minutes")
- Approximate calculations for months and years

### 🌐 Timestamp Operations
- Convert natural language to Unix timestamps
- Parse various date formats (YYYY-MM-DD, MM/DD/YYYY, etc.)
- Generate ISO format timestamps

### 📅 Comprehensive Time Information
- Get detailed information about current time
- Multiple formatting options
- Day of week, week of year, and other metadata

## Available Methods

### `calculate_time_from_query(query: str)`
**Smart query parser that handles conversational time requests**

Examples:
- `"calculate the time 2 hours from now. the current time is 12:55 PM"`
- `"Add 3 hours. The current time is 11:30 PM"`
- `"What time will it be in 6 hours? It is 10:45 AM"`

### `calculate_time_addition(duration_str: str, base_time: str = None)`
**Add a duration to a base time**

Examples:
- `duration_str="2 hours 30 minutes", base_time="3:00 PM"`
- `duration_str="3 days", base_time="tomorrow"`
- `duration_str="1 week"` (uses current time as base)

### `calculate_time_subtraction(duration_str: str, base_time: str = None)`
**Subtract a duration from a base time**

Examples:
- `duration_str="2 hours", base_time="5:00 PM"`
- `duration_str="3 days", base_time="next Friday"`
- `duration_str="45 minutes"` (subtracts from current time)

### `calculate_time_difference(start_time: str, end_time: str)`
**Calculate the difference between two times**

Examples:
- `start_time="2024-01-01", end_time="2024-01-05"`
- `start_time="yesterday", end_time="tomorrow"`
- `start_time="9:00 AM", end_time="5:00 PM"`

### `convert_duration(duration_str: str, target_unit: str = "minutes")`
**Convert durations between different units**

Examples:
- `duration_str="2 hours 30 minutes", target_unit="minutes"`
- `duration_str="90 minutes", target_unit="hours"`
- `duration_str="1 week", target_unit="days"`

### `parse_to_timestamp(datetime_str: str)`
**Convert natural language to Unix timestamp**

Examples:
- `datetime_str="tomorrow at 3pm"`
- `datetime_str="next Friday"`
- `datetime_str="in 2 hours"`

### `format_current_time(format_string: str = "%H:%M:%S")`
**Format current time with custom format strings**

Examples:
- `format_string="%Y-%m-%d %I:%M %p"`
- `format_string="%A, %B %d, %Y"`
- `format_string="%H:%M:%S"`

### `get_time_info(timezone: str = None)`
**Get comprehensive information about current time**

Returns detailed time information including day of week, week of year, day of year, and various formats.

## Supported Time Formats

### Input Formats
- **12-hour format:** `"3:30 PM"`, `"12:00 AM"`, `"9 PM"`
- **24-hour format:** `"15:30"`, `"09:00"`, `"23:45"`
- **Date formats:** `"2024-01-15"`, `"01/15/2024"`, `"15/01/2024"`
- **Natural language:** `"tomorrow"`, `"yesterday"`, `"in 2 hours"`, `"next Friday"`

### Duration Formats
- **Years:** `"1 year"`, `"2 years"`, `"3 yr"`, `"4 yrs"`
- **Months:** `"1 month"`, `"6 months"`, `"2 mo"`
- **Weeks:** `"1 week"`, `"2 weeks"`, `"3 wk"`
- **Days:** `"1 day"`, `"5 days"`, `"7 d"`
- **Hours:** `"2 hours"`, `"1 hour"`, `"3 hr"`, `"4 hrs"`
- **Minutes:** `"30 minutes"`, `"45 mins"`, `"15 m"`
- **Seconds:** `"30 seconds"`, `"45 secs"`, `"10 s"`

### Complex Durations
- `"2 hours 30 minutes"`
- `"1 day 4 hours 15 minutes"`
- `"3 weeks 2 days"`
- `"1 year 6 months 2 weeks"`

## Usage Examples

### Basic Time Addition
```python
tools.calculate_time_addition("2 hours", "12:30 PM")
# Result: 2:30 PM
```

### Smart Query Processing
```python
tools.calculate_time_from_query("What time will it be 3 hours from now? The current time is 9:15 AM")
# Result: 12:15 PM
```

### Time Difference
```python
tools.calculate_time_difference("9:00 AM", "5:00 PM")
# Result: 8 hours difference
```

### Duration Conversion
```python
tools.convert_duration("150 minutes", "hours")
# Result: 2.5 hours
```

### Timestamp Generation
```python
tools.parse_to_timestamp("tomorrow at 3pm")
# Result: Unix timestamp and formatted datetime
```

## Error Handling

The tool includes comprehensive error handling for:
- Invalid time formats
- Unparseable duration strings
- Edge cases (month overflow, leap years)
- Malformed queries

## Installation

1. Copy `time_calculator.py` to your Open WebUI tools directory
2. Restart Open WebUI to load the tool
3. The tool will be available for use in conversations

## Dependencies

- Python 3.6+
- Built-in modules only: `datetime`, `re`, `calendar`
- No external dependencies required

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the Time Calculator tool.

## License

This project is licensed under the same terms as the parent repository.
