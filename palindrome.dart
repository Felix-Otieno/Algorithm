bool isPalindrome(String string) {
  int left = 0;
  int right = string.length - 1;

  while (left < right) {
    if (string[left] != string[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
}

void main() {
  print(isPalindrome("radar")); // Output: true
}
