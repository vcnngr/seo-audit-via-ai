def generate_report_html(site_url, raw_data, report_data, competitors=[]):
    html = f"""<!DOCTYPE html>
<html lang="it">
<head><meta charset="UTF-8"><title>Report SEO</title></head>
<body>
<h1>Report SEO per {site_url}</h1>
<h2>Meta Tag</h2><p>{report_data.get("meta", "")}</p>
<h2>Headings</h2><p>{report_data.get("headings", "")}</p>
<h2>Contenuti</h2><p>{report_data.get("content", "")}</p>
<h2>Link Interni</h2><p>{"<br>".join(raw_data.get("links", []))}</p>
<h2>Competitor trovati su SERP</h2>
<ul>
""" + "".join([f"<li>{c['title']}<br>{c['link']}</li>" for c in competitors]) + f"""</ul>
<h2>Analisi Comparativa</h2><p>{report_data.get("competitor_comparison", "")}</p>
<h2>Raccomandazioni</h2><p>{report_data.get("recommendations", "")}</p>
</body></html>
"""
    return html
