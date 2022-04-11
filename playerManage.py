#!/usr/bin/python
# -*- coding: utf-8 -*-

from const import PlayerDef, WumpusDef, GoldDef
import random


# 玩家类
class Player(object):
    def __init__(self, storage):
        self.x = 0
        self.y = 0
        self.status = PlayerDef.StatusAlive
        self.point = 0
        self.mov = [[0, 0]]
        self.direction = PlayerDef.DirectionRight
        self.storage = storage

    # 上移
    def moveUp(self):
        if self.status == PlayerDef.StatusAlive:
            self.point -= 1
            self.y -= 100
            k = [self.x, self.y]
            self.direction = PlayerDef.DirectionUp
            self.mov.append(k)

    # 下移
    def moveDown(self):
        if self.status == PlayerDef.StatusAlive:
            self.point -= 1
            self.y += 100
            k = [self.x, self.y]
            self.direction = PlayerDef.DirectionDown
            self.mov.append(k)

    # 右移
    def moveRight(self):
        if self.status == PlayerDef.StatusAlive:
            self.point -= 1
            self.x += 100
            k = [self.x, self.y]
            self.direction = PlayerDef.DirectionRight
            self.mov.append(k)

    # 左移
    def moveLeft(self):
        if self.status == PlayerDef.StatusAlive:
            self.point -= 1
            self.x -= 100
            k = [self.x, self.y]
            self.direction = PlayerDef.DirectionLeft
            self.mov.append(k)

    # 死亡
    def die(self, wumpus, abysses):
        for i in self.mov:
            if i == wumpus.pos and wumpus.status == WumpusDef.StatusAlive:
                if self.status == PlayerDef.StatusAlive:
                    self.point -= 10
                    self.status = PlayerDef.StatusDie
                    return 1
            if i in abysses.local:
                if self.status == PlayerDef.StatusAlive:
                    self.point -= 10
                    self.status = PlayerDef.StatusDie
                    return 2
        return 0

    # 胜利
    def win(self, wumpus, gold):
        # 找到宝藏并回到起点
        if self.mov[-1] == [0, 0] and gold.status == GoldDef.StatusMiss:
            self.point += 100
            if wumpus.status == WumpusDef.StatusDie:
                self.point += 100
            self.saveData()
            return 1
        return 0

    # 保存数据
    def saveData(self):
        self.storage.saveDB(self.point, self.mov)


# 怪物类
class Wumpus(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.status = WumpusDef.StatusAlive
        self.pos = []

    # 生成怪物
    def genWumpus(self):
        self.pos = [random.randrange(100, self.height, 100), random.randrange(100, self.width, 100)]


# 陷阱类
class Abysses(object):
    def __init__(self, size, height, width):
        self.local = []
        self.size = size
        self.height = height
        self.width = width

    # 生成陷阱
    def genAbysses(self):
        count = ((self.size ** 2) * 0.15) - 1
        if count < 2:
            count = 2
        while len(self.local) <= count:
            p = random.randrange(0, self.height, 200)
            q = random.randrange(100, self.width, 200)
            z = [p, q]
            if z not in self.local:
                self.local.append(z)


# 射击类
class Shutting(object):
    def __init__(self):
        self.threw = []
        self.count = 1
        self.scope = 1000

    # 计算射出路线
    def calculateThrew(self, wumpus, abysses, player):
        if self.count > 0:
            player.point -= 1
            self.count -= 1
            self.threw = []
            if player.direction == PlayerDef.DirectionDown:
                for i in range(player.mov[-1][1], player.mov[-1][1] + self.scope, 100):
                    pos = [player.mov[-1][0], i]
                    hit = self.verifyThrew(pos, wumpus, abysses, player)
                    if hit == 0:
                        self.threw.append(pos)
                    else:
                        return hit
            elif player.direction == PlayerDef.DirectionRight:
                for i in range(player.mov[-1][0], player.mov[-1][0] + self.scope, 100):
                    pos = [i, player.mov[-1][1]]
                    hit = self.verifyThrew(pos, wumpus, abysses, player)
                    if hit == 0:
                        self.threw.append(pos)
                    else:
                        return hit
            elif player.direction == PlayerDef.DirectionLeft:
                for i in range(player.mov[-1][0], player.mov[-1][0] - self.scope, -100):
                    pos = [i, player.mov[-1][1]]
                    hit = self.verifyThrew(pos, wumpus, abysses, player)
                    if hit == 0:
                        self.threw.append(pos)
                    else:
                        return hit
            elif player.direction == PlayerDef.DirectionUp:
                for i in range(player.mov[-1][1], player.mov[-1][1] - self.scope, -100):
                    pos = [player.mov[-1][0], i]
                    hit = self.verifyThrew(pos, wumpus, abysses, player)
                    if hit == 0:
                        self.threw.append(pos)
                    else:
                        return hit
            return 0

    # 验证射中
    def verifyThrew(self, pos, wumpus, abysses, player):
        if pos == wumpus.pos and wumpus.status == WumpusDef.StatusAlive:
            wumpus.status = WumpusDef.StatusDie
            player.point += 100
            return 1
        elif pos in abysses.local:
            return 2
        return 0


# 金子类
class Gold(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.status = GoldDef.StatusUnMiss
        self.pos = []

    # 生成金子
    def genGold(self):
        self.pos = [random.randrange(100, self.height, 100), random.randrange(100, self.width, 100)]

    # 捡到金子
    def missGold(self, player):
        if self.pos in player.mov:
            if self.status == GoldDef.StatusUnMiss:
                player.point += 1000
            self.status = GoldDef.StatusMiss
            return 1
        return 0

