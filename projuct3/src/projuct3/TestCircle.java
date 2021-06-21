package projuct3;

public class TestCircle {
	public static void main(String[] args) {
		GeometricObject g1=new Circle(1.0);
		System.out.println("Perimeter is "+g1.get_Perimeter());
		System.out.println("Area is "+g1.get_Area());
		
		GeometricObject g2=new Circle(2.0);
		System.out.println("Perimeter is "+g2.get_Perimeter());
		System.out.println("Area is "+g2.get_Area());
		
	}

}
