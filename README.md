## Time Machine ⌚ 

### Index

1. [Introduction](#introduction)
2. [Project Description](#project-description)
3. [File Structure](#file-structure)
4. [Dependencies](#dependencies)
5. [Endpoints](#endpoints)
6. [How to Run](#how-to-run)

---

### Introduction

This document provides comprehensive documentation for the "Time Machine" project, a Flask web application that allows users to access archived web pages from the Wayback Machine. The application provides an interface for entering URLs and selecting a specific year to view archived versions of web pages.

### Project Description

The project consists of a Flask web application that uses the Wayback Machine's CDX API to retrieve archived versions of web pages based on user input. The application allows users to input a URL and select a specific year, then displays the archived version of the web page from that year.

### File Structure

- **main.py**: Flask application containing the server-side logic and endpoint definitions.
- **template/whitespace.html**: HTML template file for the web interface.
- **static/ProductSans-Black.ttf**: Font file for the web interface.
- **static/ProductSans-Light.ttf**: Font file for the web interface.

### Dependencies

The project relies on the following Python libraries:

- **Flask**: Web framework for building the application.
- **waybackpy**: Python wrapper for the Wayback Machine's CDX API.

### Endpoints

- **/**: Home page, displays the main application interface.
- **/web**: Endpoint for retrieving archived web pages based on user input (URL).
- **/set**: Endpoint for setting the year to retrieve archived web pages.

### How to Run

To run the application:

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the Flask application using `python3 main.py`.
3. Access the application in a web browser at `http://localhost:5000`.

---
Made in 2024 by Francesco Colurcio
