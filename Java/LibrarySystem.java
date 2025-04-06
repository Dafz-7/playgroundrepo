import java.util.ArrayList;
import java.util.Scanner;

public class LibrarySystem {
        // create: library array
        private static ArrayList<Book> library = new ArrayList<>();

    // method: add a new book
    private static void addBook(Scanner input) {
        System.out.print("Enter book title: ");
        String title = input.nextLine();
        System.out.print("Enter author name: ");
        String author = input.nextLine();
        System.out.print("Enter ISBN: ");
        int ISBN = input.nextInt();
        System.out.print("Number of copies: ");
        int copies = input.nextInt();

        library.add(new Book(title, author, ISBN, copies));
        System.out.println("Successfully added book!");
    }

    // method: list all book
    private static void listBooks() {
        if (library.isEmpty()) {
            System.out.println("No books currently added yet");
        } else {
            System.out.println("---Current books---");
            for (Book book : library) {
                book.displayBookInfo();
                System.out.println();
            }
        }
    }

    // method: borrow a book
    private static void borrowBook(Scanner input) {
        System.out.print("Enter book ISBN to borrow: ");
        int ISBN = input.nextInt();

        for (Book book : library) {
            if (book.getISBN() == ISBN) {
                if (book.borrowBook()) {
                    System.out.println("Successfully borrowed book!");
                } else {
                    System.out.println("No copies available to borrow");
                }
                return;
            }
        }
        System.out.println("No book found");
    }

    // method: return book
    private static void returnBook(Scanner input) {
        System.out.println("Enter book ISBN to return: ");
        int ISBN = input.nextInt();

        for (Book book : library) {
            if (book.getISBN() == ISBN) {
                book.returnBook();
                System.out.println("Successfully returned book!");
                return;
            }
        }
        System.out.println("Book not found");
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("---Welcome to Library Management System---");
            System.out.println("1. Add a new book");
            System.out.println("2. List all books");
            System.out.println("3. Borrow a book");
            System.out.println("4. Return a book");
            System.out.println("5. Exit");
            System.out.print("Choose option (1, 2, 3, 4, 5): ");
            int choice = input.nextInt();
            input.nextLine();

            switch (choice) {
                case 1:
                    addBook(input);
                    break;
                case 2:
                    listBooks();
                    break;
                case 3:
                    borrowBook(input);
                    break;
                case 4:
                    returnBook(input);
                    break;
                case 5:
                    System.out.println("Exiting the system...");
                    System.exit(0);
            }
        }
        input.close();
    }
}