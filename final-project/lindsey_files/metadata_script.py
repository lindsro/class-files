import csv

# Replace these with your file paths
csv1_path = 'file1.csv'
csv2_path = 'file2.csv'
output_matched_path = 'matched.csv'
output_unmatched_path = 'unmatched.csv'

# Read CSV2 and store filenames indexed by their possible identifiers
filenames = []
with open(csv2_path, newline='', encoding='utf-8') as f2:
    reader2 = csv.DictReader(f2)
    for row in reader2:
        filenames.append(row['filename'])

matched_rows = []
unmatched_rows = []

with open(csv1_path, newline='', encoding='utf-8') as f1:
    reader1 = csv.DictReader(f1)
    # Prepare header for output file: all columns from CSV1 + filename
    output_fieldnames = reader1.fieldnames + ['filename']

    for row1 in reader1:
        identifier = row1['dcterms:Identifier']
        found = False
        for fn in filenames:
            # Check if filename begins with identifier followed by underscore
            if fn.startswith(identifier + '_'):
                new_row = row1.copy()
                new_row['filename'] = fn
                matched_rows.append(new_row)
                found = True
                break  # Only take the first match; remove "break" for multiple matches per identifier
        if not found:
            unmatched_rows.append(row1)

# Write matched rows to output CSV
with open(output_matched_path, 'w', newline='', encoding='utf-8') as fout:
    writer = csv.DictWriter(fout, fieldnames=output_fieldnames)
    writer.writeheader()
    writer.writerows(matched_rows)

# Write unmatched rows to another output CSV
with open(output_unmatched_path, 'w', newline='', encoding='utf-8') as fout_unmatched:
    writer_unmatched = csv.DictWriter(fout_unmatched, fieldnames=reader1.fieldnames)
    writer_unmatched.writeheader()
    writer_unmatched.writerows(unmatched_rows)

print(f"Done! Matched rows saved to {output_matched_path}. Unmatched rows saved to {output_unmatched_path}.")