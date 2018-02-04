import pyqrcode
pic = 'https://www.androidgamesguide.com/wp-content/uploads/2018/01/how-to-play-tabikaeru-travel-frog-from-the-creators-of-neko-atsume.jpg'
url = pyqrcode.create(pic)
url.svg('frog01.svg', scale=8)
url.eps('frog01.eps', scale=8)
url.png('frog01.png', scale=8)

