import csv

# Input and output file paths
input_file = 'application_to_business.csv'
output_file = 'output_application_to_business.csv'

def process_csv(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # Extract elements from the row
            start = row[0]
            relationships = row[1].strip('"').split(',')
            end = row[2]
            
            # Write each new line
            for relationship in relationships:
                writer.writerow([start, relationship, end])

# Process the CSV file
process_csv(input_file, output_file)
