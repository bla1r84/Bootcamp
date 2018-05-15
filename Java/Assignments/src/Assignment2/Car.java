package Assignment2;
public class Car {
	private String color;
	private int numberOfDoors;
	private double price;

	private boolean[] doorsStatus = new boolean[5];
	private String [] doorstate = {"Front left", "Front right", "Back left", "Back right", "Trunk"};

	public Car (String color, int numberOfDoors, double price, boolean[] doorsStatus) {
		this.color = color;
		this.numberOfDoors = numberOfDoors;
		this.price = price;
		this.doorsStatus = doorsStatus;
	}

	public Car() {
		this.color = "white";
		this.numberOfDoors = 5;
		this.price = 5000.0;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public int getNumberOfDoors() {
		return numberOfDoors;
	}

	public void setNumberOfDoors(int numberOfDoors) {
		this.numberOfDoors = numberOfDoors;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	@Override
	public String toString() {
		return "Car [color=" + color + ", numberOfDoors=" + numberOfDoors + ", price=" + price + "]";
	}

	//Door methods
	public boolean[] getDoorsStatus() {
		return doorsStatus;
	}

	public void setDoorsStatus(boolean[] doorsStatus) {
		this.doorsStatus = doorsStatus;
	}

	public void openDoor() {
		int choice1 = CarTest.input.nextInt();
		this.doorsStatus[choice1-1]=true;
	}

	public void closeDoor() {
		int choice1 = CarTest.input.nextInt();
		this.doorsStatus[choice1-1]=false;
	}

	public void openCloseDoor() {
		for (int i=0;i<doorsStatus.length;i++) {
			if (this.doorsStatus[i]==true) {
				this.doorsStatus[i]=false;
			}else {
				this.doorsStatus[i]=true;
			}
		}
	}

	public void inspectDoors() {
		System.out.println("\nWhat do you want to view? \n1.Open Doors \n2.Close Doors \n3.All Doors");
		int choice1 = CarTest.input.nextInt();
		if (choice1 == 1) {
			for (int i=0;i<doorsStatus.length;i++) {
				if (this.doorsStatus[i]==true) {
					System.out.println("Open door: " + this.doorstate[i]);
				}
			}
		}else if (choice1 == 2) {
			for (int i=0;i<doorsStatus.length;i++) {
				if (this.doorsStatus[i]==false) {
					System.out.println("Close door: " + this.doorstate[i]);
				}

			}
		}else if (choice1 == 3){
			for (int i=0;i<doorsStatus.length;i++) {
				if (this.doorsStatus[i]==true) {
					System.out.println("Open door: " + this.doorstate[i]);
				}else {
					System.out.println("Close door: " + this.doorstate[i]);
				}

			}
		}

	}


	public void displayMenu() {
		System.out.println("Pick a door: \n1.Front Left \n2.Front right \n3.Back left \n4.Back right \n5.Trunk");
	}

}