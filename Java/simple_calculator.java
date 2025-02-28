// --- Simple Calculator ---
// Enter first number: 10
// Enter operator (+, -, *, /, %): *
// Enter second number: 3
// Result: 10.0 * 3.0 = 30.0

// Would you like to perform another calculation? (yes/no): yes

// Enter first number: 8
// Enter operator (+, -, *, /, %): /
// Enter second number: 0
// Error: Cannot divide by zero.

// Would you like to perform another calculation? (yes/no): no

// Goodbye!

import java.util.Scanner;

public class simple_calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        boolean repeat = true;

        while (repeat != false) {
            System.out.print("Enter the first number: ");
            double firstNumber = input.nextDouble();
    
            input.nextLine();
            System.out.print("Enter operator (+, -, *, /, %): ");
            String operator = input.nextLine();
    
            System.out.print("Enter the second number: ");
            double secondNumber = input.nextDouble();

            switch (operator) {
                case "+":
                    double add = firstNumber + secondNumber;
                    System.out.println("Result: " + add);
                    break;
                case "-":
                    double subtract = firstNumber - secondNumber;
                    System.out.println("Result: " + subtract);
                    break;
                case "*":
                    double product = firstNumber * secondNumber;
                    System.out.println("Result: " + product);
                    break;
                case "/":
                    double divide = firstNumber / secondNumber;
                    if (firstNumber == 0 || secondNumber == 0) {
                        System.out.println("Error: cannot divide by zero.");
                    } else {
                        System.out.println("Result: " + divide);
                    }
                    break;
                case "%":
                    double mod = firstNumber % secondNumber;
                    System.out.println("Result: " + mod);
                    break;
                default:
                    System.out.println("Please select an operator");
            }
            input.nextLine();
            System.out.print("Do you want to select another option? (yes/no): ");
            String choice = input.nextLine();
            if (choice.equals("no")) {
                repeat = false;
                System.exit(0);
            } else {
                repeat = true;
            }
        }
        input.close();
    }
}