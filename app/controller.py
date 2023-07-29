from model import read_excel, fetch_html, extract_content, save_to_txt, get_filename_from_url
from view import update_progress


def start_extraction(file_path):
    urls = read_excel(file_path)
    total_files = len(urls)  # Get the total number of files
    file_counter = 0  # Initialize the file counter
    
    for i, url in enumerate(urls):
        try:
            html = fetch_html(url)
            content = extract_content(html)
            filename = f'{get_filename_from_url(url)}.txt'
            save_to_txt(content, filename, url)
            
            file_counter += 1  # Increment the file counter
            
            update_progress(f"🟩 Successfully saved {filename}")
        except Exception as e:
            update_progress(f"🟥  Failed to process URL {url}: {str(e)}")
    
    
    # Check if all jobs are done
    if file_counter == total_files:
        print("")
        print(f"✅ All jobs are done. Total: {file_counter}")
        print("")
        print("👾 Thanks for choosing URL_xTRAKTOR 👾")
        print("")
        print("Check repository for updates: ")
        print("https://github.com/gorbunov8/url-xtractor")




