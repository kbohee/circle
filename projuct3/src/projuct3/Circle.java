package projuct3;

public class Circle implements GeometricObject {
	protected double radius=1.0;
	
	public Circle(double radius) {
		this.radius=radius;
	}
	
	public double getPerimeter() {
		return (radius*2*Math.PI);
	}
	
	public double getArea() {
		return (radius*radius*Math.PI);
	}

	@Override
	public double get_Perimeter() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public double get_Area() {
		// TODO Auto-generated method stub
		return 0;
	}

}