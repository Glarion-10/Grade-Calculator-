Classroom Grade Calculator

This Python program calculates the final grades for students based on their assignment, midterm, and final exam scores. The program uses weighted percentages to compute the final grade for each student and generates a summary of the class performance, including the highest, lowest, and average grades.

How It Works

Input File: The program reads student data from an input file named grades_input.txt. This file should contain the student's name, assignment score, midterm score, and final exam score, all separated by commas.

Example format of grades_input.txt:

Alice,85,90,88

Bob,75,80,78

Charlie,95,85,92


Weighted Calculation: The program calculates the final grade using the following weights

Assignments: 40%

Midterm: 30%

Final Exam: 30%


Final Grade = (Assignments * 0.4) + (Midterm * 0.3) + (Final Exam * 0.3)

Output File: The program writes the final grades to an output file named grades_output.txt. Each line in the output file contains the student's name and their final grade, rounded to two decimal places.

Example format of grades_output.txt:

Alice,87.40

Bob,77.40

Charlie,91.10


Summary: The program also calculates and displays the following statistics:

The student with the highest grade.

The student with the lowest grade.

The class average grade.

How to Use

Prepare the Input File:

Create a text file named grades_input.txt.

Add student data in the format Name,AssignmentScore,MidtermScore,FinalScore.

Ensure each student's data is on a new line.

Run the Program:

Execute the Python script cps109_a1.py.

The program will read the input file, calculate the grades, and generate the output file.

Check the Output:

The final grades will be saved in grades_output.txt.

The program will also print the grades and a summary of the class performance in the console.


Ensure that the input file is correctly formatted and that all scores are valid numbers.
The program assumes that the input file exists and is properly formatted. If the file is missing or incorrectly formatted, the program may raise an error.



