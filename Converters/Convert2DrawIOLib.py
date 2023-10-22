import os
import base64
import json

def get_svg_content_as_base64(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    # Remove XML declaration
    content = content.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '').strip()
    return 'data:image/svg+xml;base64,' + base64.b64encode(content.encode('utf-8')).decode('utf-8')

def generate_json_object(filename, svg_base64):
    title = filename.split('-')[-1].replace('_48_Light','').replace('_48', '').replace('_', ' ').replace('.svg', '')
    return {
        "data": svg_base64,
        "w": 48,
        "h": 48,
        "title": title,
        "aspect": "fixed"
    }

def main(source_dir, output_dir, output_prefix):
    for root, _, files in os.walk(source_dir):

        svg_files = [f for f in files if f.endswith('.svg')]
        if not svg_files:
            continue

        json_array = []
        for svg_file in svg_files:
            filepath = os.path.join(root, svg_file)
            svg_base64 = get_svg_content_as_base64(filepath)
            json_obj = generate_json_object(svg_file, svg_base64)
            json_array.append(json_obj)

        # Create output XML file
        folder_name = os.path.basename(root).replace('_', ' ').replace('-', ' ')
        output_file = os.path.join(output_dir, f"{output_prefix} {folder_name}.xml")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('<mxlibrary>')
            file.write(json.dumps(json_array))
            file.write('</mxlibrary>')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process SVG files into XML")
    parser.add_argument('source_dir', type=str, help='Source directory with SVG files')
    parser.add_argument('output_dir', type=str, help='Output directory for XML files')
    parser.add_argument('output_prefix', type=str, help='Prefix for library files')
    args = parser.parse_args()

    main(args.source_dir, args.output_dir, args.output_prefix)
