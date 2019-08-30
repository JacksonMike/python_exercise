class Person():
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None
        self.hp = 100
    def install_bullet(self,clip_temp,bullet_temp):
        clip_temp.store_bullet(bullet_temp)
    def install_clip(self,gun_temp,clip_temp):
        gun_temp.store_clip(clip_temp)
    def hold_gun(self,gun_temp):
        self.gun = gun_temp
    def __str__(self):
        if self.gun:
            return "%s的血量为%d,他有枪%s"%(self.name,self.hp,self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为%d,他没有枪"%(self.name,self.hp)
            else:
                return "%s已经死去"%self.name
    def use_gun(self,enemy):
        self.gun.fire(enemy)
    def lose_blood(self,power):
        self.hp -= power
class Gun():
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name
        self.clip = None
    def store_clip(self,clip_temp):
        self.clip = clip_temp
    def __str__(self):
        if self.clip:
            return "枪的信息为%s,%s"%(self.name,self.clip)
        else:
            return "枪的信息为%s,这把枪没有弹夹"%(self.name)
    def fire(self,enemy):
        bullet_temp = self.clip.eject_clip()
        if bullet_temp:
            bullet_temp.shoot(enemy)
        else:
            return "弹夹没子弹了"
class Clip():
    def __init__(self,max_num):
        super(Clip,self).__init__()
        self.max_num = max_num
        self.bullet_list = []
    def store_bullet(self,bullet_temp):
        self.bullet_list.append(bullet_temp)
    def __str__(self):
        return "弹夹的信息为%d/%d"%(len(self.bullet_list),self.max_num)
    def eject_clip(self):
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None
class Bullet():
    def __init__(self,power):
        super(Bullet,self).__init__()
        self.power = power
    def shoot(self,enemy):
        enemy.lose_blood(self.power)

def main():
    laowang = Person("Jim")
    Barrett = Gun("巴雷特")
    clip = Clip(20)
    for i in range(15):
        bullet = Bullet(20)
        laowang.install_bullet(clip,bullet)
    laowang.install_clip(Barrett,clip)
    print(Barrett)
    print(clip)
    laowang.hold_gun(Barrett)
    laosong = Person("Kent")
    print(laosong)
    laowang.use_gun(laosong)
    print(laowang)
    print(laosong)

    laowang.use_gun(laosong)
    print(laowang)
    print(laosong)

    laowang.use_gun(laosong)
    print(laowang)
    print(laosong)

    laowang.use_gun(laosong)
    print(laowang)
    print(laosong)

    laowang.use_gun(laosong)
    print(laowang)
    print(laosong)



if __name__ == '__main__':
    main()
