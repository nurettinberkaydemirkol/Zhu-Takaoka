def zhu_takaoka(text, word):
    text_len = len(text)
    word_len = len(word)

    ztbc = [[word_len for j in range(128)] for i in range(128)]

    for i in range(word_len):
        ztbc[ord(word[i])][i] = word_len - i - 1

    i = 0
    ct = 0

    while i <= text_len - word_len:
        j = word_len - 1

        while j >= 0 and text[i + j] == word[j]:
            j -= 1

        if j < 0:
            ct += 1
            i += 1
        else:
            i += max(1, j - ztbc[ord(text[i + j])][ord(word[j])])

    return ct


with open('alice_in_wonderland.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    count_upon = zhu_takaoka(text, 'upon')
    print("upon: " + str(count_upon))

    count_sight = zhu_takaoka(text, 'sight')
    print("sigh: " + str(count_sight))

    count_Dormouse = zhu_takaoka(text, 'Dormouse')
    print("Dormouse: " + str(count_Dormouse))

    count_jury_box = zhu_takaoka(text, 'jury-box')
    print("jury-box: " + str(count_jury_box))

    count_swim = zhu_takaoka(text, 'swim')
    print("swim: " + str(count_swim))
