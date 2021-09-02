#format()
string_a = "{:d}".format(21)

string_b = "{:5d}".format(21)
string_c = "{:10d}".format(-21)

string_d = "{:05d}".format(21)
string_e = "{:010d}".format(-21)

output_a = "{:+d}".format(30)
output_b = "{:-d}".format(-30)

output_c = "{: d}".format(30)
output_d = "{: d}".format(-30)
output_e = "{:=05d}".format(-2)

output_f = "{:g}".format(52.0)

print(string_a)
print(string_b)
print(string_c)
print(string_d)
print(string_e)

print("============")
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print(output_f)