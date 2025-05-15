class Print {
	private String print;
	
	Print(String print) {
		this.print = print;
	}
	
	static void printAMessage() {
		System.out.println("Printing the message.");
	}
	
	static String printTheMessage(String print) {
		System.out.println(print);
		return print;
	}
}

public class testings {
	public static void main(String[] args) {
		Print obj1 = new Print("obj1");
		
		obj1.printAMessage(); 
		obj1.printTheMessage("Jonggol");
	}
}