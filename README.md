# Shadowfox Python Internship

This repository contains my code submissions for the Shadowfox Python Development Internship tasks.

## Overview

# Beginner Level tasks:

Each task is organized into its own folder. Below is a list of tasks completed so far:

- **task-1**: Variables  
  - Create and check variable types  
  - Demonstrate reserved keywords  
  - Calculate Simple Interest  

- **task-2**: Numbers  
  - Formatted output using `format()` function  
  - Calculate area of a pond and total water content  
  - Calculate speed in meters per second (no decimals)

- **task-3**: List
  - Calculated the number of members in the Justice League.
  - Added new members Batgirl and Nightwing.
  - Moved Wonder Woman to the beginning as the leader.
  - Separated Aquaman and Flash by placing Green Lantern between them.
  - Replaced the existing team with a new Justice League roster.
  - Sorted the list alphabetically and identified the new leader.

- **task-4**: If Condition
  - BMI Calculator using user input  
  - City to Country mapping using conditional statements  
  - Check if two cities belong to the same country

- **task-5**
  This task demonstrates working with:

  - Lists and Tuples: Creating a list of friends' names and converting them into a list of tuples with name lengths.
  - Dictionaries: Comparing expenses between you and your partner.
  - Calculated total expenses for each.
  - Identified who spent more.
  - Found the category with the largest difference in spending.



# Intermediate Level Tasks:

## Task 1: Web Scrapper

This project involves scraping book information from the website [Books to Scrape](http://books.toscrape.com).

### Objective
- Extract book details including:
  - Title
  - Price 
  - Rating 
- Save the extracted data into a CSV file named `books_data.csv`.

### Technologies Used
- Python 3
- Requests library (to send HTTP requests)
- BeautifulSoup4 (to parse HTML content)
- CSV module (to save data)

### How It Works
1. The script loops through 50 pages of the website.
2. For each book on a page, it extracts the title, price, and rating.
3. Converts the price from GBP (£) to INR (₹) using a fixed exchange rate.
4. Stores all collected data in a CSV file for easy access and analysis.

### Usage
- Run the Python script.
- The script scrapes book data from all 50 pages.
- The data is saved automatically in `books_data.csv` in the project directory.

## Task 2: Hangman Game

### Objective
To build an interactive word-guessing game using Python that:
- Provides a fun and challenging experience
- Demonstrates the use of loops, conditionals, data structures, and functions
- Tracks scores and game progress across multiple rounds
- Reinforces concepts such as user input handling, game state management, and error handling

### Key Features
- Visual hangman stages that update with each incorrect guess  
- Word hints to assist the player in guessing  
- Input validation to ensure only valid, new guesses are accepted  
- Scoring system:
  - +10 points per correct guess  
  - -5 points per wrong guess  
- Game automatically progresses to the next round without asking  
- Tracks total score through all rounds  
- Graceful exit (using `Ctrl+C`) that displays the final score  

### Technologies Used
- Python 3.x  
- Standard libraries: `random`

# Advanced Level Task:

## Netflix Data Analysis Project

This project analyzes Netflix’s content library using Python. It includes data cleaning, exploratory data analysis (EDA), and visualization to uncover trends in genres, countries, and ratings.

## Dataset
The dataset contains information about Netflix titles, including type, genre, release year, and more.

## Key Insights
- Drama and documentaries are the most popular genres.
- Certain countries have more diverse content.
- Movies tend to be shorter in duration compared to TV shows.

## Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## How to Run
Open the notebook `Netflix_Data_Analysis.ipynb` in JupyterLab or Jupyter Notebook.









