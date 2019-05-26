# UbuntuでAnacondaを入れてPythonの環境を整える

著者：NaoyukiArai

初版：2018/07/13　改訂四版：2018/08/22


## 1.　Anacondaの導入

1. Anacondaのファイルを、ダウンロードして、ホームディレクトリに移動する。

2. shファイル名.sh でインストールできる。

3.　「Please, press and continue」とでるので、Enterキーを押す。

4.　「- Press ENTER to con rm the location」とでたら、Enterキーを押す。このときファイルの場所の確認だけでなくインストールもされる。

5.　「Do you wish the installer to prepend theAnaconda2 install location to PATH inyour /home/ユーザー名/.bashrc？」とでたら、「yes」と打ってEnterキーを押す。

6.　「Do you wish to proceed with the installation of microsoft VS code？」とでるので、Consolasという等幅フォントが使いたければ、「yes」（推奨）と打ってEnterキーを押す。

## 2. Anacondaの中のSpyderを使う。

端末を開いて、次のように打つ。  
cd /home/ユーザー名/anaconda2/bin  
./spyder

## 3. MDAnalysisのインストール

※「Proceed？」と聞かれたら、すべて「y」と打ってEnterキーを押す。  
端末を開いて、次のように打つ。  
conda config --add channels conda-forge  
conda install mdanalysis  
conda update mdanalysis  
conda install MDAnalysisTests


初版：2018/07/13  
二版：2018/07/15  
三版：2018/08/12  
四版：2018/08/22