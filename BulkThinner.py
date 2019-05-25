# -*- coding: utf-8 -*-
"""
2018年5月30日作成

@author:NaoyukiArai
"""

"""####################################################"""
"""####################取り扱い説明書####################"""
"""####################################################"""
"""

目的
基板の上に置いた
ある高さ以上のイオン液体の分子を削除し、
カチオンとアニオンの数を等しく修正して、
番号を再度順番につけた
ファイルを作るプログラム。

制限
単原子分子の場合は用いることができない。
GROファイルのみに対応している。

その他注釈
あえて関数を使わなかった理由は
引数が多くなりすぎるため。

"""
"""####################################################"""
"""####################取り扱い説明書####################"""
"""####################################################"""


"""####################################################"""
"""########################前半########################"""
"""####################################################"""


"""#☆#☆#☆#☆#☆#☆#☆#　好きな値を入力　#☆#☆#☆#☆#☆#☆#☆#"""

retsu=4 #Excelで表示したときにFloat型に直せる文字列の何列目か（最初の列を1とする）
ekitai=3.20 #イオン液体の厚さ
kibannm=3.02 #基板の厚さ
cation='' #カチオンのgroファイル上での名前
anion='' #アニオンのgroファイル上での名前
kiban='' #基板のgroファイル上での名前
kibansurface='' #基板表面のgroファイル上での名前
inputfile='' #入力ファイル名（拡張子抜き）
LogFile='IranaiFile' #ログファイルの名前（拡張子抜き）
LogFileKakuchoushi='.log' #ログファイルの拡張子
outputfile='ekitai' #出力ファイル名（拡張子抜き）
CationAtomSu=10 #カチオン分子一つ当たり原子数
AnionAtomSu=3 #アニオン分子一つ当たり原子数
StrRetsuSu=2 #文字列部分の列の数
FloatRetsuSu=4 #float型部分の列の数
GroGyo=[8,15,20,28,36,44] #groの原子のデータ部分の一列の文字の終わりの文字がある列数（vimで見た時の）
ReaderZembu=[] #CSVモジュールのようにgroファイルを読み込んだ後のリスト

"""#☆#☆#☆#☆#☆#☆#☆#　好きな値を入力　#☆#☆#☆#☆#☆#☆#☆#"""

atai=ekitai+kibannm #基板とイオン液体を足した厚さ

import csv

####################ここから読み込み####################

#----------初期値----------#

i=0 #行数
j=0 #何番目の文字か
ReaderCombined=''
CopyReaderYou=[] #ファイルの一行分をリストに変換
CopyReader=[] #ファイルの一行分のコピー
ReaderSplit=[] #リスト形式で読み込むためのリスト
ReaderZembu=[] #CSVモジュールのようにgroファイルを読み込んだ後のリスト
SpaceDeleter=[] #スペースを消して文字列を分割できるようにするためのリスト
ReaderHeaderFooter=[] #ヘッダーとフッターをリストにする
    
#----------プログラム部分----------#
       
f=open(inputfile+'.gro','rU') #ファイル読み込み開始
       
for reader in f: #CSVモジュールのように読み込んでリストにする
    CopyReaderYou.append(reader.rstrip('\n')) #ヘッダーとフッターを保存
    CopyReader=CopyReaderYou
    if i<=1:
        ReaderHeaderFooter.append(CopyReader)
    for row in reader:
        if len(reader)==GroGyo[-1]+1:
            j+=1
        SpaceDeleter.append(row)
        if j in GroGyo and j!=GroGyo[-1]:
            SpaceDeleter.append(' ')
        if len(SpaceDeleter)>=2:
            if SpaceDeleter[-2]==' ' and SpaceDeleter[-1]==' ':
                del SpaceDeleter[-1]
        if j==GroGyo[-1]+1:
            j=0
    del SpaceDeleter[-1]
    if SpaceDeleter[0]==' ':
        del SpaceDeleter[0]
    ReaderCombined=''.join(SpaceDeleter)
    ReaderSplit=ReaderCombined.split(' ')
    SpaceDeleter=[]
    ReaderZembu.append(ReaderSplit)
    CopyReaderYou=[]
    i+=1
        
f.close() #ファイル読み込み終了
        
ReaderHeaderFooter.append(CopyReader)
    
