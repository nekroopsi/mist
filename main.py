meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH":  "onaylamamak",
            "CREEPY":  "korkunç",
            "AGGRO":  "agresifleşmek/sinirlenmek",
            }
            
word = input("Anlamadığınız bir kelime yaz bacım (hepsini büyük harflerle yazıyorsun hata almıyorsun bacım!): ")

if word in meme_dict.keys():
    print("Kelimenin anlamı:" ,meme_dict[word])
else:
    print("bu kelime yok bacım")
