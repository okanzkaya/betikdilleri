
'''
saat 03:57
Merhaba Komutan acilen uyan ülken savaşa girdi.
hemen komuta merkezine uçak filonu ve gereklii bilgileri bildir ve savaşmaya başla


daha önce tespit ettigin bazı sıkıntılar şunlardı:

-imha için havalanan uçağa hedef koordinatın yazılmıyor olması.
yani (0,0,0) yerine (x,y,z) gibi sayısal değerlerin olması gerekli - çözüldü

-savaşta kazanılan ya da kaybedilen skor kayıt altına alınmıyor.  - çözüldü

-şavaşta kaybedilen uçaklar uçak filosundan düşmüyor(eksilmesi lazım) - çözüldü

-
#######-------------------------------------------------########
savaşın kazanılması için yapılmasını istediğin yenilikler:

-savaşı kazanma ihtimalini artırmanın yolu şudur ki:
????????????????????????düşün karar ver uygula GENERALLİĞE Terfi et.......??????
bu noktada düşünüp geliştireceğin stratejiyi kodlayıp savaşta üstünlüğü yakala -- tek seferde 2 uçak göndermeyi denedim.

'''
import random
import time
import math

class Radar:
    def __init__(self):
        self.koordinat=(0,0,0)
        self.asker=0
        self.tank=0
        self.ucak=0
        self.hedef=(0,0,0)
    def ucak_goruldu(self):
        self.ucak+=1
    def ucak_imha_edildi(self):
        self.ucak-=1
    def tank_goruldu(self):
        self.tank+=1
    def tank_imha_edildi(self):
        self.tank-=1
    def asker_goruldu(self):
        self.asker+=1
    def asker_imha_edildi(self):
        self.asker-=1
    def koordinat_tarama(self, ucak, ucak2):
        
        cisim=random.randint(1,9)
        koordinat=random.randint(0,50),random.randint(0,50),random.randint(0,50)

        if cisim < 5 and cisim > 3:
            print('hedefte düşman uçağı tespit edildi')
            self.ucak_goruldu()
            self.hedef=koordinat
            ucak.koordinata_git(*koordinat)
            ucak2.koordinata_git(*koordinat)
        elif cisim< 3 and cisim > 1:
            print('hedefte düşman tankı tespit edildi')
            self.tank_goruldu()
            self.hedef = koordinat
            ucak.koordinata_git(*koordinat)
            ucak2.koordinata_git(*koordinat)
        elif cisim < 7 and cisim> 5:
            print('hedefte düşman askeri tespit edildi')
            self.asker_goruldu()
            self.hedef = koordinat
            ucak.koordinata_git(*koordinat)
            ucak2.koordinata_git(*koordinat)
        else:
            print('{} temiz'.format(koordinat))
            return 0
        return cisim

class Ucak_Filosu:
    def __init__(self):
        self.ucaklar=[]
    def Ucak_Filosuna_Ekle(self,ucak):
        self.ucaklar.append(ucak)
    def Ucak_Filosundan_Cikar(self):
        self.ucaklar.pop()
    def filo_goster(self):
        for i in self.ucaklar:
            print('{} nolu {} {} koordinatta {} vaziyetindedir'.format(i.ucak_id, i.ucak_turu, i.koordinat,
                                                                       i.durum))


class Ucak:
    def __init__(self,ucak_id,ucak_turu):
        self.ucak_id=ucak_id
        self.ucak_turu=ucak_turu
        self.durum='durma'
        self.koordinat=(0,0,0)
    def koordinata_git(self,x,y,z):
        self.koordinat=(x,y,z)
    def ucak_bilgisi(self):
        print('{} nolu {} {} koordinatta {} vaziyetindedir'.format(self.ucak_id,self.ucak_turu,self.koordinat,self.durum))


class Sorti:
    def __init__(self, sorti_id, filo, hedef):
        self.flight_number = sorti_id
        self.filo = filo
        self.hedef = hedef
        self.vaziyet = 'planlandı'

    def hedefi_imha_et(self):
        print('imha için 2 adet uçak havalandı hedef {} koordinatına doğru gidiliyor.'.format(self.hedef))
        time.sleep(1)
        print('hedefe kitlendi.....atış yapılıyor.....')
        time.sleep(1)
        atis = random.random()
        atis2 = random.random()
        self.vaziyet = 'bombalıyor'
        if atis < 0.5 and atis2 < 0.5:
            print('merkez hedef ıskalandı ..... ')
            time.sleep(1)
            print('pilot : ..merkez tuzağa düştüm, ikinci uçak geri çekildi, ben kurtulamayacağım......Eşhedü.... ')
            time.sleep(1)
            print(f'Merkez : ...Tüm birimlere idsi:{self.filo.ucaklar[-1].ucak_id} olan {self.filo.ucaklar[-1].ucak_turu} uçağımız düşürüldü')
            self.filo.Ucak_Filosundan_Cikar()
            global kaybedilen
            kaybedilen  += 1
        else:
            print('merkez hedef başarıyla imha edildi.')
            global kazanilan
            kazanilan += 1



u=Ucak('001','F16')
v=Ucak('002','F22')
k=Ucak('s0001','siha')
l=Ucak('s0001','siha')
m=Ucak('s0002','siha')
n=Ucak('s0003','siha')

filo=Ucak_Filosu()
filo.Ucak_Filosuna_Ekle(u)
filo.Ucak_Filosuna_Ekle(v)
filo.Ucak_Filosuna_Ekle(k)
filo.Ucak_Filosuna_Ekle(l)
filo.Ucak_Filosuna_Ekle(m)
filo.Ucak_Filosuna_Ekle(n)

kazanilan = 0
kaybedilen = 0

while True:
    t1=Radar()
    hdf=t1.hedef
    tarama=t1.koordinat_tarama(filo.ucaklar[-1], filo.ucaklar[-2])
    print('-----------------------------')
    print(kazanilan,kaybedilen)
    print('-----------------------------')
    if kazanilan==5 or kaybedilen==5:
        galip=max(kazanilan,kaybedilen)
        print('savaş bitti ')
        if galip==kazanilan:
            print('oley savaş kazanıldı ')
        else :
            print('maalesef savaş kaybettik.')
        break
    else:
        if tarama>0:
            print('hedeflerin imhası için koordinatlar merkeze gönderiliyor')
            imh = Sorti('imha01', filo, hdf)
            time.sleep(1)
            imh.hedefi_imha_et()
            time.sleep(1)
            #print(f'kazanilan: {kazanilan}')
            #print(f'kaybedilen: {kaybedilen}')
        else:
            print('...diğer bölgeler taranılıyor.....')
            time.sleep(1)
