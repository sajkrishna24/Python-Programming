def character_freq(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
test_string="programming"
result=character_freq(test_string)
print("character frequency dictionary")
print(result)