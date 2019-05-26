# Ubuntu18でAnaconda2とAnaconda3を入れて、Python2とPython3を両方使えるようにする

著者：NaoyukiArai

初版：2018/08/12　改訂六版：2018/11/15


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
cd /home/ユーザー名  
vi .bashrc

2.  .bashrcファイルを開けたら、一番下に、次のように書き加える。順番は守る。  
export PATH="/home/ユーザー名/anaconda3/bin:$PATH"  
export PATH="/home/ユーザー名/anaconda2/bin:$PATH"  

3. 端末を閉じる。

## 3. Anaconda2とAnaconda3それぞれにモジュールをインストールできるようにする

1. 端末を開いて、次のように打つ。  
cd anaconda2/bin  
mv anaconda anaconda2  
mv conda conda2  
mv easy_install easy_install2  
mv pip pip2  
mv spyder spyder2

2. anaconda2、conda2、easyinstall2、pip2、spyder2のファイルの中身の最初の行を、#! /home/ユーザー名/anaconda2/bin/python2に書き換える。

3. pipやconda、spyderを使うときは、すべてpip2、conda2、spyder2のように「2」をつけるとAnaconda2でPython2を使うことになり、「2」をつけないとAnaconda3、Python3を使うことになる。モジュールのインストール方法は「UbuntuでAnacondaを入れてPythonの環境を整える」マニュアルを見ること。

## 4. SpyderをLauncherに登録

1. 端末に、次のように打つ。
sudo apt install gnome-panel

2. 「この操作後に追加で76.4MBのディスク容量が消費されます。続行しますか？」とでるので、Yと打ってEnterキーを押す。

3. 「ホーム」で、gnome-desktop-item-edit --create-new .local/share/applications/ と打つと、ランチャーの作成ソフトが起動する。

4. 名前は「Spyder (python2.7)」、  
コマンドは「/home/ユーザー名/anaconda2/bin/spyder2」、  
コメントも「Spyder (python2.7)」、  
右上のアイコンを押し、/home/ユーザー名/anaconda2/share/iconsのアイコンファイルを選択する。

5. 名前は「Spyder (python3.6)」、  
コマンドは「/home/ユーザー名/anaconda3/bin/spyder」、  
コメントも「Spyder (python3.6)」、  
右上のアイコンを押し、/home/ユーザー名/anaconda3/share/iconsのアイコンファイルを選択する。

6. Launcherの一番下の「アプリケーションを表示する」をクリック。

7. 検索ボックスに「Spyder」と入力。

8. 検索して「アプリケーション」のところにでてきた、「Spyder (Python2.7)」と「Spyder(Python3.6)」をどちらも右クリックでお気に入りに追加する。


初版：2018/08/10  
二版：2018/08/22  
三版：2018/08/23  
四版：2018/09/13  
五版：2018/09/14  
六版：2018/11/15