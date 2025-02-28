// Enter account holder's name: Dafz
// Enter initial deposit amount: 200

// Account created successfully!

// --- BANK MENU ---
// 1. Deposit
// 2. Withdraw
// 3. Check Balance
// 4. Exit
// Choose an option: 1
// Enter deposit amount: 50
// Deposited $50.0.

import java.util.Scanner;

// class
public class bank_account_system {
    // attributes
    private String account_holder;
    private double account_balance;

    // constructor
    public bank_account_system(String account_holder, double account_balance) {
        this.account_holder = account_holder;
        this.account_balance = account_balance;
    }

    // methods

    // method: deposit
    public void deposit(double amount) {
        if (amount > 0) {
            account_balance += amount;
            System.out.println("Successfully deposited!");
        } else if (amount <= 0) {
            System.out.println("Amount cannot be zero or less than zero");
        } else {
            System.out.println("Invalid value");
        }
    }

    // method: withdraw
    public void withdraw(double amount) {
        if (amount <= account_balance) {
            account_balance -= amount;
            System.out.println("Successfully withdrawed!");
        } else if (amount > account_balance) {
            System.out.println("Value exceeded your current account_balance");
        } else {
            System.out.println("Invalid value");
        }
    }

    // method: check account_balance
    public void check_account_balance() {
        System.out.println("Account holder: " + account_holder);
        System.out.println("Currect account_balance: " + account_balance);
    }

    // running here
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("--Welcome to bank account system--");
        System.out.println("To start, please create an account:");
        System.out.print("Enter account name: ");
        String name = input.nextLine();
        System.out.print("Enter initial account balance: ");
        double balance = input.nextDouble();

        bank_account_system user_bank_account = new bank_account_system(name, balance);
        System.out.println("Bank account created successfully!");

        boolean running = true;

        while (running) {
            System.out.println("---Bank menu---");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check balance");
            System.out.println("4. Exit");
            System.out.print("Your option: ");
            int choice2 = input.nextInt();
            switch (choice2) {
                case 1:
                    System.out.print("Enter deposit amount: $ ");
                    double deposit_amount = input.nextDouble();
                    user_bank_account.deposit(deposit_amount);
                    break;
                case 2:
                    System.out.print("Enter withdraw amount: $ ");
                    double withdraw_amount = input.nextDouble();
                    user_bank_account.withdraw(withdraw_amount);
                    break;
                case 3:
                    user_bank_account.check_account_balance();
                    break;
                case 4:
                    System.out.println("Exiting the program...");
                    System.exit(0);
                default:
                    System.out.println("Invalid input");
            }

            input.nextLine();
            System.out.print("Make more changes to your account? (yes/no): ");
            String choice3 = input.nextLine();
            if (choice3.equals("yes")) {
                running = true;
            } else if (choice3.equals("no")) {
                running = false;
                System.out.println("Exiting the program...");
            } else {
                System.out.println("Invalid input");
            }
        }

        input.close();
    }
}