from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

# HTML template for rendering the Mermaid flowchart
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Mermaid Flowchart</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
</head>
<body>
    <h1>Mermaid Flowchart</h1>
    <div class="mermaid">
        {{ mermaid_chart }}
    </div>
    <script>
        mermaid.initialize({ startOnLoad: true });
    </script>
</body>
</html>
"""


def generate_mermaid(node, parent=None):
    """Recursive function to generate Mermaid flowchart syntax."""
    lines = []
    if parent:
        lines.append(f'{parent} --> {node["name"]}')
    for child in node.get("children", []):
        lines.extend(generate_mermaid(child, node["name"]))
    return lines


@app.route("/")
def index():
    # Ensure the data.json file exists
    if not os.path.exists("data.json"):
        return "Error: data.json file not found. Please ensure it exists in the same directory as this script.", 400

    try:
        # Load the hierarchy from data.json
        with open("data.json", "r", encoding='utf-8') as file:
            hierarchy = json.load(file)

        # Generate Mermaid flowchart
        flowchart_lines = generate_mermaid(hierarchy)
        mermaid_chart = "graph TD\n" + "\n".join(flowchart_lines)

        # Render the chart in the HTML template
        return render_template_string(HTML_TEMPLATE, mermaid_chart=mermaid_chart)
    except Exception as e:
        return f"Error processing data.json: {e}", 400


if __name__ == "__main__":
    app.run(debug=True)
