import urllib.request
import json

GROUP_ID = "io.github.glzzjhn-byte"
URL = f"https://search.maven.org/solrsearch/select?q=g:\"{GROUP_ID}\"&rows=20&wt=json"

try:
    req = urllib.request.urlopen(URL)
    data = json.loads(req.read().decode('utf-8'))
    docs = data.get('response', {}).get('docs', [])
    
    markdown_content = ""
    for doc in docs:
        artifact = doc.get('a')
        version = doc.get('latestVersion')
        
        # Bulletproof string formatting (no triple quotes)
        markdown_content += (
            "<details>\n"
            f"  <summary>📦 <b>{artifact}</b> (<code>{GROUP_ID}:{artifact}:{version}</code>)</summary>\n"
            "  <br>\n\n"
            "  **Maven Implementation:**\n"
            "  ```xml\n"
            "  <dependency>\n"
            f"      <groupId>{GROUP_ID}</groupId>\n"
            f"      <artifactId>{artifact}</artifactId>\n"
            f"      <version>{version}</version>\n"
            "  </dependency>\n"
            "  ```\n"
            "</details>\n<br>\n"
        )
        
    with open("README.md", "r") as file:
        readme = file.read()
        
    start_marker = "<!-- MAVEN-START -->\n"
    end_marker = "<!-- MAVEN-END -->"
    
    start_idx = readme.find(start_marker)
    end_idx = readme.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_readme = readme[:start_idx + len(start_marker)] + markdown_content + readme[end_idx:]
        
        with open("README.md", "w") as file:
            file.write(new_readme)
            print("Successfully updated README.md!")
    else:
        print("Error: Could not find the MAVEN-START or MAVEN-END markers in the README.")
        
except Exception as e:
    print(f"Error fetching Maven data: {e}")
