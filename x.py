import json

# Sample hierarchy JSON
hierarchy = {
    "name": "root",
    "children": [
        {
            "name": "child1",
            "children": [
                {
                    "name": "child1-1",
                    "children": []
                }
            ]
        },
        {
            "name": "child2",
            "children": [
                {
                    "name": "child2-1",
                    "children": []
                },
                {
                    "name": "child2-2",
                    "children": [
                        {
                            "name": "child2-2-1",
                            "children": []
                        }
                    ]
                }
            ]
        }
    ]
}

# Function to generate Mermaid flowchart


def generate_mermaid(node, parent=None):
    lines = []
    if parent:
        lines.append(f'{parent} --> {node["name"]}')
    for child in node.get("children", []):
        lines.extend(generate_mermaid(child, node["name"]))
    return lines


# Generate flowchart lines
flowchart_lines = generate_mermaid(hierarchy)

# Add the Mermaid flowchart header
mermaid_output = "graph TD\n" + "\n".join(flowchart_lines)

# Output the Mermaid flowchart
print(mermaid_output)

# Save to a file
with open("hierarchy_flowchart.mmd", "w") as file:
    file.write(mermaid_output)

print("Mermaid flowchart saved to 'hierarchy_flowchart.mmd'")
