"""
Generate JSON & CSV versions of the source YAML taxonomies, for convenience
"""
import yaml
import json
import csv

YAML_FILES = ["../data_categories.yml", "../data_uses.yml", "../data_subjects.yml", "../data_qualifiers.yml"]

if __name__ == "__main__":
    for input_filename in YAML_FILES:
        with open(input_filename, "r") as input_file:
            print(f"Loading YAML from {input_filename}...")
            yaml_dict = yaml.safe_load(input_file)
            json_filename = input_filename.replace("yml", "json")
            with open(json_filename, "w") as json_file:
                print(f"Writing JSON to {json_filename}...")
                json_str = json.dumps(yaml_dict, indent=4)
                print(json_str, file=json_file)
            csv_filename = input_filename.replace("yml", "csv")
            with open(csv_filename, "w") as csv_file:
                print(f"Writing csv to {csv_filename}...")
                assert len(yaml_dict.keys()) == 1 # should only have a single top-level key
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

                print(f"headers: {unique_keys}")
                csv_writer = csv.DictWriter(csv_file, fieldnames=unique_keys)
                csv_writer.writeheader()

                # For convenience, generate a single "root" node
                assert { "fides_key", "name", "parent_key" }.issubset(unique_keys)
                root_key = toplevel_key.replace("-", "_")
                root_name = " ".join([word.capitalize() for word in root_key.split("_")])
                root_node = { "fides_key": root_key, "name": root_name }
                print(f"Generating root node: {root_node}...")
                csv_writer.writerow(root_node)

                for item in yaml_dict[toplevel_key]:
                    if item.get("parent_key", None) is not None:
                        # Write out the item normally if it has a parent
                        csv_writer.writerow(item)
                    else:
                        # Insert the new "root" node for items that have no parent
                        new_item = { "parent_key": root_key }
                        new_item.update(item)
                        csv_writer.writerow(new_item)
