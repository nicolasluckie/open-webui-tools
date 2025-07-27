"""
title: Time Calculator
author: Nicolas Luckie
author_url: https://github.com/nicolasluckie/open-webui-tools
version: 1.0.0
"""

import datetime
import re
import calendar


def get_current_time() -> datetime.datetime:
    """
    Get the current time - centralized function for consistency across all time operations.
    """
    return datetime.datetime.now()


def parse_duration(duration_str: str) -> dict:
    """
    Parse a natural language duration string into components.
    Examples: "2 hours 30 minutes", "3 days", "1 year 2 months"
    """
    duration_str = duration_str.lower().strip()
    
    # Define patterns for different time units
    patterns = {
        'years': r'(\d+)\s*(?:year|years|yr|yrs|y)',
        'months': r'(\d+)\s*(?:month|months|mon|mons|mo)',
        'weeks': r'(\d+)\s*(?:week|weeks|wk|wks|w)',
        'days': r'(\d+)\s*(?:day|days|d)',
        'hours': r'(\d+)\s*(?:hour|hours|hr|hrs|h)',
        'minutes': r'(\d+)\s*(?:minute|minutes|min|mins|m)',
        'seconds': r'(\d+)\s*(?:second|seconds|sec|secs|s)'
    }
    
    result = {}
    for unit, pattern in patterns.items():
        match = re.search(pattern, duration_str)
        if match:
            result[unit] = int(match.group(1))
    
    return result


def parse_time_string(time_str: str) -> datetime.time:
    """
    Parse a simple time string like "3pm", "15:30", "9:45 AM"
    """
    time_str = time_str.strip().lower()
    
    # Handle AM/PM format
    if 'pm' in time_str or 'am' in time_str:
        is_pm = 'pm' in time_str
        time_str = time_str.replace('pm', '').replace('am', '').strip()
        
        if ':' in time_str:
            parts = time_str.split(':')
            hour = int(parts[0])
            minute = int(parts[1]) if len(parts) > 1 else 0
        else:
            hour = int(time_str)
            minute = 0
        
        if is_pm and hour != 12:
            hour += 12
        elif not is_pm and hour == 12:
            hour = 0
            
        return datetime.time(hour, minute)
    
    # Handle 24-hour format
    if ':' in time_str:
        parts = time_str.split(':')
        hour = int(parts[0])
        minute = int(parts[1]) if len(parts) > 1 else 0
        return datetime.time(hour, minute)
    
    # Simple hour
    hour = int(time_str)
    return datetime.time(hour, 0)


def add_months(dt: datetime.datetime, months: int) -> datetime.datetime:
    """
    Add months to a datetime, handling month overflow correctly
    """
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def parse_natural_datetime(date_str: str) -> datetime.datetime:
    """
    Parse a natural language date/time string into a datetime object.
    Handles various formats like "next Friday", "in 2 hours", "tomorrow at 3pm", etc.
    """
    date_str = date_str.lower().strip()
    now = get_current_time()
    
    # Handle relative terms
    if 'now' in date_str:
        return now
    elif 'today' in date_str:
        if 'at' in date_str:
            time_part = date_str.split('at')[1].strip()
            try:
                parsed_time = parse_time_string(time_part)
                return datetime.datetime.combine(now.date(), parsed_time)
            except:
                return now.replace(hour=0, minute=0, second=0, microsecond=0)
        # If no specific time is mentioned, use the current time
        return now
    elif 'tomorrow' in date_str:
        tomorrow = now + datetime.timedelta(days=1)
        if 'at' in date_str:
            time_part = date_str.split('at')[1].strip()
            try:
                parsed_time = parse_time_string(time_part)
                return datetime.datetime.combine(tomorrow.date(), parsed_time)
            except:
                return tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
        # If no specific time is mentioned, use the same time as now but tomorrow
        return tomorrow
    elif 'yesterday' in date_str:
        yesterday = now - datetime.timedelta(days=1)
        # If no specific time is mentioned, use the same time as now but yesterday
        return yesterday
    
    # Try to parse simple date formats
    try:
        # Handle YYYY-MM-DD format
        if re.match(r'\d{4}-\d{2}-\d{2}', date_str):
            return datetime.datetime.strptime(date_str, '%Y-%m-%d')
        # Handle MM/DD/YYYY format
        elif re.match(r'\d{1,2}/\d{1,2}/\d{4}', date_str):
            return datetime.datetime.strptime(date_str, '%m/%d/%Y')
        # Handle DD/MM/YYYY format
        elif re.match(r'\d{1,2}/\d{1,2}/\d{4}', date_str):
            return datetime.datetime.strptime(date_str, '%d/%m/%Y')
    except:
        pass
    
    # If all else fails, return current time
    return now


