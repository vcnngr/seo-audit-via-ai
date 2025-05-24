from openai import OpenAI
import pdfkit
import time
from core.scraper import scrape_site
from core.prompts import build_prompts
from core.report_builder import generate_report_html
from core.serp_scraper import get_serp_results
from core.comparator import build_comparison_prompt

def safe_chat_completion(client, model, messages, retries=3):
    for attempt in range(retries):
        try:
            return client.chat.completions.create(model=model, messages=messages)
        except Exception as e:
            if 'rate_limit_exceeded' in str(e).lower():
                time.sleep(65)
            else:
                raise e
    raise RuntimeError("Limite di tentativi superato.")

def process_site(site_url, api_key, keyword="hotel roma", serpapi_key=None):
    client = OpenAI(api_key=api_key)

    raw_data = scrape_site(site_url)
    prompts = build_prompts(raw_data)

    report = {}
    for key, prompt in prompts.items():
        response = safe_chat_completion(
            client,
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Agisci come un consulente SEO senior. Fornisci analisi tecniche e consigli ottimizzati."},
                {"role": "user", "content": prompt}
            ]
        )
        report[key] = response.choices[0].message.content

    # SERP + confronto competitivo
    competitors_data = []
    if serpapi_key:
        results = get_serp_results(keyword, serpapi_key)
        competitors_data = results
        site_data = {
            "title": raw_data.get("headings")[0] if raw_data.get("headings") else "",
            "meta": raw_data.get("meta_tags"),
            "h1": raw_data.get("headings")
        }

        comparison_prompt = build_comparison_prompt(site_data, results)
        response = safe_chat_completion(
            client,
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Agisci come un consulente SEO esperto in benchmarking competitivo."},
                {"role": "user", "content": comparison_prompt}
            ]
        )
        report["competitor_comparison"] = response.choices[0].message.content

    # HTML rendering
    html_output = generate_report_html(site_url, raw_data, report, competitors_data)

    # PDF export
    pdf_path = "/mnt/data/report_seo.pdf"
    pdfkit.from_string(html_output, pdf_path)

    return {
        "site": site_url,
        "summary": {"homepage": f"Analisi della homepage del sito {site_url}"},
        "meta": report.get("meta", ""),
        "headings": report.get("headings", ""),
        "content": report.get("content", ""),
        "links": report.get("links", ""),
        "competitor_comparison": report.get("competitor_comparison", ""),
        "recommendations": report.get("recommendations", ""),
        "pdf_path": pdf_path
    }
