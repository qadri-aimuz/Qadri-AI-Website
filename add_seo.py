import os
import re

base_dir = r"C:\Users\Muzamil\Desktop\Source Code\Qadri AI Website"
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

seo_tags_template = """
    <!-- SEO Meta Tags -->
    <meta name="description" content="Qadri AI is the ultimate advanced desktop AI assistant offering smart automation, real-time support, and powerful capabilities.">
    <meta name="keywords" content="Qadri AI, AI Desktop Assistant, Offline AI, Productivity, Software, Automation">
    <meta name="author" content="Qadri AI Team">
    <meta name="robots" content="index, follow">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://qadri-ai-website.vercel.app{path}">
    <meta property="og:title" content="Qadri AI - The Ultimate Desktop Assistant">
    <meta property="og:description" content="Qadri AI is the ultimate advanced desktop AI assistant offering smart automation, real-time support, and powerful capabilities.">
    <meta property="og:image" content="https://qadri-ai-website.vercel.app/og-image.jpg">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://qadri-ai-website.vercel.app{path}">
    <meta property="twitter:title" content="Qadri AI - The Ultimate Desktop Assistant">
    <meta property="twitter:description" content="Qadri AI is the ultimate advanced desktop AI assistant offering smart automation, real-time support, and powerful capabilities.">
    <meta property="twitter:image" content="https://qadri-ai-website.vercel.app/og-image.jpg">

    <!-- Canonical URL -->
    <link rel="canonical" href="https://qadri-ai-website.vercel.app{path}">
"""

for file_name in html_files:
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has SEO tags
    if 'name="description"' in content:
        continue

    # Determine path for canonical/og urls
    path_suffix = "" if file_name == "index.html" else f"/{file_name.replace('.html', '')}"
    seo_tags = seo_tags_template.replace('{path}', path_suffix)

    # Insert just before </head>
    content = content.replace('</head>', f"{seo_tags}</head>")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("SEO tags successfully injected into all HTML files!")
