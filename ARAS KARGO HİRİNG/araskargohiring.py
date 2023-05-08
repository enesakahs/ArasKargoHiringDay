import math
import os
import random
import re
import sys


class Message(object):
    def __init__(self, message: str, sender: int, receiver: int) -> None:
        self.message = message
        self.sender = sender
        self.receiver = receiver

    def __str__(self) -> str:
        return self.message
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Message):
            return self.message == __o.message
        return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_message = int(input())
    messages = [None]*num_message
    for i in range(num_message):
        *message, sender, receiver = input().split()
        message = " ".join(message)
        sender, receiver = map(int, [sender, receiver])
        messages[i] = Message(message, sender, receiver)

    result = ""
    num_queries = int(input())
    for i in range(num_queries):
        instruction, *ids =  input().split()
        if instruction == 'print':
            id = int(ids[0])
            result += f"{messages[id]}\n"
        elif instruction == 'eq':
            id1, id2 = map(int, ids)
            result += f"{messages[id1] == messages[id2]}\n"
    fptr.write(result + '\n')

    fptr.close()

# Bu kodlar, kullanıcıdan alınan mesajları ve mesajlara ait gönderici ve alıcı bilgilerini bir sınıf ile temsil ederek, birbirleriyle karşılaştırmak veya belirli bir mesajı yazdırmak için kullanıcının yapacağı sorgulara yanıt veriyor.

# Kodların ayrıntılı açıklamaları şöyle:
# Message adında bir sınıf tanımlanıyor. Bu sınıf, mesajları, mesajların göndericilerini ve alıcılarını temsil etmek için kullanılıyor.

# __init__ fonksiyonu, mesaj sınıfının özelliklerini tanımlıyor. message, sender ve receiver adında üç adet özellik alıyor ve bu özellikler, sınıfın örneklerine atanıyor.

# __str__ fonksiyonu, bir mesajın yazdırılması gerektiğinde, mesaj metnini döndürüyor.

# __eq__ fonksiyonu, iki mesajın eşitliğini kontrol ediyor. İki mesajın eşit olduğu durumda True değerini, eşit olmadığı durumda False değerini döndürüyor.

# num_message adında bir değişkene, kullanıcıdan alınacak mesaj sayısı atanıyor.

# messages adında bir dizi tanımlanıyor ve boyutu num_message olarak belirleniyor. Bu dizi, kullanıcının girdiği mesajların depolanması için kullanılıyor.
# for döngüsü içinde, kullanıcıdan mesajlar ve gönderici/alıcı bilgileri alınıyor. Mesajlar, önce *message ile bir liste olarak alınıyor ve daha sonra join fonksiyonu ile birleştirilerek message adlı bir dizeye dönüştürülüyor. 
# sender ve receiver değişkenleri, kullanıcının girdiği sayısal verilerden oluşan bir listeyi map fonksiyonu yardımıyla int olarak dönüştürerek alınıyor. 
# Son olarak, Message sınıfının bir örneği oluşturuluyor ve bu örnek messages dizisine atanıyor.   

# result adında boş bir dize tanımlanıyor. Bu değişken, kullanıcının yapacağı sorgulara verilecek yanıtları depolamak için kullanılacak.
# num_queries adında bir değişkene, kullanıcının yapacağı sorgu sayısı atanıyor.

# for döngüsü içinde, kullanıcının yapacağı sorgular alınıyor. Eğer sorgu print ise, ids adlı değişkenden alınan indekse sahip mesajın yazdırılması gerekiyor. 
# Bu durumda, id adlı bir değişkene indeks atanıyor ve result değişkenine, f-string yapısı kullandığı bir string ifadesi ekleniyor. Eğer sorgu eq ise, ids adlı değişkenden alınan indekslere sahip iki mesajın eşitliği kontrol ediliyor 
# ve sonuç result değişkenine f-string kullanarak ekleniyor. Son olarak, result değişkeni yazdırılıyor.