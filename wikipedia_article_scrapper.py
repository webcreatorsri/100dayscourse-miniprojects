import requests
from bs4 import BeautifulSoup
import streamlit as st
import pdfkit

# Wikipedia API Base URL
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

# Function to fetch Wikipedia article
def get_wikipedia_page(topic):
    search_url = f"{WIKI_API_URL}?action=query&list=search&srsearch={topic}&format=json"
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        if data["query"]["search"]:
            best_match = data["query"]["search"][0]["title"]
            page_url = f"https://en.wikipedia.org/wiki/{best_match.replace(' ', '_')}"
            return requests.get(page_url).text, page_url, best_match
        else:
            return None, None, None
    else:
        return None, None, None

# Extract article details
def extract_article_details(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    
    title = soup.find('h1').text if soup.find('h1') else "No Title Found"
    paragraphs = soup.find_all('p')
    summary = next((p.text.strip() for p in paragraphs if p.text.strip()), "No Summary Found")
    headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3'])][:5]
    
    return title, summary, headings

# Extract related links
def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(set(links))[:5]

# Convert to PDF
def convert_to_pdf(title, summary, headings, related_links):
    html_content = f"""
    <h1>{title}</h1>
    <p><strong>Summary:</strong> {summary}</p>
    <h2>Headings:</h2>
    <ul>
    {''.join(f'<li>{heading}</li>' for heading in headings)}
    </ul>
    <h2>Related Links:</h2>
    <ul>
    {''.join(f'<li><a href="{link}">{link}</a></li>' for link in related_links)}
    </ul>
    """
    pdfkit.from_string(html_content, "article.pdf")
    return "article.pdf"

# Streamlit UI
st.title("📚 Wikipedia Article Scraper")

# User selects a topic
topic = st.text_input("Enter a topic (e.g., Python, AI, Science, Space, History):").strip()

if st.button("Search Wikipedia"):
    if topic:
        st.info(f"Searching for '{topic}'...")
        page_content, page_url, best_match = get_wikipedia_page(topic)

        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            title, summary, headings = extract_article_details(page_content)
            related_links = get_related_links(soup)

            st.subheader(f"📖 {title}")
            st.write(f"🔗 **Wikipedia URL:** [Read Full Article]({page_url})")
            st.write(f"📝 **Summary:** {summary}")
            
            st.subheader("📌 Key Headings:")
            for heading in headings:
                st.write(f"- {heading}")

            st.subheader("🔗 Related Links:")
            for link in related_links:
                st.write(f"- [{link}]({link})")

            # Convert to PDF and Provide Download Option
            if st.button("Download as PDF"):
                pdf_path = convert_to_pdf(title, summary, headings, related_links)
                with open(pdf_path, "rb") as file:
                    st.download_button(label="📥 Download Article PDF", data=file, file_name="Wikipedia_Article.pdf", mime="application/pdf")

        else:
            st.error("❌ No Wikipedia article found! Try a different topic.")
    else:
        st.warning("⚠️ Please enter a topic.")

