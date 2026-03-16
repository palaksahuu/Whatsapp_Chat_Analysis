# WhatsApp Chat Data Preprocessing

This project contains a Python function that preprocesses exported WhatsApp chat data and converts it into a structured pandas DataFrame for further analysis.

The script extracts message timestamps, users, and messages from raw WhatsApp chat text and organizes them into a tabular format. It also generates additional time-based features that can be used for chat analysis, visualization, or natural language processing.

---

## Project Overview

WhatsApp chat exports usually come as raw text files where each message contains a timestamp, username, and message content.

This preprocessing script performs the following tasks:

- Extracts messages and timestamps using regular expressions
- Converts timestamps into datetime format
- Separates usernames and message content
- Identifies group notifications
- Creates additional time-based features such as year, month, day, hour, and minute

The final output is a clean pandas DataFrame that can be used for further data analysis.

---

## Technologies Used

- Python
- Pandas
- Regular Expressions (re module)
