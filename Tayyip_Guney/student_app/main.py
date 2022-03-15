'''
Bir ogrenci Class i yazin ve While dongusunde kullandigimiz methodlarin icerinde 
bu ogrenci sinifini kullanarak yine ayni islemleri yapalim. Fakat bu sefer 
ogrenci sinifinin objeleri uzerinden.
'''

class Student:
    sonuclar = []
    def __init__(self,sec) -> None:
        self.sec = sec
        
    def secim(self):
        Islem_secim ={
     "1":self.notgir,
     "2":self.nothesapla,
     "3":self.notkaydet,
     "4":self.cikis,
     "5":self.del_all
}
        return Islem_secim[self.sec]    
    
    def notgir(self):
        self.ogrenci_adi,self.ogrenci_soyadi = input("Ogrenci Adini Giriniz: "),input("Ogrenci Soyadini Giriniz:")
        self.vize1,self.vize2,self.final = input("Vize1: " ), input("vize2: "),input("Final: ")
        virgul=","
        text = self.ogrenci_adi+virgul+self.ogrenci_soyadi+virgul+self.vize1+virgul+self.vize2+virgul+self.final+"\n"
        print("\n")
        with open("W_7\\Tayyip_Guney\\student_app\\notlar.txt","a") as file:
            file.write(text)  
            
    def nothesapla(self):
   
        with open("W_7\\Tayyip_Guney\\student_app\\notlar.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(",")
                self.ogrenci = data[0]+" "+data[1]
                self.ortalama = (int(data[2])+int(data[3])+int(data[4]))/3
                print(self.ogrenci,self.harf_degeri()) 
                Student.sonuclar.append(f"{self.ogrenci} {self.harf_degeri()}")

    def notkaydet(self):
        
        with open("W_7\\Tayyip_Guney\\student_app\\son_durum.txt","w") as file:
            for line in Student.sonuclar:
                file.write(line+"\n")
                
    def harf_degeri(self):
    
        if self.ortalama>=90 and self.ortalama<=100:
            self.harf = "AA"
        elif self.ortalama>=85 and self.ortalama<=89:
            self.harf = "BA"
        elif self.ortalama>=80 and self.ortalama<=84:
            self.harf = "BB"
        elif self.ortalama>=75 and self.ortalama<=79:
            self.harf = "CB"
        elif self.ortalama>=70 and self.ortalama<=74:
            self.harf = "CC"
        elif self.ortalama>=65 and self.ortalama<=69:
            self.harf = "DC"
        elif self.ortalama>=60 and self.ortalama<=64:
            self.harf = "DD"
        elif self.ortalama>=50 and self.ortalama<=59:
            self.harf = "FD"
        else:
            self.harf = "FF"
        return  self.harf
 
    def cikis(self):
        global is_on
        is_on = False

        print("Good Bye\n")
        
    def del_all(self):
        with open("W_7\\Tayyip_Guney\\student_app\\notlar.txt","w") as file:
            pass
        with open("W_7\\Tayyip_Guney\\student_app\\son_durum.txt","w") as file:
            pass
        
is_on = True
while is_on:
    print(50*"+")
    secim = input("1-Not Gir\n2-Not Hesapla\n3-Not Kaydet\n4-Cikis\n5-Temizle\nYapmak Istediginiz Islemi Seciniz: ")
    print("\n")
    
    st = Student(secim)
    my_operation = st.secim()
    my_operation()
    