ReaderZembu[0]=ReaderHeaderFooter[0] #ReaderZembuの補正
ReaderZembu[1]=ReaderHeaderFooter[1]
ReaderZembu[-1]=ReaderHeaderFooter[-1]
    
    
####################ここまで読み込み####################

#----------初期値----------#

i=0 #（一行目の）行数
f=0 #float型にできる列を検出するための変数
fsigma=0 #文字列以外の部分の総数
realcopyreader=[] #readerの完コピリスト
copyreader=[] #csvのリスト形式のコピーリスト（文字列のみのリストを含まない）
strrow=[] #一行の文字列部分
floatrow=[] #一行の数字部分
strrowrow=[] #リストの文字列部分
floatrowrow=[] #リストの数字部分
gyoshushi=[] #初期化
    
#----------文字列の部分のリストとfloatの部分のリストに分ける----------#
    
ReaderZembu[1].extend(['','','','']) #Gro読み込みの便宜上のもの

for row in ReaderZembu:
    realcopyreader.append(row)
    for kata in row:
        try:
            floatrow.append(float(kata))
        except:
            strrow.append(kata)
            f+=1
    floatrowrow.append(floatrow)
    strrowrow.append(strrow)
    copyreader.append(row)
    if f==0: #全部が文字列ならリストに入れない
        fsigma+=1
        copyreader.remove(row)
        floatrowrow.remove(floatrow)
        strrowrow.remove(strrow)
    f=0
    strrow=[] #一行の文字列部分初期化
    floatrow=[] #一行の数字部分初期化
    i+=1

#----------初期値----------#

bindrow=[] #CSVの、リストのリストの、空リスト
kindofatom='hogehoge' #初期値の要素としてかぶらない適当な値を入れてるだけ
saigo='hogehoge' #最後の値の要素としてかぶらない適当な値を入れてるだけ
gyoshushi=[] #行の値が同じ最初から最後までの行番号を入れる
allgyoshushi=[] #gyoshushiのリスト
i=0 #（一行目の）行数
j=0 #（一行目の）同じ分子番号が続いた数
gyoshushi.append(0) #（一行目の）分子番号が同じ塊の始まり
    
#----------分子番号が同じ範囲のリストを作成----------#

realcopyreader.append(saigo) #最後に便宜のための値を入れる

for row in realcopyreader:
    if kindofatom!=row[0]: #分子番号が変わっていたら
        if len(gyoshushi)==2:
            allgyoshushi.append(gyoshushi)
        else:
            gyoshushi.append(gyoshushi[0])
            allgyoshushi.append(gyoshushi)
        kindofatom=row[0]
        gyoshushi=[] #同じ分子番号の行の始めと終わりの行数を初期化
        gyoshushi.append(i)
    else: #同じ番号が続いているとき
        if len(gyoshushi)==2:
            gyoshushi[1]=i
        else:
            gyoshushi.append(i)

    i+=1

del allgyoshushi[0] #無駄な初期値との比較の行を消去

#----------初期値----------#

i=0 #（一行目の）行数

#----------ある一定の値より低い位置にある分子の行のリストを作る----------#

for floatrow in floatrowrow:
    try:
        if floatrow[retsu-1]>=atai: #消す（下限）の高さ
            for gyoshushi in allgyoshushi:
                if gyoshushi[0]<=i+fsigma and gyoshushi[1]>=i+fsigma:
                    del allgyoshushi[allgyoshushi.index(gyoshushi)]
                gyoshushi=[]
    except:
        pass
    finally:
        i+=1
            
#----------初期値----------#

copycopyreader=[] #最終生成物

#----------ある一定の値より低い位置にある分子だけ抜き取ってリストを作る----------#

for gyoshushi in allgyoshushi:
    num=0
    while num<=(gyoshushi[1]-gyoshushi[0]):
        copycopyreader.append(copyreader[gyoshushi[0]+num])
        num+=1

####################ここから書き込み####################
    
with open(LogFile+'100000'+LogFileKakuchoushi, 'w') as f: #書き込む
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(copycopyreader)

####################ここまで書き込み####################
        
"""####################################################"""
"""########################中盤########################"""
"""####################################################"""

InputFile=outputfile

n=100000 #一回はループするため

