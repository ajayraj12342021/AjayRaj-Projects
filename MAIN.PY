import os

def arrange_files(directory, ext):
    if not ext.startswith('.'):
        ext = f'.{ext}'
    ext = ext.lower()

    os.makedirs(os.path.join(directory, "Images"), exist_ok=True)

    files_with_ext = [
        name for name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, name))
        and os.path.splitext(name)[1].lower() == ext
    ]

    for i, name in enumerate(files_with_ext, start=1):
        src = os.path.join(directory, name)
        dest = os.path.join(directory, "Images", f"photo-{i}{ext}")

        while os.path.exists(dest):
            i += 1
            dest = os.path.join(directory, "Images", f"photo-{i}{ext}")

        os.rename(src, dest)
        print(f"Moved {name} -> {dest}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    arrange_files(base_dir, ".jpg")
    
