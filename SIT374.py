import re
##Read file

#please change the directory by your self. Thanks. Check this directory in Xcode.
with open('/Users/QiQi/Library/Developer/CoreSimulator/Devices/9A39295F-8ACD-4F18-B0D8-673FF32683C9/data/Containers/Data/Application/EE6CB462-C3BD-4D48-A188-F2A4F4330031/Documents/file.txt', 'r') as f:
    test_input = f.read()

test_output = ""

testing = {
    "intents":
    [
     {"intent":"Location","utterances":["burwood","chadstone","blackburn","boxhill"]},
     {"intent":"Operation: call","utterances":["call","phone"]},
     {"intent":"Operation: go","utterances":["go","navigate","direction","drive"]}
     ]
}

#input_index = 1

to_lower_case = test_input.lower()
#print(to_lower_case)

#clean data
pre_mapper = re.sub("[+\.\!\/_,$%^*)(+\"\']+|[+——！，。？、~@#￥%……&*（）]+"," ",to_lower_case)
print(pre_mapper)

mapper_out = []

mapper_input = pre_mapper.split()
for word in mapper_input:
    #print ("%s\t%s" % (word, 1))
    mapper_out += ["%s %s" % (word, 1)]

#print(mapper_out)

current_word = None
current_count = 0
word = None

key_words = []


for line in mapper_out:
    line = line.strip()
    word, count = line.split(' ', 1)
    try:
        count = int(count)
    except ValueError:  #count
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            #print ("%s\t%s" % (current_word, current_count))
            key_words += ["%s" % (current_word)]
        current_count = count
        current_word = word

if word == current_word:
    #print ("%s\t%s" % (current_word, current_count))
    key_words += ["%s" % (current_word)]

#print(key_words)

for key in testing:
    for keys in testing[key]:
        for test in keys:
            if test == 'utterances':
                for tests in keys[test]:
                    for keyword in key_words:
                        if  keyword == tests.lower():
                            if keys['intent'] == "Operation: call":
                                print("Have %s " %(keys['intent']))
                                test_output += ("Have %s \n" %(keys['intent']))
                            elif keys['intent'] == "Operation: go":
                                print("Have %s " %(keys['intent']))
                                test_output += ("Have %s \n" %(keys['intent']))
                            elif keys['intent'] == "Location":
                                print("Have %s: %s" %(keys['intent'], keyword))
                                test_output += ("Have %s: %s \n" %(keys['intent'], keyword))
                            else :
                                print("Error!") #useless. This line doesn't make any sence.
##Write file
#please change the directory by your self. Thanks
with open('/Users/QiQi/Desktop/test.txt', 'w') as f_o:
    f_o.write(test_output)
