a = "hello world, my name is python"
print(a.upper()) #모든 소문자를 대문자로 변경

b = "LOST ARK"
print(b.lower()) #모든 대문자를 소문자로 변경

a1 = """
hello guys haha
"""

print("------")
print(a1)
print("------")
print(a1.strip()) #앞뒤 공백 제거

print("안녕" in "안녕하세요") #앞의 문자열이 뒤에 포함이 되어있나 검사

ex = "10 20 30 40 50 70 9 0".split()
print(ex)