import requests

def get_serp_results(keyword, serpapi_key, num_results=5):
    url = "https://serpapi.com/search"
    params = {
        "q": keyword,
        "hl": "it",
        "gl": "it",
        "api_key": serpapi_key
    }

    response = requests.get(url, params=params).json()
    results = []
    for result in response.get("organic_results", [])[:num_results]:
        results.append({
            "title": result.get("title"),
            "link": result.get("link"),
            "snippet": result.get("snippet")
        })
    return results
