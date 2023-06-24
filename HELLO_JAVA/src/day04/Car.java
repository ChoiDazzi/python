package day04;

public class Car extends  Vehicle{
	int autoPilotLevel = 1;
	
	public void hit() {
		autoPilotLevel++;
	}
}
