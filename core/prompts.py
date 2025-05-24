def build_prompts(data):
    prompts = {}

    prompts["meta"] = f"""Sei un esperto SEO. Analizza i seguenti meta tag della homepage:
{data['meta_tags']}

Verifica se rispettano le best practice in termini di:
- lunghezza ottimale
- presenza di keyword pertinenti
- efficacia comunicativa

Se assenti o subottimali, proponi un esempio concreto di title e meta description ottimizzati.
"""

    prompts["headings"] = f"""Valuta questi heading HTML (H1-H2-H3):
{data['headings']}
Verifica struttura gerarchica, keyword, coerenza.
"""

    prompts["content"] = f"""Analizza il seguente testo della homepage:

"{data['text']}"

Valuta se è efficace dal punto di vista SEO:
- chiarezza e leggibilità
- keyword ben distribuite
- appeal per il lettore

Se mancano questi aspetti, suggerisci **modifiche concrete** o **frasi alternative**.
"""

    prompts["links"] = f"""Analizza i seguenti link presenti nella homepage:
{data['links']}

Valuta:
- correttezza e leggibilità degli URL
- presenza di anchor text descrittivi
- strategia interna SEO

Se trovi link mal strutturati o assenti, suggerisci best practice.
"""

    prompts["recommendations"] = f"""Sulla base di questi elementi:
- meta tag
- heading
- testo principale
- link presenti

Fornisci **5 suggerimenti SEO personalizzati** per migliorare questo sito.
Non usare raccomandazioni generiche. Focalizzati sul sito in esame.
"""

    return prompts
