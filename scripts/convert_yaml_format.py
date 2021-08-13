"""
Generate JSON & CSV versions of the source YAML taxonomies, for convenience
"""
import yaml
import json
import csv

YAML_FILES = ["../data_categories.yml"]

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
                unique_keys = set(flattened_keys)

                # Write out the CSV file
                csv_writer = csv.DictWriter(csv_file, fieldnames=unique_keys)
                csv_writer.writeheader()
                for item in yaml_dict[toplevel_key]:
                    csv_writer.writerow(item)
