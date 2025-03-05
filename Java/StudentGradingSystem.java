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

import java.util.Scanner;
import java.util.ArrayList;

public class StudentGradingSystem {

    private static ArrayList<Student> students = new ArrayList<>();

    // Helper method to search for a student by ID
    private static Student find_student_id(int student_id) {
        for (Student student : students) {
            if (student.get_student_id() == student_id) {
                return student;
            }
        }
        return null;
    }

    // Main method (Runs the program)
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("---Welcome to Student Grading System---");
            System.out.println("1. Add a new student");
            System.out.println("2. Add grades to a student");
            System.out.println("3. Display a student's average grade");
            System.out.println("4. List all students, their IDs, and their grades");
            System.out.println("5. Exit the system");
            System.out.print("Choose option (1, 2, 3, 4, 5): ");
            int choice = input.nextInt();
            input.nextLine();  // Consume the newline

            switch (choice) {
                case 1: 
                    System.out.print("Enter student name: ");
                    String student_name = input.nextLine();
                    System.out.print("Enter student ID: ");
                    int student_id = input.nextInt();
                    students.add(new Student(student_name, student_id));
                    System.out.println("Successfully added new student!");
                    break;
                case 2:
                    System.out.print("Enter student ID: ");
                    int search_student_id = input.nextInt();
                    Student student_found = find_student_id(search_student_id);
                    if (student_found != null) {
                        System.out.print("Enter grade: ");
                        double grade = input.nextDouble();
                        student_found.add_grade(grade);
                    } else {
                        System.out.println("Student not found.");
                    }
                    break;
                case 3:
                    System.out.print("Enter student ID: ");
                    int student_id_average = input.nextInt();
                    Student student_found_average = find_student_id(student_id_average);
                    if (student_found_average != null) {
                        System.out.println("Student name: " + student_found_average.get_student_name());
                        System.out.println("Student ID: " + student_id_average);
                        System.out.println("Student's average grade: " + student_found_average.calculate_average_grade());
                    } else {
                        System.out.println("Student not found.");
                    }
                    break;
                case 4:
                    System.out.println("--- Student List ---");
                    if (students.isEmpty()) {
                        System.out.println("No students have been added yet.");
                    } else {
                        for (Student student : students) {
                            student.display_student_details();
                        }
                    }
                    break;
                case 5:
                    System.out.println("Exiting the system...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid input. Please try again.");
            }
        }
        input.close();
    }
}