# 課題00

# 01
name1 = "ねずこ"
name2 = "ぜんいつ"

print (name1 + "と" + name2 + "は仲間です")

# 02
name1 = "ねずこ"
name2 = "むざん"

def if_muzan(name):
    if name == "むざん":
        print (name + "は仲間ではありません") 
    else:
        print(name + "は仲間です")

if_muzan(name2)

# 03
name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ")
print(name)

# 04
for n in name:
    print(n)



# 05
# 01
def study01(a, b):
    return (a + "と" + b + "は仲間です")
name1 = "ねずこ"
name2 = "ぜんいつ"
p = study01(name1, name2)
print(p)

# 02
def study02(a, b):

    if b == "むざん":
        return (b + "は仲間ではありません") 
    else:
        return(a + "は仲間です")

name1 = "ねずこ"
name2 = "むざん"
p = study02(name1, name2)
print(p)

# 03
def study03(a):
    return(a)
name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ")
p = study03(name)
print(p)


# 04
def study04(a):
    for b in a:
        return(b)
p = study04(name)
print(p)

##############ここまで課題05

# 06
def study06(hikisuu):
    if (hikisuu in name):
        return(hikisuu + "はリストに存在します")
    else:
        return(hikisuu + "はリストに存在しません")


sample1 = "鬼滅の刃"
p = study06(sample1)
print(p)
sample2 = "ねずこ"
p = study06(sample2)
print(p)