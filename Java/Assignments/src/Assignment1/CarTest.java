package Assignment1;
public class CarTest {

	public static void main(String[] args) {
		/* create Cars */
		Car car1 = new Car ();
		Car car2 = new Car("red", 3, 12000.10);

		/* print cars*/
		System.out.println(car1);
		System.out.println(car2);

		car1.setPrice(10000);// change car's price
		System.out.println(car1);//print to see the change

	}

}