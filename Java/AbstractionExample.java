// class: abstract Vehicle
abstract class Vehicle {
    // method: abstract start()
    abstract void start();

    // method: stop()
    void stop() {
        System.out.println("Engine is stopping...");
    }
}

// class: Car extends from Vehicle
class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Engine starts...");
    }
}

public class AbstractionExample {
    public static void main (String[] args) {
        Vehicle car1 = new Car();
        car1.start();
        car1.stop();
    }
}