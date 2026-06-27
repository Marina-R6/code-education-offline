from download import get_code_html
from extract import extract_articles
from pdf import generate_pdf

def main():
    print("Téléchargement...")
    html = get_code_html()

    print("Extraction...")
    articles = extract_articles(html)

    print("PDF...")
    generate_pdf(articles)

    print("Terminé -> Code_Education.pdf")

if __name__ == "__main__":
    main()
