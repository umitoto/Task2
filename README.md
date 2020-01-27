# ロボットシステム学　課題2
 **概要**
 
 Raspberry piを用いてLEDを点灯、制御するデバイスドライバ及びプログラム。
 echoコマンドによってLEDを常時点灯及び消灯させます。
 また、timer.shファイルを実行する事で入力した数の秒数点灯し、その後消灯します。
 
# デモ映像
 
URL：https://youtu.be/ygsqqd6A4mg
 
# 要件
### 環境
Raspberry Pi Model 3B   
OS:raspbian

### ピン設定
GPIO25: 22番ピン  
GND: 39番ピン

> アノード22番ピンへ
 カソードを
 39番ピン（GND）へ接続する。  
 長時間点灯させる場合は抵抗（200〜300Ω）を繋ぐ。
 
 
# Installation/Usage
 
    $ git clone https://github.com/umitoto/Task1.git  
> ↑githubよりコードを入手。

    $ cd Task1  
> ↑入手したコードのディレクトリへ移動。

    $ make  
    $ sudo insmod myled.ko
    $ sudo chmod 666 /dev/myled0
> ↑カーネルモジュールをロード。

    $ sh timer.sh
> ↑LEDが入力された数字の秒数点灯する。
    
    $ sudo echo 1 > /dev/myled0
> ↑LEDが点灯する。

    $ sudo echo 0 > /dev/myled0
> ↑LEDが消灯する。

    $ sudo rmmod myled.ko
> ↑カーネルモジュールをアンロード。
 
# Licenses
This is under [GNU license]<http://www.gnu.org/licenses/>.
 
