# Zhu-Takaoka
 Boyer-Moore algoritmasının bir türevidir. Karşılaştırma işlemi sağdan sola doğru gerçekleştirilir. Boyer-Moore algoritmasındaki kötü karakter kaydırmasını hesaplamak için ardıl metin karakterlerini kullanır. İyi sonek önişlem safhası ise Boyer-Moore algoritmasındaki ile aynıdır. Kaydırma işlemini gerçekleştirirken bu iki kural arasındaki maksimum değerini seçerek kaydırma yapar.
 
 Zhu-Takaoka algoritması, grafın kenarlarını ağırlık değerlerine göre sıralar ve birbirine bağlayan düğümleri birbirine bağlamadan önce aynı ağaca bağlamayı tercih eder. Algoritma, her bir düğümün ait olduğu ağacı tutar ve yeni bir düğümü eklediğinde, bu düğümü ekleyerek ağaçları birleştirir. Bu şekilde, her zaman en küçük ağaçlar elde edilir.

## EN İYİ DURUM

En iyi durumda, algoritmanın çalışma zamanı, grafın ayrılmış olması durumunda O(ElogE) olacaktır.

## ORTALAMA DURUM

Ortalama durumda, algoritmanın çalışma zamanı, bir grafa ağırlıkların rastgele atanması durumunda O(ElogE) olacaktır.

##EN KOTU DURUM

En kötü durumda, algoritmanın çalışma zamanı, grafın tüm düğümleri arasında kenarların ağırlığı eşit olarak dağıldığı durumlarda, yani ağırlıklı tam bir grafsa O(E^2logE) olacaktır.

 
 
