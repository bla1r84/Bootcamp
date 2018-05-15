package Assignment1;
public class Car {
	private String color;
	private int numberOfDoors;
	private double price;

	public Car(String color, int numberOfDoors, double price) {
		this.color = color;
		this.numberOfDoors = numberOfDoors;
		this.price = price;
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
}