s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

for word in s.split(" "):
    a=''
    for i in word:
        if(ord(i)+2>122):
            a=a+(chr(ord(i)+2-26))
        else:
            a=a+(chr(ord(i)+2))
    print(a+" ")

chr(97)
chr(122)
