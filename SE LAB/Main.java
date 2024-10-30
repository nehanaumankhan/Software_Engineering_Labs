// Step 1: Create the Animal Interface
interface Animal {
    void speak();
}

// Step 2: Implement Concrete Classes for Dog and Cat
class Dog implements Animal {
    @Override
    public void speak() {
        System.out.println("Dog says: Woof Woof!");
    }
}

class Cat implements Animal {
    @Override
    public void speak() {
        System.out.println("Cat says: Meow Meow!");
    }
}

// Step 3: Create the AnimalFactory Class
class AnimalFactory {
    public Animal getAnimal(String animalType) {
        if (animalType == null) {
            return null;
        }
        if (animalType.equalsIgnoreCase("Dog")) {
            return new Dog();
        } else if (animalType.equalsIgnoreCase("Cat")) {
            return new Cat();
        }
        return null;
    }
}

// Step 4: Driver code to use the AnimalFactory
public class Main {
    public static void main(String[] args) {
        AnimalFactory animalFactory = new AnimalFactory();

        // Create a Dog and make it speak
        Animal animal1 = animalFactory.getAnimal("Dog");
        if (animal1 != null) {
            animal1.speak();
        }

        // Create a Cat and make it speak
        Animal animal2 = animalFactory.getAnimal("Cat");
        if (animal2 != null) {
            animal2.speak();
        }

        // Trying with an unknown animal
        Animal animal3 = animalFactory.getAnimal("Horse");
        if (animal3 != null) {
            animal3.speak();
        } else {
            System.out.println("Animal type not recognized.");
        }
    }
}
