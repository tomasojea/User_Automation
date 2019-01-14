
class palind(object):

        def reverse(self, word):
             return word[::-1]
        def isPalindrome(self,word2):
             return word2 == word2[::-1]

my_palind = palind()
print(my_palind.reverse("123"))
print(my_palind.isPalindrome("anna"))