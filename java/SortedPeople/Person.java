public class Person {
    private String givenName;
    private String familyName;
    private int yearOfBirth;
    private int monthOfBirth;
    private int dayOfBirth;
    private int age;

    public Person(String gName, String fName, int year, int month, int day) {
       // Initialize the instance variables here.
       givenName = gName;
       familyName = fName;
       yearOfBirth = year;
       monthOfBirth = month;
       dayOfBirth = day;
       age = 2016 - year;
    }

    public int getAge() {
       return 2016 - yearOfBirth;
    }

    public String getFullName() {
       return givenName + " " + familyName;
    }

    public void setAge(int newAge) {
        age = newAge;
    }
}
