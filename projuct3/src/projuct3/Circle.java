package projuct3;

public class Circle implements GeometricObject {
	protected double radius=1.0;
	
	public Circle(double radius) {
		this.radius=radius;
	}
	
	public double get_Perimeter() {
		return radius*2*Math.PI;
	}
	
	public double get_Area() {
		return radius*radius*Math.PI;
	}


}