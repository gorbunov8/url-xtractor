import urllib.parse
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import json

def read_excel(file_path):
    df = pd.read_excel(file_path)
    urls = df['URL'].tolist()
    # Exclude empty URLs from the list
    urls = [url for url in urls if url and not pd.isna(url)]
    return urls

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises stored HTTPError, if one occurred
    return response.text

def extract_content(html, container_class='kbArticlesBody'):
    soup = BeautifulSoup(html, 'html.parser')
    # Handle <pre> tags
    for tag in soup.find_all('pre'):
        # Add markers and extra whitespace around the tag's contents
        tag.string = '\n=== START OF CODE ===\n' + tag.get_text() + '\n=== END OF CODE ===\n'
    # Check if a specific container class is specified
    if container_class:
        # Find the desired container using the specified class
        target = soup.find('div', class_=container_class)
    else:
        # Extract the body container by default
        target = soup.find('body')
    if target:
        return target.get_text(strip=True, separator=' ')
    else:
        return ""

def save_to_txt(data, filename, url):
    workspace_folder = "workspace"
    
    # Create the workspace folder if it doesn't exist
    if not os.path.exists(workspace_folder):
        os.makedirs(workspace_folder)
        print("✅ Folder 'workspace' created successfully")
    
    # Create the full file path including the workspace folder
    file_path = os.path.join(workspace_folder, filename)
    
    # Save the data to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)
        f.write('\n\n')
        f.write(f'Source: {url}')
    
    # Print the file path to the console log window
    # print(f"File saved: {file_path}")
        
def get_filename_from_url(url):
    # Parse the URL into components
    parsed_url = urllib.parse.urlparse(url)
    # Split the path into parts and get the last part
    filename = parsed_url.path.rstrip('/').split('/')[-1]
    return filename



