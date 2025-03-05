// ✅ Requirements:

// 1️⃣ Create a Student class
// 	•	Attributes:
// 	•	studentName (String)
// 	•	studentID (int)
// 	•	grades (ArrayList) → Stores multiple grades.
// 	•	Methods:
// 	•	addGrade(double grade) → Adds a grade to the student’s list.
// 	•	calculateAverage() → Returns the average of all grades.
// 	•	displayInfo() → Prints student name, ID, grades, and average grade.

// 2️⃣ Create a StudentManagement Class (Main Program)
// 	•	The program should allow users to:
// 	1.	Add a new student
// 	2.	Add grades to a student
// 	3.	Calculate and display the student’s average grade
// 	4.	List all students and their grades
// 	5.	Exit the program
// 	•	Use a looping menu so the user can perform multiple actions.

// --- Student Grade Management System ---
// 1. Add a new student
// 2. Add grade to a student
// 3. Display student's average grade
// 4. List all students
// 5. Exit

// 1. add student to an exiting list --> input: name, id
// 2. add grade to a student --> input: id, grade
// 3. display a student's average grade --> input: id
// 4. list all students in the student list --> input: 4
// 5. exit the system --> input: 5

import java.util.ArrayList;

public class Student {
    private String student_name;
    private int student_id;
    private ArrayList<Double> grades;

    // Constructor
    public Student(String student_name, int student_id) {
        this.student_name = student_name;
        this.student_id = student_id;
        this.grades = new ArrayList<>();
    }

    // Method to add grade
    public void add_grade(double grade) {
        grades.add(grade);
        System.out.println("Successfully added grade!");
    }

    // Method to calculate average grade
    public double calculate_average_grade() {
        if (grades.isEmpty()) {
            return 0.0;
        } else {
            double sum = 0;
            for (double grade : grades) {
                sum += grade;
            }
            return sum / grades.size();
        }
    }

    // Method to display student details
    public void display_student_details() {
        System.out.println("Name: " + student_name);
        System.out.println("ID: " + student_id);
        System.out.println("Grades: " + grades);
        System.out.println("Average: " + calculate_average_grade());
    }

    // Getter for student name
    public String get_student_name() {
        return student_name;
    }

    // Getter for student ID
    public int get_student_id() {
        return student_id;
    }
}