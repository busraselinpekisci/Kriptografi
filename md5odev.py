from hashlib import md5

def read_file():
    dosya = input("İçeriği kullanılacak dosya adını giriniz: ")
    with open(dosya, 'r') as f:
        text = f.read()
        return text


def crypt(text):
    return md5(text).hexdigest()


def main():
    list = []
    n = input("Kaç elemanlı rastgelemsi sayı dizisi oluşturmak istersiniz? : ")
    text = read_file()
    for i in range(0, int(n)):
        hash = crypt(text.encode('utf-8'))
        list.append(int(hash[6], 16))
        text = hash

    print("Rastgelemsi sayı diziniz: ", list)


if __name__ == "__main__":
    main()
