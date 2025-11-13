import sqlite3
import json
from flask import Flask, request, render_template_string

app = Flask(__name__)


db = sqlite3.connect("packages.db", check_same_thread=False)
db.enable_load_extension(True)
db.row_factory = sqlite3.Row

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Package Search</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 2rem auto; }
        form { margin-bottom: 1rem; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 0.5rem; text-align: left; }
        th { background: #f4f4f4; }
    </style>
</head>
<body>
    <h1>Package Search</h1>
    <form method="get">
        <label>Distro:
            <input name="distro" value="{{ request.args.get('distro', '') }}">
        </label>
        <label>Package:
            <input name="package" value="{{ request.args.get('package', '') }}">
        </label>
        <button type="submit">Search</button>
    </form>

    {% if results %}
        <h2>Showing {{ results|length }} result{{ 's' if results|length != 1 else '' }}</h2>
        <table>
            <tr>
                <th>Distro</th>
                <th>Distro Version</th>
                <th>Package</th>
                <th>Package Version</th>
            </tr>
            {% for row in results %}
                <tr>
                    <td>{{ row['distro'] }}</td>
                    <td>{{ row['distro_version'] }}</td>
                    <td>{{ row['package'] }}</td>
                    <td>{{ row['package_version'] }}</td>
                </tr>
            {% endfor %}
        </table>
    {% else %}
        <p>No results found.</p>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET"])
def index():
    distro = request.args.get("distro", "").strip().lower()
    package = request.args.get("package", "").strip().lower()

    sql = "SELECT distro, distro_version, package, package_version FROM packages"
    if distro or package:
        sql += " WHERE "
    if distro:
        sql += f"LOWER(distro) = {json.dumps(distro)}"
    if distro and package:
        sql += " AND "
    if package:
        sql += f"LOWER(package) = {json.dumps(package)}"
    sql += " ORDER BY distro, distro_version, package"

    print(sql)
    results = db.execute(sql).fetchall()

    return render_template_string(TEMPLATE, request=request, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