while n>1:

    ####################ここから読み込み####################

    with open(LogFile+str(n)+LogFileKakuchoushi, 'rU') as f: #読み込む
        reader = csv.reader(f)

    ####################ここまで読み込み####################
        
    #----------初期値----------#

        i=0 #（一行目の）行数
        f=0 #float型にできる列を検出するための変数
        RealCopyReader=[] #readerの完コピリスト
        CopyReader=[] #csvのリスト形式のコピーリスト（文字列のみのリストを含まない）
        StrRow=[] #一行の文字列部分
        FloatRow=[] #一行の数字部分
        StrRowRow=[] #リストの文字列部分
        FloatRowRow=[] #リストの数字部分
        GyoShushi=[] #初期化
    
    #----------文字列の部分のリストとfloatの部分のリストに分ける----------#

        for row in reader:
            RealCopyReader.append(row)
            for kata in row:
                try:
                    FloatRow.append(float(kata))
                except:
                    StrRow.append(kata)
                    f+=1
            FloatRowRow.append(FloatRow)
            StrRowRow.append(StrRow)
            CopyReader.append(row)
            if f==0: #全部が文字列ならリストに入れない
                CopyReader.remove(row)
                FloatRowRow.remove(FloatRow)
                StrRowRow.remove(StrRow)
            f=0
            StrRow=[] #一行の文字列部分初期化
            FloatRow=[] #一行の数字部分初期化
            i+=1

    #----------初期値----------#

        i=0 #行数
        j=0 #ループ回数の変数
        cat=0 #カチオン原子数
        ani=0 #アニオン原子数
        noko=0 #基板原子数
        Header=0 #ヘッダーの行数
        Footer=0 #フッターの行数
        CationFloatRetsu=[] #カチオンのZ座標のリスト
        AnionFloatRetsu=[] #アニオンのZ座標のリスト
        NokoriFloatRetsu=[] #残りのZ座標のリスト
        FloatRetsu=[] #Z座標すべてのリスト

    #----------カチオンとアニオンの分子の原子数を数える、float列をカチオン、アニオン、それ以外に分ける----------#

        for FloatRow in FloatRowRow: #Z座標のリストを作る
            if len(FloatRow)==4:
                if StrRowRow[i][0].find(anion)!=-1: #カチオン、アニオン、それ以外のZ座標のリストそれぞれを作る
                    AnionFloatRetsu.append(FloatRow[retsu-1])
                    ani+=1
                elif StrRowRow[i][0].find(cation)!=-1:
                    CationFloatRetsu.append(FloatRow[retsu-1])
                    cat+=1
                else:
                    NokoriFloatRetsu.append(FloatRow[retsu-1])
                    noko+=1
                FloatRetsu.append(FloatRow[retsu-1])
            elif ani==0:
                Header+=1
            elif noko>0:
                Footer+=1

            i+=1
        

    #----------初期値----------#

        BindRow=[] #CSVの、リストのリストの、空リスト
        KindOfAtom='hogehoge' #初期値の要素としてかぶらない適当な値を入れてるだけ
        saigo='hogehoge' #最後の値の要素としてかぶらない適当な値を入れてるだけ
        GyoShushi=[] #行の値が同じ最初から最後までの行番号を入れる
        AllGyoShushi=[] #gyoshushiのリスト
        i=0 #（一行目の）行数
        j=0 #（一行目の）同じ分子番号が続いた数
        GyoShushi.append(0) #（一行目の）分子番号が同じ塊の始まり
    
    #----------分子番号が同じ範囲のリストを作成----------#

        RealCopyReader.append(saigo) #最後に便宜のための値を入れる

        for row in RealCopyReader:
            if KindOfAtom!=row[0]: #分子番号が変わっていたら
                if len(GyoShushi)==2:
                    AllGyoShushi.append(GyoShushi)
                else:
                    GyoShushi.append(GyoShushi[0])
                    AllGyoShushi.append(GyoShushi)
                KindOfAtom=row[0]
                GyoShushi=[] #同じ分子番号の行の始めと終わりの行数を初期化
                GyoShushi.append(i)
            else: #同じ番号が続いているとき
                if len(GyoShushi)==2:
                    GyoShushi[1]=i
                else:
                    GyoShushi.append(i)

            i+=1

        del AllGyoShushi[0] #無駄な初期値との比較の行を消去

    #----------初期値----------#

        ZembuCationAtomSu=0 #カチオンの原子で、ある高さ以上を削除したときに残った分の個数
        ZembuAnionAtomSu=0 #アニオンの原子で、ある高さ以上を削除したときに残った分の個数
        ZembuNokoriAtomSu=0 #基板の原子で、ある高さ以上を削除したときに残った分の個数
        n=0 #イオンの個数の差

    #----------カチオンとアニオンの分子数の差を計算で出す----------#

        for GyoShushi in AllGyoShushi: #それぞれの原子数で、ある高さ以上を削除したときに残った分をカウント
            if GyoShushi[0]>=Header and GyoShushi[1]<(ani+Header):
                ZembuAnionAtomSu+=(GyoShushi[1]-GyoShushi[0]+1)
            if GyoShushi[0]>=(ani+Header) and GyoShushi[1]<(ani+cat+Header):
                ZembuCationAtomSu+=(GyoShushi[1]-GyoShushi[0]+1)
            if GyoShushi[0]>=(ani+cat+Header) and GyoShushi[1]<(ani+cat+noko+Header):
                ZembuNokoriAtomSu+=(GyoShushi[1]-GyoShushi[0]+1)
    
        n=abs(ZembuCationAtomSu/CationAtomSu-ZembuAnionAtomSu/AnionAtomSu) #イオン個数の差
        
    #----------初期値----------#

        i=0 #行数
        GyoShushi=[] #初期化
    
    #----------多いほうのイオンの中で、一番高い位置にある原子を持つものを特定し、抹消する----------#

        if ZembuCationAtomSu/CationAtomSu>ZembuAnionAtomSu/AnionAtomSu:
            i=ZembuAnionAtomSu #開始行数
            while 1:
                if CationFloatRetsu[i]==sorted(CationFloatRetsu)[-1]:
                    break
                i+=1
        if ZembuCationAtomSu/CationAtomSu<ZembuAnionAtomSu/AnionAtomSu:
            i=0 #開始行数
            while 1:
                if AnionFloatRetsu[i]==sorted(AnionFloatRetsu)[-1]:
                    break
                i+=1

        if ZembuCationAtomSu/CationAtomSu!=ZembuAnionAtomSu/AnionAtomSu:
             for GyoShushi in AllGyoShushi:
                 if GyoShushi[0]<=i+Header and GyoShushi[1]>=i+Header:
                     del AllGyoShushi[AllGyoShushi.index(GyoShushi)]

    #----------初期値----------#

        CopyCopyReader=[] #最終生成物

    #----------ある一定の値より低い位置にある分子だけ抜き取ってリストを作る----------#
        for GyoShushi in AllGyoShushi:
            num=0
            while num<=(GyoShushi[1]-GyoShushi[0]):
                CopyCopyReader.append(CopyReader[GyoShushi[0]+num])
                num+=1

    ####################ここから書き込み####################
        if n!=1 and n!=0:
            with open(LogFile+str(n)+LogFileKakuchoushi, 'w') as f: #書き込む
                writer = csv.writer(f, lineterminator='\n')
                writer.writerows(CopyCopyReader)
        else:
            with open(LogFile+LogFileKakuchoushi, 'w') as f: #書き込む
                writer = csv.writer(f, lineterminator='\n')
                writer.writerows(CopyCopyReader)

        ####################ここまで書き込み####################
    
    
