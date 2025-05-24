def build_comparison_prompt(site_data, competitors_data):
    return f"""Agisci come un esperto SEO con esperienza in benchmarking competitivo.
Analizza e confronta il sito principale con i suoi competitor su Google.

Sito principale:
- Title: {site_data.get('title')}
- Meta: {site_data.get('meta')}
- H1: {site_data.get('h1')}

Competitor (primi risultati SERP):
{competitors_data}

Confronta chiarezza comunicativa, struttura SEO, uso keyword, efficacia.
Fornisci suggerimenti chiari per superare i competitor.
Rispondi in italiano.
"""
