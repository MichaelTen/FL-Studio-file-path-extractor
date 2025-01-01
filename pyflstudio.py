import pyflp
import sys
# YOU MAY NEED TO USE THIS FIX for pyflp IF MY PULL REQUEST IS NOT MERGED https://github.com/demberto/PyFLP/issues/183#issuecomment-2490292942 
# limitless blessings and limitless peace
def extract_sample_paths(flp_file_path):
    print(f"Attempting to load the FL Studio project file: {flp_file_path}")
    try:
        # Load the FL Studio project
        project = pyflp.parse(flp_file_path)
        print("Project loaded successfully.")
        
        # Extract and store all sample file paths
        sample_paths = []
        print("Iterating through project channels to find sample paths...")
        for i, channel in enumerate(project.channels):
            print(f"Processing channel {i + 1}: {channel}")
            
            # Check for sample path attributes
            if hasattr(channel, "sample_path") and channel.sample_path is not None:
                print(f"Sample path found in channel {i + 1}: {channel.sample_path}")
                sample_paths.append(str(channel.sample_path))  # Convert Path object to string
            elif hasattr(channel, "sample") and channel.sample is not None:
                # Fall back to the sample attribute if available
                print(f"Sample path (from sample attribute) found in channel {i + 1}: {channel.sample.file_path}")
                sample_paths.append(channel.sample.file_path)
            else:
                print(f"No sample path found in channel {i + 1}. Possibly a missing sample.")

        return sample_paths
    except Exception as e:
        print(f"An error occurred while loading the project or extracting samples: {e}")
        raise

def save_paths_to_file(paths, output_file):
    print(f"Saving {len(paths)} sample paths to file: {output_file}")
    try:
        with open(output_file, 'w') as file:
            for path in paths:
                file.write(path + '\n')
        print(f"Sample paths saved successfully to {output_file}.")
    except Exception as e:
        print(f"An error occurred while saving the sample paths to file: {e}")
        raise

# Main function
if __name__ == "__main__":
    print("Starting the script...")

    # Check if the file name is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py [flp_file.flp]")
        sys.exit(1)

    # Get the file name from command-line arguments
    flp_file = sys.argv[1]
    output_file = "sample_paths.txt"

    try:
        print(f"File provided: {flp_file}")
        paths = extract_sample_paths(flp_file)
        if paths:
            print(f"Sample Paths Found: {len(paths)} paths")
            save_paths_to_file(paths, output_file)
            print(f"Sample paths saved to: {output_file}")
        else:
            print("No sample paths found.")
    except Exception as e:
        print(f"An error occurred during execution: {e}")
