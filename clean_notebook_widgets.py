import os
import json

def clean_widgets_metadata_in_notebooks(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ipynb"):
                notebook_path = os.path.join(root, file)
                print(f"Checking: {notebook_path}")

                with open(notebook_path, "r", encoding="utf-8") as f:
                    notebook = json.load(f)

                # Check if metadata.widgets exists
                widgets = notebook.get("metadata", {}).get("widgets")
                if widgets is not None:
                    # Fix or remove the widgets metadata
                    if "state" not in widgets:
                        print(f" - Fixing or removing malformed 'widgets' metadata")

                        # Either remove it or insert an empty 'state'
                        # Option A: Remove the widgets metadata
                        del notebook["metadata"]["widgets"]

                        # Option B (uncomment to use): Insert default state instead
                        # notebook["metadata"]["widgets"]["state"] = {}

                        # Save the fixed notebook
                        with open(notebook_path, "w", encoding="utf-8") as f:
                            json.dump(notebook, f, indent=1, ensure_ascii=False)
                        print(f" - Updated: {notebook_path}")
                    else:
                        print(" - 'widgets' metadata already valid")

    print("✅ Done cleaning notebooks.")

# Replace this with the path to your folder
folder_to_clean = "/Users/iftekhar/Documents/Projects/Open-Source-Models-using-Hugging-Face"  # current directory
clean_widgets_metadata_in_notebooks(folder_to_clean)
