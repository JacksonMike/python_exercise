class Person(object):
    '''人的类'''
    def __init__(self,name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None #用来保存枪对象的引用
        self.hp = 100
    def installBullet(self,clipTemp,bulletTemp):
        '''把子弹装在弹夹中'''
        #弹夹保存子弹
        clipTemp.bulletStore(bulletTemp)
    def installClip(self,gunTemp,clipTemp):
        '''把弹夹安装在枪中'''
        #枪保存弹夹
        gunTemp.storeClip(clipTemp)
    def holdGun(self,gunTemp):
        '''拿起一把枪'''
        self.gun = gunTemp
    def __str__(self):
        if self.gun:
            return "%s的血量为:%d,他有枪 %s"%(self.name,self.hp,self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为:%d,他没有枪" % (self.name, self.hp)
            else:
                return "%s 已挂..."%self.name

    def useGun(self,enemy):
        '''让枪发射子弹去找敌人'''
        #枪.开火
        self.gun.fire(enemy)
    def loseBlood(self,power):
        '''根据威力掉相应的血量'''
        self.hp -= power

class Gun(object):
    '''枪类'''
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name #用来记录枪的类型
        self.clip = None #用来记录弹夹对象的引用
    def storeClip(self,clip_temp):
        '''用一个属性来保存弹夹对象的引用'''
        self.clip = clip_temp
    def __str__(self):
        if self.clip:
            return "枪的信息为:%s,%s"%(self.name,self.clip)
        else:
            return "枪的信息为:%s,这把枪中没有弹夹"%(self.name)

    def fire(self,enemy):
        '''枪从弹夹中获取一发子弹,然后让一发子弹去击中敌人'''
        #先从弹夹中取出子弹
        #弹夹.弹出一发子弹
        bulletTemp = self.clip.ejectClip()
        #让这个子弹去伤害敌人
        if bulletTemp:
            #子弹.打中敌人
            bulletTemp.shoot(enemy)
        else:
            return "弹夹中没子弹了...."
class Clip(object):
    '''弹夹类'''
    def __init__(self,maxNum):
        super(Clip,self).__init__()
        self.maxNum = maxNum # 用来记录子弹的最大容量
        self.bulletList = [] #用来记录所有子弹的引用
    def bulletStore(self,bulletTemp):
        '''将这颗子弹保存'''
        self.bulletList.append(bulletTemp)
    def __str__(self):
        return "弹夹的信息为:%d/%d"%(len(self.bulletList),self.maxNum)
    def ejectClip(self):
        '''弹出最上面的那颗子弹'''
        if self.bulletList:
            return self.bulletList.pop()
        else:
            return None

class Bullet(object):
    '''子弹对象'''
    def __init__(self,power):
        super(Bullet,self).__init__()
        self.power = power
    def shoot(self,enemy):
        '''让敌人掉血'''
        #敌人.掉血(一颗子弹的威力)
        enemy.loseBlood(self.power)

#老王开枪
def main():
    '''用来控制整个程序的流程'''
    #创建老王对象
    laowang = Person("Jim")
    #创建枪对象
    Barrett = Gun("巴雷特")
    #创建弹夹对象
    clip = Clip(20)
    #创建子弹对象
    for i in range(15):
        bullet = Bullet(20)
        #老王把子弹放进弹夹
        laowang.installBullet(clip,bullet)
    #老王把弹夹放进枪中
    laowang.installClip(Barrett,clip)
    #测试弹夹信息
    print(clip)
    #测试枪的信息
    print(Barrett)
    #老王拿枪
    #测试老王对象
    laowang.holdGun(Barrett)
    print(laowang)
    # 创建敌人对象
    laoSong = Person("Kity")
    print(laoSong)
    #老王开枪打敌人
    laowang.useGun(laoSong)
    print(laowang)
    print(laoSong)
    laowang.useGun(laoSong)
    print(laowang)
    print(laoSong)
    laowang.useGun(laoSong)
    print(laowang)
    print(laoSong)
    laowang.useGun(laoSong)
    print(laowang)
    print(laoSong)
    laowang.useGun(laoSong)
    print(laowang)
    print(laoSong)

if __name__ == "__main__":
    main()
