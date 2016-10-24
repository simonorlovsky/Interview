function palindrome(str) {
  // Good luck!

  newStr = str.replace(/\W/g, '')
  console.log(newStr)
  newStr = newStr.toLowerCase();

  var isPalindrome = true;
  console.log(newStr.length);
  for (i=0; i<newStr.length; i++){
    console.log(newStr.charAt(newStr.length - i - 1))
    if (newStr.charAt(i) != newStr.charAt(newStr.length - i - 1)){
      isPalindrome = false;
    }
  }
  return isPalindrome;
}

console.log(palindrome("eye#"));
