package day03;

public class Human extends Animal{
	int communitySkill = 0;
	
	public void study(int hour) {
		communitySkill += hour;
	}
}
