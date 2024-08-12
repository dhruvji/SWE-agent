import os
import subprocess
import shutil

# Set paths
trajectories_dir = '/Users/dhruv/Desktop/research/swe/SWE-agent/trajectories/run/'
django_codebase_dir = '/Users/dhruv/Desktop/research/swe/django_menial'  # Set this to your actual Django codebase path
destination_dir = '/Users/dhruv/Desktop/research/swe/patches/'  # Where you want to save the patched versions

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Iterate over each trajectory folder
for trajectory_folder in os.listdir(trajectories_dir):
    trajectory_path = os.path.join(trajectories_dir, trajectory_folder)
    
    if not os.path.isdir(trajectory_path):
        continue
    patches_folder = os.path.join(trajectory_path, 'patches')

    # Find the patch file in the patches folder
    for patch_file in os.listdir(patches_folder):
        if patch_file.endswith('.patch'):
            patch_path = os.path.join(patches_folder, patch_file)

            # Create a copy of the Django codebase
            new_codebase_path = os.path.join(destination_dir, trajectory_folder)
            shutil.copytree(django_codebase_dir, new_codebase_path)

            # Apply the patch
            patch_command = ['git', 'apply', patch_path]
            result = subprocess.run(patch_command, cwd=new_codebase_path, capture_output=True, text=True)

            if result.returncode != 0:
                print(f"Failed to apply patch for {trajectory_folder}: {result.stderr}")
            else:
                print(f"Successfully applied patch for {trajectory_folder} and saved to {new_codebase_path}")
