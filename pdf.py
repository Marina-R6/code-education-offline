from weasyprint import HTML

def generate_pdf(articles):
    html = "<h1>Code de l'éducation</h1>"

    for a in articles:
        html += f"<p>{a}</p><hr>"

    HTML(string=html).write_pdf("Code_Education.pdf")
