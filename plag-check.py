from difflib import SequenceMatcher

with open("t1.txt") as file1, open("t2.txt") as file2:
  fil1data=file1.read()
  file2data=file2.read()
  similarity=SequenceMatcher(None,fil1data,file2data).ratio()
  print(f"Plagarism between t1 and t2 is: {similarity*100}.")


with open("t3.txt") as file3, open("t4.txt") as file4:
  fi1data=file3.read()
  file4data=file4.read()
  similarity=SequenceMatcher(None,fi1data,file4data).ratio()
  print(f"Plagarism between t3 and t4 is: {similarity*100}.")