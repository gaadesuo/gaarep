kbn = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
kbh = "qwertasdfgzxcvb"
kbm = "yuiophjklnm"

inp = input()
#inp = "lkfhakmwnleighlaid"
rst = 0
bfr = inp[0]
if  (kbh.find(bfr) != -1): typ = 0
elif(kbm.find(bfr) != -1): typ = 1
#print(inp, bfr, typ)

for trg in inp[1:]:
    if  (kbh.find(trg) != -1): hmp = 0
    elif(kbm.find(trg) != -1): hmp = 1
    if  (kbn[0].find(trg) != -1): y = 0
    elif(kbn[1].find(trg) != -1): y = 1
    elif(kbn[2].find(trg) != -1): y = 2
    x = kbn[y].find(trg)
    z = len(kbn[y])-1

   rin = kbn[y+0][x+0]
    if((x-1)>=0): rin = rin + kbn[y+0][x-1]
    if((x+1)<=z): rin = rin + kbn[y+0][x+1]
    if(((y-1)>=0) and ((len(kbn[y-1])-1) >= x)): rin = rin + kbn[y-1][x+0]
    if(((y+1)<=2) and ((len(kbn[y+1])-1) >= x)): rin = rin + kbn[y+1][x+0]

#    print(typ, hmp, bfr, rin)

   if(typ != hmp):
        if(rin.find(bfr) != -1): rst = rst + 1
        else                   : typ = hmp

   bfr = kbn[y][x]
print(rst)