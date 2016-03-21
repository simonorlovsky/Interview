import java.util.*;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class PeopleSorter {
    public static void main(String[] args) {
        // If there's no command-line argument, print a usage statement
        // and exit. Otherwise, use args[0] as the input file path.
        if (args.length == 0) {
           System.out.println("Usage java PeopleSorter <people.txt>");
           System.exit(0);
        }

        // Call loadPersonList to build an ArrayList of Person objects
        // from the input file.
        String filePath = args[0];
        ArrayList<Person> personList = loadPersonList(filePath);
        sortPersonList(personList);
        printPersonList(personList);

        // Call sortPersonList

        // Call printPersonList
    }

    public static ArrayList<Person> loadPersonList(String personFilePath) {
        // Use File and Scanner to set up a Scanner for the input file
        File inputFile = new File(personFilePath);

        // Create a Scanner object connected to your file. This is where
        // the JVM tries to actually open the file, and thus this is
        // where an exception can occur. That's why there's a  you need to catch  the
        // exception.
        Scanner scanner = null;
        try {
            scanner = new Scanner(inputFile);
        } catch (FileNotFoundException e) {
            System.err.println(e);
            System.exit(1);
        }

        // Get one line at a time from the file, and print each line in upper
        // case to standard output.
        ArrayList<Person> personList = new ArrayList<Person>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            List<String> personTraits = Arrays.asList(line.split(","));
            Person person = new Person(personTraits.get(1), personTraits.get(0), Integer.parseInt(personTraits.get(2)), Integer.parseInt(personTraits.get(3)), Integer.parseInt(personTraits.get(4)));
            // System.out.println(line.toUpperCase());
            personList.add(person);
        }

        return personList;
    }

    // int n = numArray.length;
    // int temp = 0;
    //
    // for (int i = 0; i < n; i++) {
    //     for (int j = 1; j < (n - i); j++) {
    //
    //         if (numArray[j - 1] > numArray[j]) {
    //             temp = numArray[j - 1];
    //             numArray[j - 1] = numArray[j];
    //             numArray[j] = temp;
    //         }
    //
    //     }
    // }

    public static void sortPersonList(ArrayList<Person> personList) {
      //Sorting by age
        int n = personList.size();
        Person temp;

        for (int i=0; i<n; i++){
          for (int j=1; j<(n); j++){
            if (personList.get(j-1).getAge() > personList.get(j).getAge()){
              temp = personList.get(j-1);
              personList.set(j-1, personList.get(j));
              personList.set(j, temp);
            }
          }
        }
    }

    public static void printPersonList(ArrayList<Person> personList) {
        for (int i=0; i<personList.size(); i++){
          System.out.println(personList.get(i).getFullName()+" "+personList.get(i).getAge());
        }
    }
}
