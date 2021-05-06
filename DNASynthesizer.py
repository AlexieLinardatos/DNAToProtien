
#This function takes dna and turns it into a dna template
def CodeToTemp(dna):
    CodeToTempDic ={
    "c" : "g",
    "a":"t",
    "t":"a",
    "g":"c"
    }
    finalBeforeProtein =""
    for x in range(0,len(dna)):
        finalBeforeProtein += CodeToTempDic.get(dna[x])
    return finalBeforeProtein.strip()

#This turns the template dna to Rna
def TempToRna(temp):
    temp.replace("t","u").strip()
    TemptoRnaDic ={
    "c" : "g",
    "a":"u",
    "t":"a",
    "g":"c"
    }
    final = ""
    for x in range(0,len(temp)):
        final += TemptoRnaDic.get(temp[x])

    return final 

#Take Rna and adds amuno acides
def RnaToProten(prot):
    protien = []
    finSeq = ""
    RnaToProtenDic ={
    "uuu":"Phe",
    "uuc":"Phe",
    "uua":"Leu",
    "uug":"Leu",
    "ucu":"Ser",
    "ucc":"Ser",
    "uca":"Ser",
    "ucg":"Ser",
    "uau":"Tyr",
    "uac":"Tyr",
    "uaa":"stop",
    "uag":"stop",
    "ugu":"Cys",
    "ugc":"Cys",
    "uga":"stop",
    "ugg":"Trp",
    "cuu":"Leu",
    "cuc":"Leu",
    "cua":"Leu",
    "cug":"Leu",
    "ccu":"Pro",
    "ccc":"Pro",
    "cca":"Pro",
    "ccg":"Pro",
    "cau":"His",
    "cac":"His",
    "caa":"Gin",
    "cag":"Gin",
    "cgu":"Arg",
    "cgc":"Arg",
    "cga":"Arg",
    "cgg":"Arg",
    "auu":"IIe",
    "auc":"IIe",
    "aua":"IIe",
    "aug":"Met",
    "acu":"Thr",
    "acc":"Thr",
    "aca":"Thr",
    "acg":"Thr",
    "aau":"Asn",
    "aac":"Asn",
    "aaa":"Lys",
    "aag":"Lys",
    "agu":"Ser",
    "agc":"Ser",
    "aga":"Arg",
    "agg":"Arg",
    "guu":"Val",
    "guc":"Val",
    "gua":"Val",
    "gug":"Val",
    "gcu":"Ala",
    "gcc":"Ala",
    "gca":"Ala",
    "gcg":"Ala",
    "gau":"Asp",
    "gac":"Asp",
    "gaa":"Asp",
    "gag":"Asp",
    "ggu":"Gly",
    "ggc":"Gly",
    "gga":"Gly",
    "ggg":"Gly",
    }
    for i in range(0, len(prot), 3):
        protien.append(prot[i : i + 3])
        
    for i in range(0, len(protien)):
       finSeq += RnaToProtenDic.get(protien[i])
    print("prot",protien)
    print("helo")
    
    return finSeq



dna = input("Please enter DNA strand: ")
print("This is the ammino accid chain",RnaToProten(TempToRna(CodeToTemp(dna))))
