# FL-Studio-file-path-extractor

an FL-Studio-file-path-extractor FTW

# FL Studio Missing Sample Path Extractor

This small project provides a script to extract the paths of missing samples from FL Studio `.flp` project files. The tool simplifies the process of resolving missing sample issues by listing paths, even for samples that are not easily visible in FL Studio.

## Features

- **Extract Sample Paths**: Automatically scans FL Studio project files for all sample paths.
- **Identify Missing Samples**: Highlights channels with missing sample paths.
- **Save to File**: Outputs the extracted paths to a text file for easy reference.

## Requirements

- Python 3.8+
- [`pyflp`](https://pypi.org/project/pyflp/) library for parsing FL Studio project files

## Usage

1. create pyflstudio.py and copy the python code into it. 

2. Install the required dependencies:
   ```bash
   pip install pyflp
   ```

## Usage

1. Run the script with the path to an `.flp` file as an argument (put the FLP file in the same direcotry as pyflstudio.py):
   ```bash
   python pyflstudio.py path/to/project.flp
   ```

2. The script will process the project file and output the paths of the samples to `sample_paths.txt`.

### Example

```bash
python pyflstudio.py my_project.flp
```

- Output file: `sample_paths.txt`
- Contents:
  ```
  C:\Samples\Kick.wav
  D:\Audio\Snare.wav
  ```

## Handling Errors

If the script encounters any issues while parsing the `.flp` file or saving paths, detailed error messages will be displayed in the terminal.

### Common Issues

- **Corrupt or unsupported `.flp` file**: Ensure the file is a valid FL Studio project.
- **Missing `pyflp` library**: Install it using `pip install pyflp`.
- Use this fix if needed!!!!!!!!!!!!!!!!!! https://github.com/demberto/PyFLP/issues/183#issuecomment-2490292942

## Contributions

Feel free to submit issues or pull requests to improve the functionality.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [FL Studio](https://www.image-line.com/) for their powerful DAW.
- [pyflp](https://github.com/chrislorenz/pyflp) for making `.flp` file parsing possible.
