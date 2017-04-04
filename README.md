# Homework-Notifier

Checks and notifies users of homework for classes.

## Functions

Currently only works for RPI students.
Last updated for Spring 2017 semester.
Checks and updates for all assignments in:
  * CSCI 2300: Introduction to Algorithms
  * CSCI 2600: Principles of Software

The program works by scraping the assignment information off the class websites.
Each class web scraper is created tailored to the class website for that semester.

## Use

In order to run the program, clone the repository and fill in holder.py with the details of the gmail account intended to send updates from - MUST ALLOW FOR OTHER PROGRAMS TO ACCESS ACCOUNT.

 * Run ```python main.py``` to send out updates to all users.
 * Run ```python main.py -help``` in order to read about all flags.