"""####################################################"""
"""########################後半########################"""
"""####################################################"""


####################ここから読み込み####################

with open(LogFile+LogFileKakuchoushi, 'rU') as f: #読み込む
    reader = csv.reader(f)

####################ここまで読み込み####################
        
    #----------初期値----------#

    i=0 #（一行目の）行数
    f=0 #float型にできる列を検出するための変数
    RealCopyReader=[] #readerの完コピリスト
    CopyReader=[] #csvのリスト形式のコピーリスト（文字列のみのリストを含まない）
    StrRow=[] #一行の文字列部分
    FloatRow=[] #一行の数字部分
    StrRowRow=[] #リストの文字列部分
    FloatRowRow=[] #リストの数字部分
    GyoShushi=[] #初期化
    
    #----------文字列の部分のリストとfloatの部分のリストに分ける----------#

    for row in reader:
        RealCopyReader.append(row)
        for kata in row:
            try:
                if j==0:
                    FloatRow.append(float(kata))
                else:
                    FloatRow.append("{0:.3f}".format(float(kata)))
            except:
                StrRow.append(kata)
                f+=1
            finally:
                j+=1
        FloatRowRow.append(FloatRow)
        StrRowRow.append(StrRow)
        CopyReader.append(row)
        if f==0: #全部が文字列ならリストに入れない
            CopyReader.remove(row)
            FloatRowRow.remove(FloatRow)
            StrRowRow.remove(StrRow)
        f=0
        StrRow=[] #一行の文字列部分初期化
        FloatRow=[] #一行の数字部分初期化
        i+=1
        j=0

    #----------初期値----------#

    i=0 #行数
    j=0 #ループ回数の変数
    cat=0 #カチオン原子数
    ani=0 #アニオン原子数
    noko=0 #基板原子数
    Header=0 #ヘッダーの行数
    Footer=0 #フッターの行数
    CationFloatRetsu=[] #カチオンのZ座標のリスト
    AnionFloatRetsu=[] #アニオンのZ座標のリスト
    NokoriFloatRetsu=[] #残りのZ座標のリスト
    FloatRetsu=[] #Z座標すべてのリスト
    
    #----------カチオンとアニオンの分子の原子数を数える、float列をカチオン、アニオン、それ以外に分ける----------#

    for FloatRow in FloatRowRow: #Z座標のリストを作る
        if len(FloatRowRow[i])==4:
            if StrRowRow[i][0].find(anion)!=-1: #カチオン、アニオン、それ以外のZ座標のリストそれぞれを作る
                AnionFloatRetsu.append(FloatRow[retsu-1])
                ani+=1
            elif StrRowRow[i][0].find(cation)!=-1:
                CationFloatRetsu.append(FloatRow[retsu-1])
                cat+=1
            else:
                NokoriFloatRetsu.append(FloatRow[retsu-1])
                noko+=1
            FloatRetsu.append(FloatRow[retsu-1])
        elif ani==0:
            Header+=1
        elif noko>0:
            Footer+=1
        
        i+=1
        
    #----------初期値----------#

    i=0 #行数
    bango=0 #分子の順番の番号
    GenshiSu=0 #原子数を数える
    mae='' #便宜的に値を入れている、分子の種類の番号
    CopyStrRow=[] #StrRowの完コピ
    StrRow=[] #StrRowRowの要素
    row=[]
    CopyStrRowRow=[] #StrRowRowの完コピ

    #----------str列をカチオン、アニオン、基板に分ける、順番に分子に番号をつける----------#

    for StrRow in StrRowRow:
        for row in StrRow:
            CopyStrRow.append(row)
        CopyStrRowRow.append(CopyStrRow)
        CopyStrRow=[]
    
    for StrRow in StrRowRow:
        if len(FloatRowRow[i])==4:
            GenshiSu+=1
            if CopyStrRowRow[i][0]!=CopyStrRowRow[i-1][0]:
                bango+=1
            else:
                pass
            if StrRow[0].find(anion)!=-1:
                StrRowRow[i][0]=str(bango)+anion
            elif StrRow[0].find(cation)!=-1:
                StrRowRow[i][0]=str(bango)+cation
            elif StrRow[0].find(kiban)!=-1:
                StrRowRow[i][0]=str(bango)+kiban
            elif StrRow[0].find(kibansurface)!=-1:
                StrRowRow[i][0]=str(bango)+kibansurface            
            
        i+=1

    #----------初期値----------#

    i=1 #行数

    #----------float列をカチオン、アニオン、それ以外に分ける、順番に番号をつける----------#

    for FloatRow in FloatRowRow: #Z座標のリストを作る
        if len(FloatRow)==4:
            FloatRow[0]=i
            i+=1

    #----------初期値----------#

    StrSu=0 #文字列の列の数を数える変数
    FloatSu=0 #float型列の列の数を数える変数
    num=0 #繰り返しのための変数
    KetsugouList=[] #文字列型リストとfloat型リストを結合したものを作る
    CopyCopyReader=[] #最終生成物
    
    #----------リストを作る----------#

    CopyCopyReader.append(RealCopyReader[0]) #ヘッダーの文字列のみの部分を入れる
    CopyCopyReader.append([str(GenshiSu)]) #原子数を次に入れる

    while num<GenshiSu+Header:
        if len(FloatRowRow[num])==4:
            while StrSu<StrRetsuSu:
                KetsugouList.append(StrRowRow[num][StrSu])
                StrSu+=1
            while FloatSu<FloatRetsuSu:
                KetsugouList.append(str(FloatRowRow[num][FloatSu]))
                FloatSu+=1
            StrSu=0
            FloatSu=0

            CopyCopyReader.append(KetsugouList) #文字列リストとfloatリストの行を次々入れる
            KetsugouList=[] #初期化
        num+=1
    
    CopyCopyReader.append(copyreader[-1]) #フッターを最後に入れる

