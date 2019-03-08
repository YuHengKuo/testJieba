from opencc import OpenCC

def translate(): #先將食譜預處理成全繁體
    cc = OpenCC('s2t')
    source = open('iCook.csv', 'r', encoding = 'utf-8')
    result = open('iCook_translated.csv', 'w', encoding = 'utf-8')

    count = 0
    while True:
        line = source.readline()
        line = cc.convert(line)
        if not line:
            break
        print(line)
        count = count +1
        result.write(line)
        print('===已處理'+str(count)+'行===')
    source.close()
    result.close()

translate()