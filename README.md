# AWS 2023 Icon Pack for Draw.io

## Preparation Steps

1. Visit https://aws.amazon.com/architecture/icons/ and download the most recent Asset Package (as of now, the version is from 2023.10.18).
2. Clear all files in the `Latest Icons` and `Libs` folders, then extract the asset package to the `Latest Icons` folder.
3. Amazon seems to adjust the structure regularly, so ensure there aren't any "size" versions in folders. For instance, in the recent pack, the `Architecture-Service-Icons_10182023` folder had subfolders named `16`, `32`, `48`, `64`. To correct this, run the script: : `python3 ./Converters/FixDirStructure.py ./LatestIcons/Architecture-Service-Icons_10182023`. This script eliminates unnecessary folders and shifts files from the `48` subfolder to the main folder.
4. Inspect the `Resource-Icons_10182023/Res_General-Icons` directory. It might have two subfolders: `Res_48_Dark` and `Res_48_Light`. Remove the `Res_48_Dark` folder, move all files from `Res_48_Light` to the main directory, and then delete the now-empty `Res_48_Light` folder.
5. For each directory, run the script:  `python3 ./Converters/Convert2DrawIOLib.py ./LatestIcons/Name_Of_The_Folder ./Libs "AWS23"`

## Adding Libraries to Draw.io

TBD