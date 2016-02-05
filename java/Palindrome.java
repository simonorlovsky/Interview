public class Palindrome {
  private static boolean bool = true;

  public static boolean isPalindrome(String s){
    for(int i=0; i<s.length()/2;i++){
      System.out.println(i);
      if (s.charAt(i)!=s.charAt(s.length()-i-1)){
        bool=false;
        System.out.println("Hello World");
      }
    }
    return bool;
  }
  public static void main(String[] args){
    String s = "diid";
    System.out.println(isPalindrome(s));
  }
}
