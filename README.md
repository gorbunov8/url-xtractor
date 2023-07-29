# url-xtractor
Lightweight Python app for user-friendly, customizable web data extraction. Chooses URLs from Excel file, fetches HTML content, and extracts data with BeautifulSoup. Outputs in txt, pdf, or doc formats.

<img src="interface.png" width="500">

In `model.py`, there is a function named `extract_content`, which allows you to extract content from specific `<div>` containers within an HTML document. You can specify the target `<div>` containers by using their CSS class names. Default container: `<body>`. 
