from bs4 import BeautifulSoup
import logging

def clean_html(content):
    """Removes HTML tags and extracts plain text."""
    try:
        soup = BeautifulSoup(content, "html.parser")
        return soup.get_text(separator=" ").strip()
    except Exception as e:
        logging.error(f"Error cleaning HTML content: {e}")
        return content  # Return raw content if cleaning fails
