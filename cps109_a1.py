"""Classroom Grade Calculator: This Python program computes students 
to a final score based of scores on assignment, mid and finals A 
weighted total is computed for each student using the weight percentages
defined (40% Assignments, 30% Midterm, 30% Final) Read the input data 
from grades_input file txt, process that grades and write the output 
into a grades_output txt. In addition to scoring, the program also 
reviewed results to identify top, bottom and average performers  
 
A summary of how well the class did as a whole."""

# Classroom Grade Calculator

# Define the percentage of each section
assignment_percent = 0.4
midterm_percent = 0.3
final_percent = 0.3

# Function to calculate the grade of student
def calculate_grade(assignments, midterm, final):
    assignment_total = assignments * assignment_percent
    midterm_total = midterm * midterm_percent
    final_total = final * final_percent
    total_grade = assignment_total + midterm_total + final_total
    return total_grade

# Function to read data from the input file 
def read_input_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Removes extra whitespace
            parts = line.split(',')
            name = parts[0]  # First part is the student's name
            assignments = float(parts[1])  # Assignment grade
            midterm = float(parts[2])  # Midterm grade
            final = float(parts[3])  # Final grade
            data.append((name, assignments, midterm, final))  
    return data

# Function to write results in an output file
def write_output_file(filename, results):
    with open(filename, 'w') as file:
        for result in results:
            name = result[0]
            total_grade = result[1]
            file.write(f"{name},{total_grade:.2f}\n")  # Writes each student's result

# Function to calculate the highest grade
def calculate_max_grade(results):
    highest = results[0]  # Assume first result is highest
    for result in results:
        if result[1] > highest[1]:  # Comparing grades
            highest = result
    return highest

# Function to calculate the lowest grade
def calculate_min_grade(results):
    lowest = results[0]  # Assume first result is lowest
    for result in results:
        if result[1] < lowest[1]:  # Comparing grades
            lowest = result
    return lowest

# Function to calculate the average grade
def average_grade(results):
    total = 0  # Initially the total is 0
    for result in results:
        total += result[1]  # Add each grade to total
    average = total / len(results)  # Divide by number of results
    return average

# Function to display the summary
def show_summary(highest, lowest, average):
    # print(f"Highest Grade: {highest[0]} with {highest[1]:.2f}")
    print(f"Lowest Grade: {lowest[0]} with {lowest[1]:.2f}")
    print(f"Class Average: {average:.2f}")

# Main program
def main():
    input_file = "grades_input.txt"
    output_file = "grades_output.txt"

    # Read student data
    student_data = read_input_file(input_file)

    # Process grades
    results = []
    for student in student_data:
        name = student[0]
        assignments = student[1]
        midterm = student[2]
        final = student[3]
        total_grade = calculate_grade(assignments, midterm, final)
        results.append((name, total_grade))

    # Write results to output file
    write_output_file(output_file, results)

    # Calculate statistics
    highest = calculate_max_grade(results)
    lowest = calculate_min_grade(results)
    average = average_grade(results)

    # Display results
    print("The final grades have been calculated and have been saved to the file:")
    for result in results:
        print(f"{result[0]}: {result[1]:.2f}")

    # Display summary
    show_summary(highest, lowest, average)

# Run program
if __name__ == "__main__":
    main()
