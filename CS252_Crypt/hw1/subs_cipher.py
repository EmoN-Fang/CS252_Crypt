from collections import Counter

ctext = "JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX"
ind_ctext = ' '.join(ctext)
ctext_list = ind_ctext.split(' ')
new_list = [" "]*(len(ctext_list)-1)
for i in range(len(ctext_list)-1):
    new_list[i] = ctext_list[i]+ ctext_list[i+1]

print("new_list= ",new_list)


freq = Counter(new_list)
print(freq)