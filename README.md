# url-xtractor
Lightweight Python app for user-friendly, customizable web data extraction. Chooses URLs from Excel file, fetches HTML content, and extracts data with BeautifulSoup. Outputs in txt, pdf, or doc formats.

<img src="interface.png" width="500">

## Project philosophy

- Simplifies large-scale URL Extraction
- Customizable Application Functionality
- Robust and User-Friendly Experience

## Setup

Follow these steps to get this project up and running:

Step 1: Clone repository

Step 2: Install dependencies 

Step 3: Specify target HTML element using `extract_content` function (optional)

Step 4: Run `gui.py`

## Features

Use the `extract_content` function in `model.py` to pull content from designated `<div>` containers in HTML by specifying their CSS class. Default target: `<body>` container.

## Vision

URL_xTractor is a robust tool for extracting large amounts of URL data from Excel files, simplifying data preprocessing for machine learning applications. Optimal for efficient and large-scale data extraction tasks.
