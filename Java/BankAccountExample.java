class BankAccount {
    private double balance;
    private String accountName;

    public BankAccount(double balance, String accountName) {
        this.balance = balance;
        this.accountName = accountName;
    }

    // deposit
    public void deposit(int amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Processed.");
        } else {
            System.out.println("Enter valid value.");
        }
    }

    // withdraw
    public void withdraw(int amount) {
        if (amount < balance) {
            balance -= amount;
            System.out.println("Processed.");
        } else {
            System.out.println("Enter valid value.");
        }
    }

    // balance getter
    public double getBalance() {
        return balance;
    }

    // accountName getter
    public String getAccountName() {
        return accountName;
    }

    // accountName setter
    public void setAccountName(String name) {
        this.accountName = name;
    }
}

public class BankAccountExample {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount(5000, "John");

        // print balance
        System.out.println(account1.getBalance());

        // add balance and print
        account1.deposit(1000);
        System.out.println(account1.getBalance());

        // withdraw and print
        account1.withdraw(4000);
        System.out.println(account1.getBalance());

        // change account name and print
        account1.setAccountName("Budi");
        System.out.println(account1.getAccountName());
    }
}