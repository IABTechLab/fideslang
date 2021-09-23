"""
Re-create the YAML data category taxonomy from a CSV file. Used when we have to
edit the CSV file directly instead of the YAML source.
"""
import yaml
import json
import csv

CSV_FILE = "../data_categories.csv"

if __name__ == "__main__":
    with open(CSV_FILE, "r") as input_file:
        print(f"Loading CSV from {CSV_FILE}...")
        csv_reader = csv.reader(input_file, delimiter=',')
        yaml_dict = { "data-category": [] }
        line_no = 0
        for row in csv_reader:
            line_no += 1
            if line_no <= 2:
                continue
            node = {
                "fides_key": row[0],
                "name": row[1],
                "parent_key": row[2],
                "description": row[3]
            }
            yaml_dict["data-category"].append(node)

        yaml_filename = CSV_FILE.replace("csv", "yml")
        with open(yaml_filename, "w") as yaml_file:
            print(f"Writing YAML to {yaml_filename}...")
            yaml_str = yaml.dump(yaml_dict, width=120, sort_keys=False)
            print(yaml_str, file=yaml_file)
