"""
Export the Default Fideslang Taxonomy as YAML, JSON and CSV files.
"""
import csv
import json
import shutil
import yaml
from fideslang.default_taxonomy import DEFAULT_TAXONOMY
from fideslang.manifests import write_manifest
from typing import Tuple
from packaging.version import Version

FILE_RESOURCE_PAIRS: Tuple[Tuple[str, str], ...] = (
    ("data_categories", "data_category"),
    ("data_subjects", "data_subject"),
    ("data_uses", "data_use"),
)
DATA_DIR = "data_files"
DOCS_CSV_DIR = "mkdocs/docs/csv"


def export_yaml() -> None:
    """
    Export the default Taxonomy as YAML files.
    """

    for filename, resource_type in FILE_RESOURCE_PAIRS:
        output_filename = f"{DATA_DIR}/{filename}.yml"
        print(f"> Writing YAML to {output_filename}")
        resources = [x.dict() for x in getattr(DEFAULT_TAXONOMY, resource_type)]

        write_manifest(
            output_filename,
            manifest=resources,
            resource_type=resource_type,
        )


def export_json() -> None:
    """
    Load the default Taxonomy from their YAML files and re-export as JSON.
    """
    for filename, _ in FILE_RESOURCE_PAIRS:
        input_filename = f"{DATA_DIR}/{filename}.yml"
        json_filename = input_filename.replace("yml", "json")

        with open(input_filename, "r") as input_file:
            print(f"> Loading YAML from {input_filename}...")
            yaml_dict = yaml.safe_load(input_file)
            with open(json_filename, "w") as json_file:
                print(f"> Writing JSON to {json_filename}...")
                json_str = json.dumps(yaml_dict, indent=4)
                print(json_str, file=json_file)


def export_csv() -> None:
    for filename, _ in FILE_RESOURCE_PAIRS:
        input_filename = f"{DATA_DIR}/{filename}.yml"
        csv_filename = input_filename.replace("yml", "csv")
        docs_filename = f"{DOCS_CSV_DIR}/{filename}.csv"

        # Load the Taxonomy from the YAML file
        with open(input_filename, "r") as input_file:
            print(f"> Loading YAML from {input_filename}...")
            yaml_dict = yaml.safe_load(input_file)

        with open(csv_filename, "w") as csv_file:
            print(f"> Writing csv to {csv_filename}...")
            assert len(yaml_dict.keys()) == 1  # should only have a single top-level key
            toplevel_key = next(iter(yaml_dict))

            # Compute a unique set of keys used across all the sub-items
            list_of_keys = [item.keys() for item in yaml_dict[toplevel_key]]
            flattened_keys = [keys for sublist in list_of_keys for keys in sublist]
            unique_keys = sorted(list(set(flattened_keys)))

            # Insert the parent_key if not defined
            if "parent_key" not in unique_keys:
                unique_keys.append("parent_key")

            # Write out the CSV file headers. Put "description" last, for readability
            if "description" in unique_keys:
                unique_keys.remove("description")
                unique_keys.append("description")

            print(f"Headers: {unique_keys}")
            csv_writer = csv.DictWriter(csv_file, fieldnames=unique_keys)
            csv_writer.writeheader()

            # For visualizing as a hierarchy, generate a virtual "root" node to be a single parent
            assert {"fides_key", "name", "parent_key"}.issubset(
                unique_keys
            ), "Missing required keys for CSV!"
            root_key = toplevel_key.replace("-", "_")
            root_name = " ".join([word.capitalize() for word in root_key.split("_")])
            root_node = {"fides_key": root_key, "name": root_name}
            print(f"Generating root node: {root_node}...")
            csv_writer.writerow(root_node)

            for item in yaml_dict[toplevel_key]:
                if item.get("parent_key", None) is not None:
                    # Write out the item normally if it has a parent
                    csv_writer.writerow(item)
                else:
                    # Insert the new "root" node for items that are top-level nodes
                    new_item = {"parent_key": root_key}
                    item.update(new_item)
                    print(f"Edited parent for {item['fides_key']}")
                    csv_writer.writerow(item)

        print(f"> Copying csv to docs site at {docs_filename}...")
        shutil.copy(csv_filename, docs_filename)


if __name__ == "__main__":
    print("Exporting YAML files...")
    export_yaml()
    print("*" * 40)

    print("Exporting JSON files...")
    export_json()
    print("*" * 40)

    print("Exporting JSON files...")
    export_csv()
    print("*" * 40)

    print(f"Export complete! Check '{DATA_DIR}/' for output files.")
