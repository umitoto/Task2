# ロボットシステム学　課題2
 **概要**
 
 Raspberry piにROSを導入し、パブリッシャから送られたコマンドによってサブスクライバがGPIOピンに指令を送り、LEDを点灯及び消灯させるノードを作成しました。
 "1"を送ると点灯し、"0"を送ると消灯します。
 
# デモ映像
 
URL：
 
# 要件
### 環境
Raspberry Pi Model 3B   
OS:Ubuntu Mate 18.04

### ピン設定
GPIO14: 8番ピン  
GND: 6番ピン

> アノード8番ピンへ
 カソードを番ピン（GND）へ接続する。  
 長時間点灯させる場合は抵抗（200〜300Ω）を繋ぐ。
 
 
# Installation/Usage
 
    $ git clone https://github.com/umitoto/Task2.git  
> ↑githubよりコードを入手。

    $ cd Task2/mypkg/scripts/
> ↑入手したコードのディレクトリへ移動。

    $ chmod +x homework_pub.py
    $ chmod +x homework_sub.py
    $ cd ~/catkin_ws
    $ catkin_make 
    $ sourse ~/catkin_ws/devel/setup.bash
    $ roscore 
    $ rosrun mypkg homework_pub.py
    $ rosrun mypkg homework_sub.py
> ↑権限付与とメイク及び実行

    $ command -> 1
> ↑LEDが点灯する。

    $ command -> 0
> ↑LEDが消灯する。

# Licenses
This is under [GNU license]<http://www.gnu.org/licenses/>.
 
