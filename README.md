# Nic's Open WebUI Tools Collection

[![Open WebUI](https://img.shields.io/badge/Open%20WebUI-Compatible-blue?style=flat-square&logo=github)](https://github.com/open-webui/open-webui)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python)](https://www.python.org/)

> **🛠️ My personal collection of custom tools for Open WebUI.**

This is my growing collection of Open WebUI tools that I've created to enhance my AI workflow. Each tool is designed to solve specific problems and add functionality to my Open WebUI setup.

## ✨ My Tools

### 🛠️ **Tools**
- **Time Calculator** - Comprehensive time calculations, additions, subtractions, and conversions

*More tools coming soon as I develop them...*

## 🚀 Quick Start

### Installation
1. Clone or download this repository
2. Navigate to the `tools/` directory
3. Copy the `.py` file for the tool you want to use
4. In Open WebUI, go to Workspace > Tools
5. Click "Create New Tool"
6. Paste the code, provide a name and description, then save

## 🎯 Features

- **🔌 Simple Setup**: Tools work out of the box with minimal configuration
- **⏰ Time Management**: Advanced time calculations and conversions
- **🔧 Custom Built**: Each tool is tailored to my specific needs

## 📋 Prerequisites

- **Open WebUI**: Version 0.3.0+ recommended
- **Python**: 3.8 or higher

---

## 📖 Tool Documentation

### Time Calculator Tool

**Location**: `tools/time_calculator.py`

**Description**: A comprehensive time calculation tool that handles additions, subtractions, differences, conversions, and formatting for dates and times.

**Features**:
- Add or subtract durations from any date/time
- Calculate differences between two dates/times
- Convert durations between different units
- Parse natural language time expressions
- Format timestamps and dates
- Support for various time formats

**Usage Examples**:
- **NEW!** "Calculate the time 2 hours from now. The current time is 12:55 PM"
- **NEW!** "What time will it be in 6 hours? It is 10:45 AM"
- "Add 2 hours 30 minutes to now"
- "Subtract 3 days from tomorrow"
- "What's the difference between now and tomorrow?"
- "Convert 90 minutes to hours"
- "Parse tomorrow at 3pm to timestamp"

**Available Functions**:
- `calculate_time_from_query()` - **NEW!** Smart query parser for conversational time requests
- `calculate_time_addition()` - Add duration to a base time
- `calculate_time_subtraction()` - Subtract duration from a base time  
- `calculate_time_difference()` - Find difference between two times
- `convert_duration()` - Convert between time units
- `format_current_time()` - Format current time with custom patterns
- `parse_to_timestamp()` - Convert natural language to Unix timestamp
- `get_time_info()` - Get comprehensive time information

**Configuration**: No configuration required - works out of the box!

**Recent Updates (v1.0.0)**:
- **🆕 NEW**: Smart conversational query parsing with `calculate_time_from_query()`
- **🔧 Enhanced**: Better handling of "in X duration" patterns (e.g., "in 2 hours", "in 30 minutes")
- **🎯 Improved**: Automatic base time extraction from queries like "current time is 12:55 PM"
- **💬 Better UX**: More natural language understanding for time calculations
- **🛠️ Technical**: Enhanced `parse_natural_datetime()` and new `extract_base_time_from_query()` function

---

## 📁 Project Structure

```
/
├── .gitignore
├── LICENSE (MIT)
├── README.md
└── tools/
    └── time_calculator.py
```

## 📝 Adding New Tools

As I create new tools, I'll add them to the `tools/` directory and document them here. Each tool follows this structure:

1. **Header metadata** with title, author, version info
2. **Tools class** with initialization and tool methods
3. **Clear documentation** of parameters and usage

Feel free to fork this repository if you want to use it as a template for your own Open WebUI tools collection!

## 🔧 Development

To contribute or modify tools:

1. Fork the repository
2. Create a new tool file in `tools/`
3. Follow the existing code structure
4. Test thoroughly
5. Update this README
6. Submit a pull request

## 📄 License

MIT License

## 🎯 Support

This is my personal collection of tools. If you find them useful, feel free to adapt them for your own use!
