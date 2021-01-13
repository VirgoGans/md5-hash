#import hashlib first
import hashlib

#while for mass encode
while True :
  
  text = raw_input("Enter text for encode => ")
  
  f = hashlib.md5()
  
  f.update(text)
  
  print "\nmd5 => ",f.hexdigest(),"\n"
  
#Created By Virgo
#Subscribe Virgo Gans
