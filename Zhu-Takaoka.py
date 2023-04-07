def zhu_takaoka(text, word):

    # Metinin ve kelimenin uzunluklarını hesapla
    text_len = len(text)
    word_len = len(word)

    # Matris oluştur
    ztbc = [[word_len for j in range(128)] for i in range(128)]

    # Matristeki boşlukları ve sıfırları doludr
    for i in range(word_len):
        ztbc[ord(word[i])][i] = word_len - i - 1

    # Metin üzernide dolaş
    i = 0

    # Metindeki kelime sayısını sayacak sayaç
    ct = 0

    while i <= text_len - word_len:

        # Kelimenin son karakterinden başlayarak geriye doğru dolaş 
        j = word_len - 1

        while j >= 0 and text[i + j] == word[j]:
            j -= 1

        # Kelime aynıysa sayacı arttır
        if j < 0:
            ct += 1
            i += 1

        # Karakter eşleşmediyse kaydırma adımını belirle
        else:
            i += max(1, j - ztbc[ord(text[i + j])][ord(word[j])])

    return ct

#dosyayı aç oku ve zhu takaoka algoritmasına gönder sonuçları kullanıcıya çıktı ile ver
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
