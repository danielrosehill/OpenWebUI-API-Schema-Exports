import json
import os

def extract_paths(openapi_file, path_prefix=None):
    """
    Extracts paths from an OpenAPI JSON file.
    If path_prefix is provided, only paths starting with that prefix will be extracted.

    Args:
        openapi_file (str): Path to the OpenAPI JSON file.
        path_prefix (str, optional): Prefix to filter paths. If None, all paths are extracted.

    Returns:
        dict: A dictionary where keys are paths and values are the corresponding
              path definitions from the OpenAPI file.
    """
    with open(openapi_file, 'r') as f:
        data = json.load(f)

    extracted_paths = {}
    for path, definition in data.get('paths', {}).items():
#        if path_prefix is None or path.startswith(path_prefix):
        extracted_paths[path] = definition

    return extracted_paths


def generate_json_files(extracted_paths, output_dir="outputs"):
    """
    Generates separate JSON files for each extracted path, organized into folders.

    Args:
        extracted_paths (dict): Dictionary of extracted paths (from extract_paths).
        output_dir (str): Directory to save the JSON files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for path, definition in extracted_paths.items():
        # Get the category from the path (e.g., /api/v1/knowledge/... -> knowledge)
        path_parts = path.strip('/').split('/')
        if len(path_parts) >= 3 and path_parts[0] == 'api' and path_parts[1] == 'v1':
            category = path_parts[2]
        elif len(path_parts) >= 3 and path_parts[0] == 'ollama' or 'openai':
            category = path_parts[0]
        else :
            category = 'various'

        category_dir = os.path.join(output_dir, category)
            # Create category directory if it doesn't exist
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
    
            # Sanitize the filename: replace slashes and dots with underscores
        filename = path.replace("/", "_").replace(".", "_") + ".json"
        filepath = os.path.join(category_dir, filename)
            
        with open(filepath, 'w') as f:
            json.dump({path: definition}, f, indent=2)  # Wrap in a dictionary with the path as the key
        print(f"Generated JSON file: {filepath}")


def generate_markdown_files(extracted_paths, output_dir="outputs"):
    """
    Generates separate Markdown files for each extracted path, organized into folders.

    Args:
        extracted_paths (dict): Dictionary of extracted paths (from extract_paths).
        output_dir (str): Directory to save the Markdown files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for path, definition in extracted_paths.items():
        filename = path.replace("/", "_").replace(".", "_") + ".json"
        # Get the category from the path (e.g., /api/v1/knowledge/... -> knowledge)
        path_parts = path.strip('/').split('/')
        if len(path_parts) >= 3 and path_parts[0] == 'api' and path_parts[1] == 'v1':
            category = path_parts[2]
        elif len(path_parts) >= 3 and path_parts[0] == 'ollama' or 'openai':
            category = path_parts[0]
        else :
            category = 'various'

        category_dir = os.path.join(output_dir, category)
            
            # Create category directory if it doesn't exist
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            
        markdown_content = f"# {path}\n\n" # Top-level Header is the path itself

            # Add a table of contents to the markdown page
            # Use the keys from the path definitions, will work if your endpoints share structure
        if definition: # Add a definition check
            possible_top_level_operations = list(definition.keys())
            markdown_content += "## Table of contents:\n" # Level-2 header
            for operation in possible_top_level_operations:
                sanitized_operation = operation.replace(" ", "_")  # Sanitize for markdown link
                markdown_content += f"- [{operation}](#{operation})\n"
                markdown_content += "\n"
                # Next, iterate through the common API operation keys (get, post, etc):
            markdown_content += f"- [json file](./{filename})\n\n---\n"
            for operation, operation_details in definition.items():
                sanitized_operation = operation.replace(" ", "_")  # Sanitize for markdown link
                markdown_content += f"<a name=\"{operation}\"></a>\n" # Anchor href
                markdown_content += f"## {operation}\n\n"  # Level-2 header

                if isinstance(operation_details, dict):  # Check if the value is a dictionary
                      # Iterate over details in the API operation itself and display the details
                    for key, value in operation_details.items():
                        markdown_content += f"**{key}:** {value}\n\n"
                else:
                     markdown_content += f"{operation_details}\n\n" # Value is a string or neither, so post it.
        else:
             markdown_content += "No definition found for this endpoint.\n"

            # Sanitize the filename: replace slashes and dots with underscores
        filename = path.replace("/", "_").replace(".", "_") + ".md"
        filepath = os.path.join(category_dir, filename)
        with open(filepath, 'w') as f:
             f.write(markdown_content)
        print(f"Generated Markdown file: {filepath}")


if __name__ == "__main__":
    openapi_file = "full-schema.json"  # Replace with your file
    output_dir = "outputs"
    path_prefix = "/api/v1/"  # Extract all paths starting with /api/v1/

    extracted_paths = extract_paths(openapi_file, path_prefix)
    print(f"Extracted {len(extracted_paths)} paths with prefix '{path_prefix}'")
    generate_json_files(extracted_paths, output_dir)
    generate_markdown_files(extracted_paths, output_dir)
    print(f"Processing complete. Check the '{output_dir}' directory.")
