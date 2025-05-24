from flask import Blueprint, request, render_template
from app.analyzer import process_site

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        site_url = request.form.get("site_url")
        api_key = request.form.get("api_key")
        serpapi_key = request.form.get("serpapi_key")

        if not site_url or not api_key:
            return render_template("report.html", error="Compila tutti i campi obbligatori")

        report_data = process_site(site_url, api_key, serpapi_key=serpapi_key)
        return render_template("report.html", report=report_data)

    return render_template("form.html")
