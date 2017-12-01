# Name: Lizzie Siegle
# CMSC208 Assignment 5
# Fall 2017

# Example text as a string
mytext = 'NSWs must be classified for phonetic analysis. This is especially important in the case of numbers, which differ in their pronunciation depending on their category. For example, it is necessary to distinguish a year like 1849 from a PIN like 3269. Phone numbers come in variable forms like 234-6529 or 492-499-1349 or (203)893-5938. Zip codes can also vary between 29481 or 49381-2395.'

# Strips periods from sentence-final words 
def remove_punctuation(text):
   return [w[:-1] if w[-1] == '.' else w for w in text]

# Returns true iff string c is a single digit
def is_digit(c):
   return c in '0123456789'

# Returns true iff string w consists of all digits   
def is_string_of_digits(w):
   for c in w:
      if not is_digit(c):
         return False
   return True

# Returns true iff string w is of the form XXXXX or XXXXX-XXXX where X is a digit (incomplete)
def is_zip(w):
   if len(w) == 5 and is_string_of_digits(w):
      return True
   if len(w)==10 and w[5] == '-' and is_string_of_digits(w[0:4]) and is_string_of_digits(w[6:]): 
      return True
   return False
   #[] empty list is False, no zip codes

#234-6529 or 492-499-1349 or (203)893-5938
def is_phone(p):
   #234-6529
   if len(p) == 8 and is_string_of_digits(p[0:2]) and p[3] == '-' and is_string_of_digits(p[4:7]):
      return True
   #492-499-1349
   elif len(p) == 12 and is_string_of_digits(p[0:2]) and p[3] == '-' and is_string_of_digits(p[4:6]) and p[7] =='-' and is_string_of_digits(p[8:]): 
      return True
   #(203)893-5938
   elif len(p) == 13 and p[0] == '(' and is_string_of_digits(p[1:3]) and p[4] == ')' and is_string_of_digits(p[5:7]) and p[8] == '-' and is_string_of_digits(p[9:]):
      return True
   return False

def is_year(y):
   if 


def is_pin(p):
   if


# Suggested approach to distinguishing years from PINs
# Returns true iff string word is found in list wordlist within scan_range positions (left or right) of start_pos 
def scan(wordlist, word, start_pos, scan_range):
   if word in wordlist[:start_pos+scan_range] or word in wordlist[start_pos - scan_range:]:
      return True
   
   return False  # placeholder
  
# Takes a text t as a list of words with sentence-final punctuation removed and returns that text with markup for the following NSW categories: zip codes, phone numbers, years, and PINs.
def NSW_markup(t):
   markedup = []

   i = 0
   while i < len(t):
      if is_zip(t[i]):
         print t[i],'is a zip code!'
         total = '<zip>'+t[i] +'</zip'
         markedup.append(total)   
      elif is_phone(t[i]):     
         print t[i], 'is a phone num!'
         total = '<phone>'+ t[i]+'</phone'
         markedup.append(total)
      elif is_year(t[i]):
         print t[i], 'is a year'
      elif is_pin(t[i]):
      i+=1
      
   return markedup

def demo():
   print NSW_markup(remove_punctuation(mytext.split()))

if __name__ == '__main__':
   demo()




