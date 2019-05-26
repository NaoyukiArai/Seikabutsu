# Ubuntu16でAnaconda2とAnaconda3を入れて、Python2とPython3を両方使えるようにする

著者：NaoyukiArai

初版：2018/08/10　改訂三版：2018/08/23　更新終了


## 1.　Anaconda2,3の導入

Anaconda2,3両方に対して、同じことを繰り返す。

1. Anacondaのファイルをダウンロードし、ホームディレクトリに移動させる。

2. 端末を開いて、sh ファイル名.shでインストールできる。

3. 「Please, press and continue」とでるので、Enterキーを押す。

4. 「- Press ENTER to con rm the location」とでたら、Enterキーを押す。このときファイルの場所の確認だけでなくインストールもされる。

5. 「Do you wish the installer to prepend theAnaconda2 install location to PATH inyour /home/ユーザー名/.bashrc？」とでたら、「yes」と打ってEnterキーを押す。

6. 「Do you wish to proceed with the installation of microsoft VS code？」とでるので、Consolasという等幅フォントが使いたければ、「yes」（推奨）と打ってEnterキーを押す。

## 2. PATHを通す

1. 端末に、次のように打つ。  
sudo su  
cd /home/ユーザー名  
vi .bashrc

2.  .bashrcファイルを開けたら、一番下に、次のように書き加える。順番は守る。  
export PATH="/home/ユーザー名/anaconda3/bin:$PATH"  
export PATH="/home/ユーザー名/anaconda2/bin:$PATH"  
このとき、もうすでにどちらかが書き込まれていた場合は、それを消してこれを書き、「bash」と端末に打つ。

3. 端末を閉じる。

## 3. Anaconda2とAnaconda3それぞれにモジュールをインストールできるようにする

1. 端末を開いて、次のように打つ。  
cd anaconda2/bin  
mv anaconda anaconda2  
mv conda conda2  
mv easy_install easy_install2  
mv pip pip2  
mv spyder spyder2

2. pipやconda、spyderを使うときは、すべてpip2、conda2、spyder2のように「2」をつけるとAnaconda2でPython2を使うことになり、「2」をつけないとAnaconda3、Python3を使うことになる。モジュールのインストール方法は「UbuntuでAnacondaを入れてPythonの環境を整える」マニュアルを見ること。

## 4. SpyderをLauncherに登録

1. 端末に、次のように打つ。  
cd  
cd .local/share/applications

2. 中身を次のよう書いたspyder2.desktopファイルを作成。  
[Desktop Entry]  
Encoding=UTF-8  
Version=1.0  
Type=Application  
Name=Spyder (Python2.7)  
Icon=spyder.png  
Exec=/home/ユーザー名/anaconda2/bin/python /home/ユーザー名/anaconda2/bin/spyder2  
StartupNotify=false  
StartupWMClass=Spyder  
OnlyShowIn=Unity;  
X-UnityGenerated=true

3. 中身を次のよう書いたspyder.desktopファイルを作成。  
[Desktop Entry]  
Encoding=UTF-8  
Version=1.0  
Type=Application  
Name=Spyder (Python3.6)  
Icon=spyder.pngExec=/home/ユーザー名/anaconda3/bin/python /home/ユーザー名  /anaconda3/bin/spyder  
StartupNotify=false  
StartupWMClass=Spyder  
OnlyShowIn=Unity;  
X-UnityGenerated=true
4. Launcherから「コンピュータを検索」をクリック。

5. 検索ボックスに「Spyder」と入力。

6. 検索して「アプリケーション」のところにでてきた、「Spyder (Python2.7)」と「Spyder(Python3.6)」のどちらも開く。

7. Launcherのところにそれぞれのアイコンが出てくるので、それを右クリックして、「Launcherに登録」をクリックする。


初版：2018/08/10  
二版：2018/08/12  
三版：2018/08/23