public class Book {
    // attributes
    private String title;
    private String author;
    private int ISBN;
    private int copies;

    // constructor
    public Book(String title, String author, int ISBN, int copies) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
        this.copies = copies;
    }

    // getter methods to return private attributes
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getISBN() {
        return ISBN;
    }

    public int getCopies() {
        return copies;
    }

    // method: list all books
    public void displayBookInfo() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("ISBN: " + ISBN);
        System.out.println("Number of copies available: " + copies);
    }

    // method: borrow a book (based on ISBN)
    public boolean borrowBook() {
        if (copies > 0) {
            copies--;
            return true;
        } else {
            return false;
        }
    }

    // method: return a book (based on ISBN)
    public void returnBook() {
        copies++;
    }
}