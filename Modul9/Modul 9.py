##========Nomor 6========

##class SimpulPohonBiner(object):
##    def __init__(self, data):
##        self.data = data
##        self.kiri = None
##        self.kanan = None
##
##def ukuranPohon(akar, count=0):
##    if akar is None:
##        return count
##
##    return ukuranPohon(akar.kiri, ukuranPohon(akar.kanan, count+1))
##
##a = SimpulPohonBiner('Banyuwangi')
##b = SimpulPohonBiner('Jakarta')
##c = SimpulPohonBiner('Cilacap')
##d = SimpulPohonBiner('Denpasar')
##e = SimpulPohonBiner('Sukoharjo')
##f = SimpulPohonBiner('Solo')
##g = SimpulPohonBiner('Surakarta')
##h = SimpulPohonBiner('Malang')
##
##a.kiri = b; a.kanan = c
##b.kiri = d; b.kanan = e
##c.kiri = f; c.kanan = g
##e.kiri = h;
##
##print('Ukuran dari Binary Tree ini adalah', ukuranPohon(a))
##


##========Nomor 7========

##class SimpulPohonBiner(object):
##    def __init__(self, data):
##        self.data = data
##        self.kiri = None
##        self.kanan = None
##
##def tinggiPohon(akar, count=0):
##    if akar is None:
##        return 0
##    else:
##        return max(tinggiPohon(akar.kiri), tinggiPohon(akar.kanan))+1
##
##a = SimpulPohonBiner('Banyuwangi')
##b = SimpulPohonBiner('Jakarta')
##c = SimpulPohonBiner('Cilacap')
##d = SimpulPohonBiner('Denpasar')
##e = SimpulPohonBiner('Sukoharjo')
##f = SimpulPohonBiner('Solo')
##g = SimpulPohonBiner('Surakarta')
##h = SimpulPohonBiner('Malang')
##
##a.kiri = b; a.kanan = c
##b.kiri = d; b.kanan = e
##c.kiri = f; c.kanan = g
##e.kiri = h;
##
##print('Tinggi Maksimum dari Binary Tree ini adalah', tinggiPohon(a))



##========Nomor 8========

class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def cetakDataDanLevel(akar, count = 0):
    if akar is not None:
        print (akar.data + ', level '+ str(count))
        (cetakDatadanLevel(akar.kiri, count+1),
         cetakDatadanLevel(akar.kanan, count+1))

a = SimpulPohonBiner('Banyuwangi')
b = SimpulPohonBiner('Jakarta')
c = SimpulPohonBiner('Cilacap')
d = SimpulPohonBiner('Denpasar')
e = SimpulPohonBiner('Sukoharjo')
f = SimpulPohonBiner('Solo')
g = SimpulPohonBiner('Surakarta')
h = SimpulPohonBiner('Malang')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h;

datalist=[a.data, b.data, c.data, f.data, e.data, f.data, g.data, h.data]
level=[]

def preorder(sub):
    if sub is not None:
        print(sub.data)
        preorder(sub.kiri)
        preorder(sub.kanan)
        
def inorder(sub):
    if sub is not None:
        inorder(sub.kiri)
        print(sub.data)
        inorder(sub.kanan)

def postorder(sub):
    if sub is not None:
        postorder(sub.kiri)
        postorder(sub.kanan)
        print(sub.data)
def traverse(root):
    lvlist=[]
    current_level = [root]
    lv=0
    while current_level:
        next_level = list()
        for n in current_level:
            if n.kiri:
                next_level.append(n.kiri)
                level.append(lv+1)
            if n.kanan:
                next_level.append(n.kanan)
                level.append(lv+1)
            current_level = next_level
            
        lv+=1
        lvlist.append(lv)
    return lvlist

def cetak(root):
    traverse(a)
    print(root.data, ', Level 0')
    for i in range(len(level)):
          print(datalist[i+1], ', Level', level[i])
cetak(a)

print("==========preorder==========")
preorder(a)
print("==========inorder==========")
inorder(a)
print("==========postorder==========")
postorder(a)

