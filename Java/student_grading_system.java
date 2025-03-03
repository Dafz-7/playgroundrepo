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
// Choose an option: 1

// Enter student name: Alice
// Enter student ID: 101
// Student added successfully!

// Choose an option: 2
// Enter student ID: 101
// Enter grade: 95
// Grade added successfully!

// Choose an option: 3
// Enter student ID: 101
// Average Grade for Alice (ID: 101) is: 95.0

// Choose an option: 4
// Students List:
// 1. Alice (ID: 101) - Grades: [95.0]

// Choose an option: 5
// Exiting the program...

// import libraries
import java.util.Scanner;
import java.util.ArrayList;

// two classes: student class and the student system class

// class: student
class Student {
    private String student_name;
    private int student_id;
    private ArrayList<Double> grades;

    // constructor delete this word
    public Student(String student_name, int student_id) {
        this.student_name = student_name;
        this.student_id = student_id;
        this.grades = new ArrayList<>();
    }

    // methods

    // method: add grade
    public void add_grade(double grade) {
        grades.add(grade);
        System.out.println("Successfully added grade!");
    }

    // method: calculate average grade
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

    // method: display student details
    public void display_student_details() {
        System.out.println("Name: " + student_name);
        System.out.println("ID: " + student_id);
        System.out.println("Grades: " + grades);
        System.out.println("Average: " + calculate_average_grade());
    }

    // method: getter for student name
    public String get_student_name() {
        return student_name;
    }

    // method: getter for student id
    public int get_student_id() {
        return student_id;
    }
}

// class: student system
public class student_grading_system {

    // method: helper method to search student by their ID
    private static Student find_student_id(int student_id) {
        for (Student student : students) {
            if (student.get_student_id() == student_id) {
                return student;
            }
        }
        return null;
    }

    private static ArrayList<Student> students = new ArrayList<>();
    
    // running here
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("---Welcome to student grading system---");
            System.out.println("1. Add a new student");
            System.out.println("2. Add grades to a student");
            System.out.println("3. Display a student's average grade");
            System.out.println("4. List all students, their IDs, and their grades");
            System.out.println("5. Exit the system");
            System.out.print("Choose option (1, 2, 3, 4, 5): ");
            int choice = input.nextInt();
            input.nextLine();

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
                        System.out.println("Student not found");
                    }
                    break;
                case 3:
                    System.out.print("Enter student id: ");
                    int student_id_average = input.nextInt();
                    Student student_found_average = find_student_id(student_id_average);
                    if (student_found_average != null) {
                        System.out.println("Student name: " + student_found_average.get_student_name());
                        System.out.println("Student ID: " + student_id_average);
                        System.out.println("Student's average grade: " + student_found_average.calculate_average_grade());
                    } else {
                        System.out.println("Student not found");
                    }
                    break;
                case 4:
                    System.out.println("---Student list---");
                    if (students.isEmpty()) {
                        System.out.println("No students have been added yet");
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
                    System.out.println("Invalid input");
            }
        }
        input.close();
    }
}
