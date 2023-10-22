import os
import shutil

def process_directory(directory):
    # List the contents of the directory
    subdirs = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    print(f"{directory}: {subdirs}")

    # Recursively process other subdirectories
    folders2remove = {"16", "32", "64"}
    for subdir in subdirs:
        if subdir in folders2remove:
            shutil.rmtree(os.path.join(directory, subdir))
        elif subdir == "48":
          src_path = os.path.join(directory, "48")
          for item in os.listdir(src_path):
              if item == ".DS_Store":
                  os.remove(os.path.join(src_path, item))
              else:
                shutil.move(os.path.join(src_path, item), directory)
          os.rmdir(src_path)
        else:
          process_directory(os.path.join(directory, subdir))

def main(input_dir):
    process_directory(input_dir)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process subdirectories")
    parser.add_argument('input_dir', type=str, help='Input directory path')
    args = parser.parse_args()

    main(args.input_dir)
