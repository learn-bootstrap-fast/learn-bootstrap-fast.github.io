#!/usr/bin/env python3
import re

input_file = "sitemap.xml"
output_file = "aws-links.txt"

pattern = re.compile(r"https?://[^\s<]*?/videos/aws/[^\s<]*")

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

links = pattern.findall(text)

with open(output_file, "w", encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")

print(f"Extracted {len(links)} AWS video links to {output_file}")
