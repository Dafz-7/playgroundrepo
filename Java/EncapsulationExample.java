// class: bank account
class bankaccount {
    // attributes: balance
    private double balance;

    // constructor
    public bankaccount(double balance) {
        this.balance = balance;
    }

    // getter method to return balance
    public double getBalance() {
        return balance;
    }

    // method: deposit
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Balance updated!");
        } else {
            System.out.println("Invalid deposit amount");
        }
    }
}

// main class
public class EncapsulationExample {
    // running here
    public static void main(String[] args) {
        bankaccount account1 = new bankaccount(1000);

        System.out.println("Account balance: $" + account1.getBalance());

        double depositedAmount = 3000;
        account1.deposit(depositedAmount);
        System.out.println("Deposited $" + depositedAmount);

        System.out.println("Account balance: $" + account1.getBalance());
    }
}