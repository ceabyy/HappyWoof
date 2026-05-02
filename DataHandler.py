import os, shutil, random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def split_dataset(source_dir, output_dir):
    for mood in os.listdir(source_dir):
        # Skip hidden files like .DS_Store
        if mood.startswith("."):
            continue
        
        images = [f for f in os.listdir(f"{source_dir}/{mood}") if not f.startswith(".")]
        random.shuffle(images)
        
        n = len(images)
        splits = {
            "train": images[:int(n*0.8)],
            "val":   images[int(n*0.8):int(n*0.9)],
            "test":  images[int(n*0.9):]
        }
        
        for split_name, files in splits.items():
            dest = f"{output_dir}/{split_name}/{mood}"
            os.makedirs(dest, exist_ok=True)
            for f in files:
                shutil.copy(f"{source_dir}/{mood}/{f}", dest)

split_dataset("data", "data_split")
print("Done! Your data has been split into data_split/train, val, and test.")
