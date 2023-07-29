# url-xtractor
Lightweight Python app for user-friendly, customizable web data extraction. Chooses URLs from Excel file, fetches HTML content, and extracts data with BeautifulSoup. Outputs in txt, pdf, or doc formats.

<img src="interface.png" width="500">

Use the `extract_content` function in `model.py` to pull content from designated `<div>` containers in HTML by specifying their CSS class. Default target is the `<body>` container.
