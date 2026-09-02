import urllib.request
import json
import re

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
        
        markdown_content += f"""
<details>
<summary>📦 <b>{artifact}</b> (<code>{GROUP_ID}:{artifact}:{version}</code>)</summary>
<br>

**Maven Implementation:**
