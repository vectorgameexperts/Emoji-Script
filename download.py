import os
import requests

output_folder_svg = "svg_files"
output_folder_lottie = "lottie_files"
os.makedirs(output_folder_svg, exist_ok=True)
os.makedirs(output_folder_lottie, exist_ok=True)

with open("emoji-lotties.csv", encoding="UTF8") as f:
    lines = f.readlines()
    first_line_skipped = False
    print("Starting...")
    for line in lines:
        if not first_line_skipped:
            first_line_skipped = True
            continue
        values = line.split(",")
        name = values[0].replace(".json", "").strip()
        svg = values[1].strip()
        lottie = values[2].strip()
        print(f"Downloading {name}...", end="")
        svg_filename = os.path.join(output_folder_svg, f"{name}.svg")
        r = requests.get(svg, allow_redirects=True, timeout=5000)
        open(svg_filename, "wb").write(r.content)
        print("svg...", end="")
        lottie_filename = os.path.join(output_folder_lottie, f"{name}.json")
        r = requests.get(lottie, allow_redirects=True, timeout=5000)
        open(lottie_filename, "wb").write(r.content)
        print("lottie")
