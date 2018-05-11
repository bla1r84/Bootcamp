package Assignment2;
import java.util.Scanner;

public class CarTest {
	
	public static Scanner input = new Scanner (System.in);

	public static void main(String[] args) {
		/* create Cars */
		Car car1 = new Car (); // per
		
		boolean[] mystatus = {false,false,false,false,false};
		Car car2 = new Car ("red", 3, 12000.10, mystatus );

		/* print cars*/
		System.out.println(car1);
		System.out.println(car2);
		System.out.println(car2.getDoorsStatus()[0]);
		car1.setPrice(10000);// change car's price
		System.out.println(car1);//print to see the change
		
		Scanner input = new Scanner (System.in);
		boolean myBoolean = true;
		do {
			System.out.println("\nWhat do you want to do? \n1.Open Door \n2.Close Door \n3.Reverse status of the door \n4.Print specified door status \n5.Quit");
			int choice = input.nextInt();
			if (choice == 1) {
				car2.displayMenu();
				car2.openDoor();				
			}else if (choice == 2) {
				car2.displayMenu();
				car2.closeDoor();
			}else if (choice == 3) {
				car2.openCloseDoor();
			}else if (choice == 4) {
				car2.inspectDoors();
			}else if (choice == 5) {
				System.out.println("Finish of door open/close state. Goodbye.");
				myBoolean = false;
			}
		} while (myBoolean==true);
	input.close();
	}
}