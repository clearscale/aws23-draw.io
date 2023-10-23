# AWS 2023 Icon Pack for Draw.io

## Preparation Steps

1. Visit https://aws.amazon.com/architecture/icons/ and download the most recent Asset Package (as of now, the version is from 2023.10.18).
2. Clear all files in the `Latest Icons` and `Libs` folders, then extract the asset package to the `Latest Icons` folder.
3. Amazon seems to adjust the structure regularly, so ensure there aren't any "size" versions in folders. For instance, in the recent pack, the `Architecture-Service-Icons_10182023` folder had subfolders named `16`, `32`, `48`, `64`. To correct this, run the script: : `python3 ./Converters/FixDirStructure.py ./LatestIcons/Architecture-Service-Icons_10182023`. This script eliminates unnecessary folders and shifts files from the `48` subfolder to the main folder.
4. Inspect the `Resource-Icons_10182023/Res_General-Icons` directory. It might have two subfolders: `Res_48_Dark` and `Res_48_Light`. Remove the `Res_48_Dark` folder, move all files from `Res_48_Light` to the main directory, and then delete the now-empty `Res_48_Light` folder.
5. Inspect the `Category-Icons_10182023` folder. Remove the `Arch-Category_16`, `Arch-Category_32`, and `Arch-Category_64` subfolders. Then, transfer files from `Arch-Category_48` up one level and delete the now-empty `Arch-Category_48` folder.
6. For each directory, run the script:  `python3 ./Converters/Convert2DrawIOLib.py ./LatestIcons/Name_Of_The_Folder ./Libs "AWS23"`
7. Now, run the following script: `python3 Converters/GenerateConfigFiles.py ./Libs` - it will generate config files for web and VSCode versions.

## Integrating AWS23 Icons
### Integrating AWS23 Icons into the Web-Based Draw.io

1. Go to https://draw.io
2. Start a new file.
3. Choose the "Extras/Configuration" option from the menu.
4. In the `Configuration` field, paste the content from https://raw.githubusercontent.com/clearscale/aws23-draw.io/main/Libs/web-config.json and click the `Apply` button.
5. Refresh the webpage.
6. Click the `+ More Shapes` button on the left toolbar. Select `AWS23 Icons` and click `Apply`. Now, all AWS icons, categorized by type, are available in the left toolbar.

### Integrating AWS23 Icons into the VS Code extention

1. Install the `Draw.io Integration` extension for VSCode by visiting [this link](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio).
2. Navigate to `Code > Settings > Settings` from the menu.
3. In the `Extensions` section, select the `Draw.io Integration` option.
4. Locate the `Custom Libraries` section and click the `Edit in settings.json` link.
5. Copy the content from [this link](https://raw.githubusercontent.com/clearscale/aws23-draw.io/main/Libs/vscode.json) and paste it as the value for the `hediet.vscode-drawio.customLibraries` entry.
6. Save the changes to the settings.json file and close it.
7. Create a new file with the `.drawio` extension.
8. Click the `+ More Shapes` button at the bottom of the toolbox menu on the left. Check the `AWS23` box under the `Custom Libraries` section and click the `Apply` button. All AWS icons, organized by type, are now accessible in the left toolbar.