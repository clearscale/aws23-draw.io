import os
import json
import urllib.parse

def main(directory):
    xml_files = sorted([f for f in os.listdir(directory) if f.endswith('.xml')])

    web_config = []
    vscode_config = {
        "hediet.vscode-drawio.customLibraries": []
    }

    for file in xml_files:
        # Process file name to get LIBRARY_NAME
        parts = file.replace('.xml','').split(' ')
        library_name = parts[0]
        if len(parts) > 1:
            library_name += " / " + parts[1]
        if len(parts) > 2:
            library_name += " / " + ' '.join(parts[2:])
        
        # Create LIBRARY_URL
        library_url =  "https://raw.githubusercontent.com/clearscale/aws23-draw.io/main/Libs/" + urllib.parse.quote(file)
        
        # Append data to the configurations
        web_config.append({
            "title": {
                "main": library_name
            },
            "url": library_url
        })

        vscode_config["hediet.vscode-drawio.customLibraries"].append({
            "entryId": "AWS23",
            "libName": library_name,
            "url": library_url
        })

    # Write data to json files

    with open(os.path.join(directory,'web-config.json'), 'w') as f:
        json.dump({
                    "libraries": 
                    [ 
                      {
                        "title": { "main": "AWS23" },
                        "entries": [ 
                          {
                            "id": "aws23",
                            "title": { "main": "AWS23 Icons" },
                            "desc": {  "main": "Collection of AWS icons" },
                            "libs": web_config
                          }
                        ]
                      }
                    ]
                  }, f, indent=4)
    
    with open(os.path.join(directory,'vscode.json'), 'w') as f:
        json.dump(vscode_config["hediet.vscode-drawio.customLibraries"], f, indent=4)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <directory>")
        sys.exit(1)

    main(sys.argv[1])
