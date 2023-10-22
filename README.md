# AWS 2023 Icons Pack for Draw.io

## How to prepare

1. Go to https://aws.amazon.com/architecture/icons/ and download the latest Asset Package (currently it is a pack from 2023.10.18)
2. Remove all files from the `Latest Icons` and `Libs` folders and unpack the asset package into the `Latest Icons` folder.
3. It seems like Amazon changes the structure all the time, so please make sure that you have no "size" versions in folders. In the latest pack, the folder `Architecture-Service-Icons_10182023` contained subfolders like `16`, `32`, `48`, `64`. So, you have to fix it before the conversion, by running the following script: `python3 ./Converters/FixDirStructure.py ./LatestIcons/Architecture-Service-Icons_10182023`. This script removes all unecessary folders, and move files from the subfolder `48` to the root folder
4. Check out `Resource-Icons_10182023/Res_General-Icons` folder. It might contain 2 subfolders: `Res_48_Dark` and `Res_48_Light`. Remove `Res_48_Dark` folder, and place all files from `Res_48_Light` to the root folder (and remove the empty `Res_48_Light` subfolder obviously)
5. For each folder, execute the following script: `python3 ./Converters/Convert2DrawIOLib.py ./LatestIcons/Name_Of_The_Folder ./Libs "AWS23"`

## How to put libs to draw.io

TBD