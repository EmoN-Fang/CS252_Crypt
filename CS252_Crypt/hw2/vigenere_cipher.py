from collections import Counter

ctext = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE"
ind_ctext = ' '.join(ctext)
ctext_list = ind_ctext.split(' ')
# new_list = [""]*(len(ctext_list)-2)
# for i in range(len(ctext_list)-2):
#     new_list[i] += ctext_list[i]+ ctext_list[i+1] + ctext_list[i+2]
#     if new_list[i] == "CHR":
#         print("i=",i)
# print("new_list= ", new_list)


# freq = Counter(new_list)
# print(freq)

new_list_0 = [" "]*(len(ctext_list)//5 + 1)
new_list_1 = [" "]*(len(ctext_list)//5 + 1)
new_list_2 = [" "]*(len(ctext_list)//5 + 1)
new_list_3 = [" "]*(len(ctext_list)//5 + 1)
new_list_4 = [" "]*(len(ctext_list)//5 + 1)
j = 0

for i in range(len(ctext_list)):
    if i % 5 == 0:
        new_list_0[j] = ctext_list[i]
    elif i % 5 == 1:
        new_list_1[j] = ctext_list[i]
    elif i % 5 == 2:
        new_list_2[j] = ctext_list[i]
    elif i % 5 == 3:
        new_list_3[j] = ctext_list[i]
    elif i % 5 == 4:
        new_list_4[j] = ctext_list[i]
        j += 1

print(new_list_0)


freq = Counter(new_list_0)
print(freq)