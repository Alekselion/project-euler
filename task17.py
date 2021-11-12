task = "If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?"
num = {
    1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
    13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
    20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
    100:'hundred', 1000:'thousand'
}

to19, to99, to999, result = 0, 0, 0, 0
keys = [k for k in num.keys()]
for x in keys:
    if x < 100:
        result += len(num[x])
        if 20 <= x < 100:
            for y in keys:
                result += len(num[x]) + len(num[y])
                if y == 9:
                    break
                else:
                    to19 = result  # from 1 to 19
            to99 = result  # from 1 to 99
    elif x == 100:
        # 100, 200, 300, ...,  900
        for i in keys:
            if i == 10: break
            result += len(num[i]) + len(num[100])
            result += (len(num[i]) + len(num[100]) + len('and')) * 99 + to99  # from 1 to 999
        to999 = result
    else:  # x == 1000
        result += len(num[1]) + len(num[1000])

print(f"Task: {task}\nAnswer: {result}")