def format_duration(total_seconds: int) -> str:
    """
    Format a duration in seconds into a human-readable string.
    """
    if total_seconds < 0:
        sign = "-"
        total_seconds = abs(total_seconds)
    else:
        sign = ""
    
    years = total_seconds // (365 * 24 * 3600)
    total_seconds %= (365 * 24 * 3600)
    
    months = total_seconds // (30 * 24 * 3600)  # Approximate
    total_seconds %= (30 * 24 * 3600)
    
    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)
    
    hours = total_seconds // 3600
    total_seconds %= 3600
    
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    if months > 0:
        parts.append(f"{months} month{'s' if months != 1 else ''}")
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    return sign + ", ".join(parts)


class Tools:
    def __init__(self):
        self.citation = True

    def calculate_time_addition(self, duration_str: str, base_time: str = None) -> str:
        """
        Add a duration to a base time (current time if not specified).
        Examples: "Add 2 hours to now", "Add 3 days to tomorrow"
        :param duration_str: Duration to add (e.g., "2 hours", "3 days 2 hours")
        :param base_time: Base time to add to (defaults to current time)
        :return: The calculated time
        """
        try:
            # Parse the base time - use current time if not specified or implied
            if base_time is None or base_time.lower() in ['now', 'current time', '']:
                base_dt = get_current_time()
                base_description = "current time"
            else:
                base_dt = parse_natural_datetime(base_time)
                base_description = base_time
            
            # Parse the duration
            duration_components = parse_duration(duration_str)
            
            if not duration_components:
                return f"Could not parse duration: {duration_str}"
            
            # Apply the duration using standard library datetime operations
            result_dt = base_dt
            
            # Add years and months using helper function
            if 'years' in duration_components:
                result_dt = add_months(result_dt, duration_components['years'] * 12)
            if 'months' in duration_components:
                result_dt = add_months(result_dt, duration_components['months'])
            
            # Add other time units using timedelta
            delta = datetime.timedelta(
                weeks=duration_components.get('weeks', 0),
                days=duration_components.get('days', 0),
                hours=duration_components.get('hours', 0),
                minutes=duration_components.get('minutes', 0),
                seconds=duration_components.get('seconds', 0)
            )
            result_dt = result_dt + delta
            
            return f"**Time Addition Result:**\n\n" \
                   f"• **Base time:** {base_dt.strftime('%Y-%m-%d %H:%M:%S')} ({base_description})\n" \
                   f"• **Duration added:** {duration_str}\n" \
                   f"• **Result:** {result_dt.strftime('%Y-%m-%d %H:%M:%S')}\n" \
                   f"• **Day of week:** {result_dt.strftime('%A')}\n" \
                   f"• **Unix timestamp:** {int(result_dt.timestamp())}"
                   
        except Exception as e:
            return f"Error calculating time addition: {str(e)}"

    def calculate_time_subtraction(self, duration_str: str, base_time: str = None) -> str:
        """
        Subtract a duration from a base time (current time if not specified).
        Examples: "Subtract 3 days from today", "Subtract 2 hours from now"
        :param duration_str: Duration to subtract (e.g., "2 hours", "3 days 2 hours")
        :param base_time: Base time to subtract from (defaults to current time)
        :return: The calculated time
        """
        try:
            # Parse the base time - use current time if not specified or implied
            if base_time is None or base_time.lower() in ['now', 'current time', '']:
                base_dt = get_current_time()
                base_description = "current time"
            else:
                base_dt = parse_natural_datetime(base_time)
                base_description = base_time
            
            # Parse the duration
            duration_components = parse_duration(duration_str)
            
            if not duration_components:
                return f"Could not parse duration: {duration_str}"
            
            # Subtract the duration using standard library datetime operations
            result_dt = base_dt
            
            # Subtract years and months using helper function
            if 'years' in duration_components:
                result_dt = add_months(result_dt, -duration_components['years'] * 12)
            if 'months' in duration_components:
                result_dt = add_months(result_dt, -duration_components['months'])
            
            # Subtract other time units using timedelta
            delta = datetime.timedelta(
                weeks=duration_components.get('weeks', 0),
                days=duration_components.get('days', 0),
                hours=duration_components.get('hours', 0),
                minutes=duration_components.get('minutes', 0),
                seconds=duration_components.get('seconds', 0)
            )
            result_dt = result_dt - delta
            
            return f"**Time Subtraction Result:**\n\n" \
                   f"• **Base time:** {base_dt.strftime('%Y-%m-%d %H:%M:%S')} ({base_description})\n" \
                   f"• **Duration subtracted:** {duration_str}\n" \
                   f"• **Result:** {result_dt.strftime('%Y-%m-%d %H:%M:%S')}\n" \
                   f"• **Day of week:** {result_dt.strftime('%A')}\n" \
                   f"• **Unix timestamp:** {int(result_dt.timestamp())}"
                   
        except Exception as e:
            return f"Error calculating time subtraction: {str(e)}"

    def calculate_time_difference(self, start_time: str, end_time: str) -> str:
        """
        Calculate the difference between two dates/times.
        :param start_time: Start time (e.g., "2024-01-01", "yesterday", "now")
        :param end_time: End time (e.g., "2024-01-05", "tomorrow", "in 2 hours")
        :return: The time difference in various formats
        """
        try:
            # Parse both times - use current time if "now" is implied
            if start_time.lower() in ['now', 'current time', '']:
                start_dt = get_current_time()
                start_description = "current time"
            else:
                start_dt = parse_natural_datetime(start_time)
                start_description = start_time
                
            if end_time.lower() in ['now', 'current time', '']:
                end_dt = get_current_time()
                end_description = "current time"
            else:
                end_dt = parse_natural_datetime(end_time)
                end_description = end_time
            
            # Calculate the difference
            diff = end_dt - start_dt
            total_seconds = int(diff.total_seconds())
            
            # Format the difference
            formatted_diff = format_duration(abs(total_seconds))
            direction = "later" if total_seconds >= 0 else "earlier"
            
            return f"**Time Difference Calculation:**\n\n" \
                   f"• **Start time:** {start_dt.strftime('%Y-%m-%d %H:%M:%S')} ({start_description})\n" \
                   f"• **End time:** {end_dt.strftime('%Y-%m-%d %H:%M:%S')} ({end_description})\n" \
                   f"• **Difference:** {formatted_diff}\n" \
                   f"• **Direction:** End time is {formatted_diff} {direction} than start time\n" \
                   f"• **Total seconds:** {total_seconds:,}\n" \
                   f"• **Total minutes:** {total_seconds // 60:,}\n" \
                   f"• **Total hours:** {total_seconds // 3600:,}\n" \
                   f"• **Total days:** {total_seconds // 86400:,}"
                   
        except Exception as e:
            return f"Error calculating time difference: {str(e)}"

    def convert_duration(self, duration_str: str, target_unit: str = "minutes") -> str:
        """
        Convert a duration to a specific unit.
        Examples: "How many minutes in 2 hours 30 minutes?", "Convert 90 minutes to hours"
        :param duration_str: Duration to convert (e.g., "2 hours 30 minutes", "90 minutes")
        :param target_unit: Target unit (seconds, minutes, hours, days, weeks, months, years)
        :return: The converted duration
        """
        try:
            # Parse the duration
            duration_components = parse_duration(duration_str)
            
            if not duration_components:
                return f"Could not parse duration: {duration_str}"
            
            # Convert to total seconds first
            total_seconds = 0
            total_seconds += duration_components.get('years', 0) * 365 * 24 * 3600
            total_seconds += duration_components.get('months', 0) * 30 * 24 * 3600  # Approximate
            total_seconds += duration_components.get('weeks', 0) * 7 * 24 * 3600
            total_seconds += duration_components.get('days', 0) * 24 * 3600
            total_seconds += duration_components.get('hours', 0) * 3600
            total_seconds += duration_components.get('minutes', 0) * 60
            total_seconds += duration_components.get('seconds', 0)
            
            # Convert to target unit
            target_unit = target_unit.lower().rstrip('s')  # Remove plural 's'
            
            conversions = {
                'second': total_seconds,
                'minute': total_seconds / 60,
                'hour': total_seconds / 3600,
                'day': total_seconds / 86400,
                'week': total_seconds / (7 * 86400),
                'month': total_seconds / (30 * 86400),  # Approximate
                'year': total_seconds / (365 * 86400)
            }
            
            if target_unit not in conversions:
                return f"Unknown target unit: {target_unit}. Supported units: {', '.join(conversions.keys())}"
            
            result = conversions[target_unit]
            
            return f"**Duration Conversion:**\n\n" \
                   f"• **Original:** {duration_str}\n" \
                   f"• **Converted to {target_unit}s:** {result:,.2f}\n" \
                   f"• **Total seconds:** {total_seconds:,}\n" \
                   f"• **Breakdown:** {format_duration(total_seconds)}"
                   
        except Exception as e:
            return f"Error converting duration: {str(e)}"

    def format_current_time(self, format_string: str = "%H:%M:%S") -> str:
        """
        Format the current time using a specified format.
        :param format_string: Format string (e.g., "%H:%M:%S", "%Y-%m-%d %I:%M %p")
        :return: The formatted current time
        """
        try:
            now = get_current_time()
            formatted_time = now.strftime(format_string)
            
            return f"**Current Time Formatting:**\n\n" \
                   f"• **Current time:** {now.strftime('%Y-%m-%d %H:%M:%S')}\n" \
                   f"• **Formatted as \"{format_string}\":** {formatted_time}\n" \
                   f"• **Unix timestamp:** {int(now.timestamp())}\n" \
                   f"• **Day of week:** {now.strftime('%A')}"
                   
        except Exception as e:
            return f"Error formatting current time: {str(e)}"

    def parse_to_timestamp(self, datetime_str: str) -> str:
        """
        Parse a natural language date/time string into a Unix timestamp.
        Examples: "tomorrow at 3pm", "next Friday", "in 2 hours"
        :param datetime_str: Natural language date/time string
        :return: Unix timestamp and parsed datetime
        """
        try:
            # Handle implicit current time
            if datetime_str.lower() in ['now', 'current time', '']:
                parsed_dt = get_current_time()
                input_description = "current time"
            else:
                parsed_dt = parse_natural_datetime(datetime_str)
                input_description = datetime_str
            
            timestamp = int(parsed_dt.timestamp())
            
            return f"**Natural Language Date/Time Parsing:**\n\n" \
                   f"• **Input:** \"{input_description}\"\n" \
                   f"• **Parsed as:** {parsed_dt.strftime('%Y-%m-%d %H:%M:%S')}\n" \
                   f"• **Day of week:** {parsed_dt.strftime('%A')}\n" \
                   f"• **Unix timestamp:** {timestamp}\n" \
                   f"• **ISO format:** {parsed_dt.isoformat()}"
                   
        except Exception as e:
            return f"Error parsing datetime string: {str(e)}"

    def get_time_info(self, timezone: str = None) -> str:
        """
        Get comprehensive time information for current time.
        Note: Timezone support requires additional setup in Open WebUI environment.
        :param timezone: Timezone name (currently not supported without pytz)
        :return: Comprehensive time information
        """
        try:
            now = get_current_time()
            
            if timezone:
                return f"**Time Information:**\n\n" \
                       f"⚠️ **Note:** Timezone functionality requires additional Python packages (pytz) to be installed.\n\n" \
                       f"**Current local time information:**\n" \
                       f"• **Date/time:** {now.strftime('%Y-%m-%d %H:%M:%S')} (Local time)\n" \
                       f"• **12-hour format:** {now.strftime('%I:%M:%S %p')}\n" \
                       f"• **Day of week:** {now.strftime('%A')}\n" \
                       f"• **Month:** {now.strftime('%B')}\n" \
                       f"• **Week of year:** {now.strftime('%U')}\n" \
                       f"• **Day of year:** {now.strftime('%j')}\n" \
                       f"• **Unix timestamp:** {int(now.timestamp())}\n" \
                       f"• **ISO format:** {now.isoformat()}\n\n" \
                       f"💡 **Tip:** To use timezone features, install pytz: `pip install pytz`"
            
            return f"**Comprehensive Time Information (Local time):**\n\n" \
                   f"• **Date/time:** {now.strftime('%Y-%m-%d %H:%M:%S')}\n" \
                   f"• **12-hour format:** {now.strftime('%I:%M:%S %p')}\n" \
                   f"• **Day of week:** {now.strftime('%A')}\n" \
                   f"• **Month:** {now.strftime('%B')}\n" \
                   f"• **Week of year:** {now.strftime('%U')}\n" \
                   f"• **Day of year:** {now.strftime('%j')}\n" \
                   f"• **Unix timestamp:** {int(now.timestamp())}\n" \
                   f"• **ISO format:** {now.isoformat()}"
                   
        except Exception as e:
            return f"Error getting time info: {str(e)}"