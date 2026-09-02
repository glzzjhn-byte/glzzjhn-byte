import urllib.request
import xml.etree.ElementTree as ET
import re

GROUP_ID = "io.github.glzzjhn-byte"

GROUP_PATH = GROUP_ID.replace('.', '/')
BASE_URL = f"https://repo1.maven.org/maven2/{GROUP_PATH}/"

try:
    print(f"Scanning live Maven directory: {BASE_URL}")
    
    req = urllib.request.urlopen(BASE_URL)
    html = req.read().decode('utf-8')
    
    packages = re.findall(r'<a href="([^"]+)/"', html)
    packages = [p for p in packages if not p.startswith('.')]
    
    print(f"Found {len(packages)} packages: {', '.join(packages)}")
    
    markdown_content = ""
    
    for artifact in packages:
        metadata_url = f"{BASE_URL}{artifact}/maven-metadata.xml"
        try:
            meta_req = urllib.request.urlopen(metadata_url)
            meta_xml = meta_req.read().decode('utf-8')
            root = ET.fromstring(meta_xml)
            
            version = None
            versioning = root.find('versioning')
            if versioning is not None:
                latest = versioning.find('latest')
                release = versioning.find('release')
                if latest is not None and latest.text:
                    version = latest.text
                elif release is not None and release.text:
                    version = release.text
            
            if version:
                print(f" -> Generating XML for {artifact} (v{version})")
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
        except Exception as e:
            print(f" -> Skipping {artifact} (Could not read metadata: {e})")
            
    with open("README.md", "r") as file:
        readme = file.read()
        
    start_marker = "<!-- MAVEN-START -->\n"
    end_marker = "<!-- MAVEN-END -->"
    
    start_idx = readme.find(start_marker)
    end_idx = readme.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_readme = readme[:start_idx + len(start_marker)] + markdown_content + readme[end_idx:]
        if new_readme != readme:
            with open("README.md", "w") as file:
                file.write(new_readme)
            print("Successfully updated README.md with live package data!")
        else:
            print("No changes needed in README.md.")
    else:
        print("Error: Could not find the MAVEN-START or MAVEN-END markers.")
        
except Exception as e:
    print(f"Error scraping Maven repository: {e}")
