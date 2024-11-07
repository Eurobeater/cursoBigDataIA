import robocode.Robot;
import robocode.ScannedRobotEvent;
import robocode.HitByBulletEvent;

public class Robot_Eurobeater extends Robot {
    @Override
    public void run() {
        while (true) {
            ahead(100);
            turnRight(90);
        }
    }

    @Override
    public void onScannedRobot(ScannedRobotEvent event) {
        fire(2);
    }
    
    @Override
    public void onHitByBullet(HitByBulletEvent event) {
        turnRight(90);
        ahead(100);
    }
}
