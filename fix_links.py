import os
import re

base_dir = r"C:\Users\Muzamil\Desktop\Source Code\Qadri AI Website"

# 1. Create vercel.json
vercel_json_path = os.path.join(base_dir, "vercel.json")
with open(vercel_json_path, 'w', encoding='utf-8') as f:
    f.write('{\n  "cleanUrls": true\n}')

# 2. Fix all .html links inside HTML files
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

for file_name in html_files:
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace href="about.html" with href="/about"
    content = re.sub(r'href=["\']about\.html["\']', 'href="/about"', content)
    content = re.sub(r'href=["\']purchase\.html["\']', 'href="/purchase"', content)
    content = re.sub(r'href=["\']features\.html["\']', 'href="/features"', content)
    content = re.sub(r'href=["\']preview\.html["\']', 'href="/preview"', content)
    content = re.sub(r'href=["\']index\.html["\']', 'href="/"', content)

    # Optional: If there are links without leading slash like href="about"
    # the vercel.json cleanUrls handles it, but /about is cleaner.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("vercel.json created and all .html links fixed!")
