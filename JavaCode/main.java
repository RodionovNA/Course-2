/*
Необходимо будет реализовать последовательную 
иерархию из 3 классов (абстрактные классы не 
учитываются), 
учитывая все рассказанное на 1 паре и завтра. 
Каждый не менее 3 собственных атрибутов и 5 
собственных методов)
Выбор тематики зависит лишь от полета Вашей 
фантазии. Соблюдение code-style, разумеется, 
обязательно 
*/


class Monkey {
    /*
     Класс реализует сущность обезьяны
     */
    static int POPULATION = 0;
    int number;
    String country;
    int width;
    int height;

    public Monkey(int number, String country, int width, int height) {
        this.number = number;
        this.country = country;
        this.width = width;
        this.height = height;
        POPULATION += 1;
        System.out.println("Monkey is create.");
    }
    public void print_number() {
        /*
         * Печатает номер
         */
        System.out.println(number);
    }
    public void print_POPULATION() {
        /*
         * Печатает численность популяции обезьян
         */
        System.out.println(POPULATION);
    }
    public void print_info(){
        /*
         * Печатает общую информацию
         */
        System.err.println("Width: " + width + " Height: " + height);
    }
    public void print_country() {
        /*
         * Печатает страну откуда обезяна родом
         */
        System.out.println(country);
    }
}


class Homosapience extends Monkey {
    /*
     * Класс расширяет класс обезьяны и представляет сущность древнего человека
     */
    String species; // вид
    int era;
    String peculiarities; // особенности
    boolean is_live_now;
    static int POPULATION_HOMOSAPIENCE = 0;

    public Homosapience(int number, String country, int width, int height,
    String species, int era, String peculiarities, boolean is_live_now) {
        super(number, country, width, height);
        this.species = species;
        this.era = era;
        this.peculiarities = peculiarities;
        this.is_live_now = is_live_now;
        POPULATION_HOMOSAPIENCE += 1;
    }

    public String get_peculiarities(){
        /*
         * Возвращает особенности конкретной особи древнего человека
         */
        return peculiarities;
    }
    public void edit_era(int new_era) {
        /*
         * Позволяет корректировать эру существования особи древнего человека
         */
        this.era = new_era;
    }
    
    @Override
    public void print_info() {
        System.err.println("Population: " + POPULATION_HOMOSAPIENCE + " Species: " + species + 
        " era: " + era);
    }

    public void check_live() {
        /*
         * Проверяет жива ли особь на момент внесения данных в систему
         */
        if (is_live_now == true) {
            System.err.println("is live");
        }
        else {
            System.err.println("is not live");
        }
    }
    
}


class Homosapiencesapience extends Homosapience {
    /*
     * Класс расширяет функционал древнего человека и описывает сущность современного человека
     */
    String fname;
    String lname;
    int age;
    String status;
    boolean is_married;

    public Homosapiencesapience(int number, String country, int width, int height,
    String species, int era, String peculiarities, boolean is_live_now,
    String fname, String lname, int age, String status, boolean married) {
        super(number, country, width, height, species, era, peculiarities, is_live_now);
        this.fname = fname;
        this.lname = lname;
        this.age = age;
        this.status = status;
        this.is_married = married;
    }

    public String lets_married() {
        /*
         * Меняет состояние флага is_married на true
         */
        this.is_married = true;
        return "You are married";
    }
    public void print_status() {
        /*
         * Печатает статус человека в обществе
         */
        System.err.println(status);
    }
    public void happy_birthday() {
        /*
         * Прибавляет к возрасту единицу, день рождения человека
         */
        this.age += 1;
    }

    @Override
    public void print_info() {
        System.err.println("Name: " + fname + " Lname: " + lname + " Age: " + age + " Is married ? " + is_married);
    }
}

public class main {

    public static void main(String[] args) {
        System.out.println("Hello world!");
        System.out.println("Bye world...");
        Monkey mk = new Monkey(23, "Russia", 10, 24);
        mk.print_country();
        Homosapience hmk = new Homosapience(11, "Columbia", 160, 55, "Soplec", 5, "Has a blue eye", false);
        hmk.check_live();

        Homosapiencesapience hss = new Homosapiencesapience(15, "Russia", 50, 177, "European", 1, "Stury in university", true, "Nikita", "Rodionov", 22, "Student", false);
        hss.happy_birthday();
        hss.print_info();
    }
}





