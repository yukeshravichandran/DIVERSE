import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the injected chat widget code block
# The block starts with "<!-- AI Chat Widget -->" and ends with "</script>\n" right before </body>
# But to be safe, we can use a regex or just string splitting
if "<!-- AI Chat Widget -->" in html:
    start_idx = html.find("<!-- AI Chat Widget -->")
    end_idx = html.find("</script>\n\n</body>", start_idx)
    if end_idx != -1:
        end_idx += len("</script>\n\n")
        html = html[:start_idx] + html[end_idx:]
    else:
        # Fallback if the newline structure is slightly different
        end_idx = html.find("</body>", start_idx)
        html = html[:start_idx] + "\n" + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Chat widget removed from index.html")
