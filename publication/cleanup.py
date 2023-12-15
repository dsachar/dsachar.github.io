import os

def remove_line_from_files(directory, line_to_delete):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                with open(file_path, 'w') as f:
                    for line in lines:
                        if line.strip() != line_to_delete:
                            f.write(line)

if __name__ == "__main__":
    # Specify the directory where your .md files are located
    directory = "./"

    # Specify the line to be deleted
    line_to_delete = "Add the **full text** or **supplementary notes** for the publication here using Markdown formatting."

    # Call the function to remove the line from the .md files
    remove_line_from_files(directory, line_to_delete)