#----------情報の出力----------#
    
print("Atom : "+str(GenshiSu)+" [ko]")
with open('Info'+str(ekitai)+'nm.txt','w') as f:
     f.write("Atom : "+str(GenshiSu)+" [ko]"+'\n')

#----------カチオンとアニオンの数を出力----------#
    
if ZembuCationAtomSu/CationAtomSu>ZembuAnionAtomSu/AnionAtomSu:
    print(cation+" : "+str(ZembuCationAtomSu/CationAtomSu-1)+" [ko]")
    print(anion+" : "+str(ZembuAnionAtomSu/AnionAtomSu)+" [ko]")
    with open('Info'+str(ekitai)+'nm.txt','a') as f:
        f.write(cation+" : "+str(ZembuCationAtomSu/CationAtomSu-1)+" [ko]"+'\n')
        f.write(anion+" : "+str(ZembuAnionAtomSu/AnionAtomSu)+" [ko]")
    
if ZembuCationAtomSu/CationAtomSu<ZembuAnionAtomSu/AnionAtomSu:
    print(cation+" : "+str(ZembuCationAtomSu/CationAtomSu)+" [ko]")
    print(anion+" : "+str(ZembuAnionAtomSu/AnionAtomSu-1)+" [ko]")
    with open('Info'+str(ekitai)+'nm.txt','a') as f:
        f.write(cation+" : "+str(ZembuCationAtomSu/CationAtomSu)+" [ko]"+'\n')
        f.write(anion+" : "+str(ZembuAnionAtomSu/AnionAtomSu-1)+" [ko]")

