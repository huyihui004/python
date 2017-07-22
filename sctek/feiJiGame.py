#!/usr/bin/env python
#__*__coding:utf-8__*__
#Author:Jason Zhang
'''这是个飞机大战游戏'''

import time
import random

import pygame
from pygame.locals import *

class BasePlane(object):
    '''飞机基类'''
    def __init__(self, screen, x, y, imagePath):
        #飞机坐标
        self.x=x
        self.y=y
        # 飞机图片
        self.imagepath = imagePath
        self.image = pygame.image.load(self.imagepath)
        # 显示的窗口
        self.screen=screen
        # 子弹列表
        self.bullets=[]

    def display(self):
        '''显示飞机'''
        self.screen.blit(self.image,(self.x,self.y))
        # 用来存放需要删除的对象引用
        needDelItemList = []

        # 绘制所有子弹
        for bullet in self.bullets:
            # 显示一个子弹的位置
            bullet.display()
            # 让这个子弹进行移动，下次再显示的时候就会看到子弹在修改后的位置
            bullet.move()
            # 保存需要删除的对象
            if bullet.judge():
                needDelItemList.append(bullet)

        # 删除需要删除的对象
        for bullet in needDelItemList:
            self.bullets.remove(bullet)

    def moveLeft(self):
        '''向左移动'''
        if self.x>-40:
            self.x -=20

    def moveRight(self):
        '''向右移动'''
        if self.x <420:
            self.x +=20

    def moveUp(self):
        '''向上移动'''
        if self.y >10:
            self.y -=20

    def moveDown(self):
        '''向下移动'''
        if self.y <600:
            self.y +=20


class HeroPlane(BasePlane):
    '''玩家飞机'''
    def __init__(self,screen):
        super(HeroPlane, self).__init__(screen, 190, 550, "./feiji/hero1.png")

    def shoot(self):
        '''发射子弹'''
        bullet = Bullet(self.screen,self.x,self.y)
        self.bullets.append(bullet)

class EnemyPlane(BasePlane):
    '''敌人飞机'''
    def __init__(self,screen):
        super(EnemyPlane, self).__init__(screen, 0, 0, "./feiji/enemy1.png")
        #移动方向
        self.direction = "right"

    #左右移动
    def move(self):
        if self.direction =="right":
            self.x +=3
        elif self.direction =="left":
            self.x -=3

        if self.x >480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"
    
    #随机发射子弹
    def sheBullet(self):
        num=random.randint(1,35)
        if num==8:
            newBullet = EnemyBullet(self.x,self.y,self.screen)
            self.bullets.append(newBullet)

class BaseBullet(object):
    '''子弹基类'''
    def __init__(self,screen, planeX, planeY, imagePath):
        self.x=planeX
        self.y=planeY
        # 创建图片
        self.imagepath = imagePath
        self.image = pygame.image.load(self.imagepath)
        # 使用的窗口
        self.screen = screen

    def display(self):
        '''显示当前子弹'''
        self.screen.blit(self.image,(self.x,self.y))


class Bullet(BaseBullet):
    '''玩家子弹'''
    def __init__(self, screen, planeX, planeY):
        super(Bullet, self).__init__(screen, planeX+40, planeY-20, "./feiji/bullet.png")

    def move(self):
        self.y -=8

    # 判断子弹是否出边间
    def judge(self):
        if self.y<0:
            return True
        else:
            return False

    def __del__(self):
        print("玩家的子弹被销毁了")

class EnemyBullet(BaseBullet):
    '''敌人子弹'''
    def __init__(self,planeX, planeY,screen):
        super(EnemyBullet, self).__init__(screen, planeX+30, planeY+30, "./feiji/bullet1.png")

    def move(self):
        self.y +=3
        
    #判断子弹是否出边间
    def judge(self):
        if self.y>700:
            return True
        else:
            return False

    def __del__(self):
        print("敌人的子弹被销毁了")

def key_control(hero):
    #判断是否是点击了退出按钮
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()

        elif event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                # 控制飞机让其向上移动
                hero.moveUp()

            elif event.key == K_s or event.key == K_DOWN:
                # 控制飞机让其向下移动
                hero.moveDown()

            elif event.key == K_a or event.key == K_LEFT:
                # 控制飞机让其向左移动
                hero.moveLeft()

            elif event.key == K_d or event.key == K_RIGHT:
                #控制飞机让其向右移动
                hero.moveRight()

            elif event.key == K_SPACE:
                #发射子弹
                hero.shoot()


def main():
    # 创建一个新的窗口
    screen = pygame.display.set_mode((480,700),0,32)
    # 创建背景图片
    bg = pygame.image.load("./feiji/background.png")
    # 创建玩家的飞机
    hero = HeroPlane(screen)
    #创建一个敌人飞机
    enemyPlane = EnemyPlane(screen)

    while True:
        # 把背景图片显示到窗口上
        screen.blit(bg,(0,0))
        # 把玩家飞机显示到窗口上
        hero.display()
        # 把敌人飞机显示到窗口上
        enemyPlane.display()
        #敌人飞机自动移动
        enemyPlane.move()
        #敌人飞机自动发射
        enemyPlane.sheBullet()
        #按键事件
        key_control(hero)
        # 刷新界面
        pygame.display.update()
        # 使程序休眠释放资源
        time.sleep(1/200)

if __name__ == "__main__":
    print("程序开始运行")
    main()
    print("程序结束")