'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
import random
import time

def buat_soal():
    """AI membuat soal acak dari Matematika, IPA, IPS, Bahasa."""
    kategori = random.choice(["matematika","ipa","ips","bahasa","logika"]) 

    if kategori == "matematika":
        soal = [
            ("apa itu gradien ?","kemiringan"),
            ("bilangan yang bisa jadi pecahan (a/b)?","rasional"),
            ("berapa akar pangkat dari 64","8"), 
            ("variabel sebelum (y)","x"), 
            ("berapakah 100-47","53"), 
            ("berapa akar kuadrat dari 81","9"), 
            ("nilai dari 6 kuadrat adalah","36"), 
            ("berapa 50% dari 200","100"), 
            ("berapakah 7 × 8","56"), 
            ("berapa hasil 15 + 27","42"), 
            ("berapa hasil dari 3x -5 = 10","5"),
            ("bentuk sederhana dari akar 49","7"),
            ("nilai dari 3 pangkat 2 adalah?","9"),
        ]
        return random.choice(soal)
        
    elif kategori == "ipa":
        soal = [
            ("Apa satuan untuk kuat arus listrik?","ampere"), 
            ("Planet terbesar di tata surya?","jupiter"),
            ("apa zat yang tidak bisa dibagi lagi secara kimia","unsur"), 
            ("proses pengubahan air menjadi uap disebut","evaporasi"),
            ("satuan dasar gaya dalam SI","newton"), 
            ("planet yang dikenal sebagai (planet merah) adalah","mars"), 
            ("kata virus berasal dari bahasa Latin yang artinya?","racun"), 
            ("berapa kedalaman zona fotik?","200 meter"), 
            ("ekosistem air tawar tenang disebut?","lentik"), 
            ("unit dasar kehidupan yang menyusul semua mahluk hidup","sel"), 
            ("fungi adalah?","jamur"), 
        ]
        return random.choice(soal)

    elif kategori == "ips":
        soal = [
            ("Apa ibu kota provinsi Jawa Timur?","surabaya"),
            ("Gunung apa yang meletus tahun 2010?","merapi"),
            ("nilai 2 pangkat 6 adalah? ","168"), 
            ("kegiatan menjual barang ke luar negeri disebut?","ekspor"), 
            ("kegiatan menghasilkan barang disebut?","produksi"), 
            ("persaingan untuk mendapat pengaruh politik disebut?","konflik"), 
            ("perubahan sosial yang terjadi secara cepat disebut","revolusi"), 
            ("perpindahan penduduk secara permanen disebut?","migrasi"), 
            ("proses terjadinya siang dan malah karena rotasi...?","bumi"), 
            ("perubahan sosial yang berjalan lambat disebut?","evolusi"),
            ("ibu kota indonesia saat ini?","jakarta"),
            ("ibu kota jawa barat","bandung"),
            ("mata uang Amerika adalah?","dolar"),
            ("pulau dengan penduduk terbanyak di Indonesia adalah","jawa"),
        ]
        return random.choice(soal)
        semua_soal.remove(soal)

    elif kategori == "bahasa":
        soal = [
            ("Apa sinonim dari kata 'indah'?","cantik"),
            ("Apa lawan kata 'panas'?","dingin"),
            ("Antonim dari kata “maju” adalah…","mundur"), 
            ("gagasan utama di sebuah paragraf disebut?","ide pokok"), 
            ("kalimat yang berisi pendapat disebut?","opini"), 
            ("kata yang memiliki makna yang mirip disebut?","sinonim"), 
            ("kata yang berlawanan makna disebut?","antonim"), 
            ("teks yang bertujuan menghibur pembaca disebut?","anekdot"), 
            ("kata yang digunakan untuk menghubungkan kalimat disebut?","konjungsi"), 
            ("tokoh yang mengalami masalah utama dalam cerita disebut?","protagonis"), 
            
        ]
        return random.choice(soal)
        semua_soal.remove(soal)

    elif kategori == "logika" :
        soal = [
            ("aku  adalah barang yang sangat dibutuhkan manusia","uang"), 
            ("aku adalah sesuatu yang tidak pernah mau kalah","ego"), 
            ("aku adalah  hal yang tidak pernah dimiliki manusia","keabadian"), 
            ("manusia sangat bergantung padaku, apakah aku? ","oksigen"), 
            ("aku adalah sesuatu yang  ingin manusia ketahui atau jelajahi! ","alam semesta"), 
            ("aku adalah sesuatu yang sering disepelekan oleh manusia","tanggung jawab"), 
            ("aku adalah benang yang mengikat manusia","takdir") , 
            ("aku adalah sesuatu yang  tidur saat siang hari,apakah aku? ","kelelawar"), 
            ("aku adalah sesuatu yang berhaga","waktu"),
            ("aku adalah sesuatu yang  selalu dicari manusia","harta"),
            ("apa hal yang selalu naik tapi tidak bisa turun","umur"), 
            ("aku selalu bertumbuh panjang, tapi aku akan berubah warna seiring bertambahnya waktu, apakah aku?","rambut")
        ]
        return random.choice(soal)
    

def game_teacher_battle() :
    print("\n===== ⚡ TEACHER BATTLE AI ⚡ =====")
    print("Jawab secepat mungkin! Kamu punya 20 detik untuk tiap soal.\n")
    skor = 0

    while True:
        print("\n=== SOAL BARU ===")
        soal,jawaban_benar=buat_soal()
        print(f"Soal AI: {soal}")

        start = time.time()
        try:
            jawab = input("Jawabanmu: ").lower().strip()
        except:
            jawab = ""

        waktu = time.time() - start

        if waktu > 20 :
            print("⏳ Terlambat! Kamu kehabisan waktu!")
            break

        if jawab == jawaban_benar:
            print("✅ Benar! +10 poin\n")
            skor += 5
        else:
            print(f"❌ Salah! Jawaban benar: {jawaban_benar}")
            break

    print(f"\n🏁 Game selesai! Skor akhir kamu: {skor}")

game_teacher_battle()