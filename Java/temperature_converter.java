// 🎯 Challenge: Temperature Converter

// Objective:
// Write a Java program that converts temperatures between Celsius (°C), Fahrenheit (°F), and Kelvin.

// 📋 Requirements:
// 	•	The program should first ask the user to choose the type of conversion:
// 	1.	Celsius to Fahrenheit
// 	2.	Fahrenheit to Celsius
// 	3.	Celsius to Kelvin
// 	4.	Kelvin to Celsius
// 	5.	Exit
// 	•	Prompt the user to enter a temperature value.
// 	•	Convert the temperature according to the selected option.
// 	•	Display the result clearly.
// 	•	Use a loop to allow multiple conversions until the user chooses the Exit option.

import java.util.Scanner;

public class temperature_converter {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean repeat = true;
        while (repeat != false) {
            System.out.println("1. Celsius to Fahrenheit");
            System.out.println("2. Fehrenheit to Celsius");
            System.out.println("3. Celsius to Kelvin");
            System.out.println("4. Kelvin to Celsius");
            System.out.println("5. Exit");
            System.out.print("Choose option (1, 2, 3, 4, 5): ");
            int num = input.nextInt();
            if (num == 5) {
                System.out.println("Proceeding to exit...");
                System.exit(0);
            }
            System.out.print("Enter temperature: ");
            double value = input.nextDouble();
            switch (num) {
                case 1:
                    double updated_value1 = ((9.0/5.0) * value) + 32;
                    System.out.println(value + " Celsius = " + updated_value1 + " Fahrenheit");
                    break;
                case 2:
                    double updated_value2 = ((5.0/9.0) * value) - 32;
                    System.out.println(value + " Fahrenheit = " + updated_value2 + " Celsius");
                    break;
                case 3:
                    double updated_value3 = value + 273.15;
                    System.out.println(value + " Celsius = " + updated_value3 + " Kelvin");
                    break;
                case 4:
                    double updated_value4 = value - 273.15;
                    System.out.println(value + " Kelvin = " + updated_value4 + " Celsius");
                    break;
                default:
                    System.out.println("Please enter valid value");
                    break;
            }
        input.nextLine();
        System.out.println("Select more options? (yes or no)");
        String choice = input.nextLine();
        if (choice.equals("no")) {
            repeat = false;
        }
        }
        input.close();
    }
}