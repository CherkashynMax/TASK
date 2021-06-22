Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
str = input("Введіть рядок: ")

numb = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
numb = [int(i) for i in numb]

print("\n Рядок без чисел:\n", str)
print("\n Числа з рядка:\n", numb)

str, result = str.title(), ""
for word in str.split():    
      result += word[:-1] + word[-1].upper() + " "
print("\n Кожне слово починається і закінчується великою літерою:")
print( " " + result[:-1])
     

max_numb = max(numb)
print("\n Максимальне число в масиві:", max_numb)


arr_vals = []
for i in range(len(numb)):
    
    if i !=numb.index(max_numb):
        temp = numb[i] 
        stup=temp** i
        arr_vals.insert(i, stup)
print("Масив чисел в степені по їх індексу:\n", arr_vals)