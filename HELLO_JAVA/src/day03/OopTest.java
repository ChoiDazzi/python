package day03;

public class OopTest {
	public static void main(String[] args) {
		Human h = new Human();
		System.out.println(h.flagSound);
		System.out.println(h.communitySkill);
		h.die();
		h.study(5);
		System.out.println(h.flagSound);
		System.out.println(h.communitySkill);
	}
}