if ZembuCationAtomSu/CationAtomSu==ZembuAnionAtomSu/AnionAtomSu:
    print(cation+" : "+str(ZembuCationAtomSu/CationAtomSu)+" [ko]")
    print(anion+" : "+str(ZembuAnionAtomSu/AnionAtomSu)+" [ko]")
    with open('Info'+str(ekitai)+'nm.txt','a') as f:
        f.write(cation+" : "+str(ZembuCationAtomSu/CationAtomSu)+" [ko]"+'\n')
        f.write(anion+" : "+str(ZembuAnionAtomSu/AnionAtomSu)+" [ko]")
        
####################ここから書き込み####################

#----------初期値----------#
    
i=0 #行数
j=0 #挿入するスペースの数
CopyRow=[] #rowをコピーしたもの
ReaderZembuStr=[] #リストのリストを文字列のリストにしたもの
    
#----------プログラム部分----------#
    
for row in CopyCopyReader:
    CopyRow.extend(row)
    if len(row)==len(GroGyo):
        while i<len(GroGyo):
            if i!=len(GroGyo)-1:
                while j<GroGyo[-i-1]-GroGyo[-i-2]-len(row[-i-1]):
                    CopyRow.insert(len(GroGyo)-i-1,' ')
                    j+=1
            else:
                while j<GroGyo[-i-1]-len(row[-i-1]):
                    CopyRow.insert(0,' ')
                    j+=1
                
            j=0
            i+=1
        i=0
    ReaderZembuStr.append(''.join(CopyRow))
    CopyRow=[]
        
with open(outputfile+'_'+str(ekitai)+'nm.gro','w') as f: #ファイル書き込み開始
    for reader in ReaderZembuStr:
        f.write(reader+'\n')

####################ここまで書き込み####################