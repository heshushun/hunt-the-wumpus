#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, time

from const import PlayerDef, WumpusDef
from playerManage import Player, Shutting, Wumpus, Gold, Abysses
from storage import Storage

cor = {"branco": (255, 255, 255), "preto": (0, 0, 0), "vermelho": (255, 0, 0), "verde": (0, 255, 0),
       "azul": (0, 255, 255), "azul_escuro": (0, 200, 200), "vermelho_escuro": (200, 0, 0), "verde_escuro": (0, 200, 0),
       "cinza": (124, 124, 124), "cinza_claro": (189, 196, 202), "cinza_escuro": (36, 36, 36)}


# 目录类
class Menu(object):
    def __init__(self, size, height, width, screen):
        self.size = size
        self.height = height
        self.width = width
        self.screen = screen

        self.cor = cor["branco"]
        
        self.source = pygame.font.SysFont("", 30)
        self.sourcePrincipal = pygame.font.SysFont("", 50)
        
        self.logo = pygame.image.load("./assets/logo.png")
        self.imageBackground = pygame.image.load("./assets/terra.png")

    # 背景
    def background(self):
        for i in range(self.size):
            for j in range(self.size + 1):
                x = 100 * i
                y = 100 * j
                self.screen.blit(self.imageBackground, (x, y))

    # 记录
    def records(self):
        Records = self.sourcePrincipal.render("Records", True, cor["preto"])
        posRet = [self.width // 2 - 200, self.height // 2 - 200]

        storageObj = Storage()
        points = storageObj.quiryDB()

        points.sort()
        points = points[::-1]

        points0 = self.source.render("points: " + str(points[0][0]), True, cor["preto"])
        mov0 = self.source.render("movs: " + str(points[0][1]), True, cor["preto"])
        points1 = self.source.render("points: " + str(points[1][0]), True, cor["preto"])
        mov1 = self.source.render("movs: " + str(points[1][1]), True, cor["preto"])
        points2 = self.source.render("points: " + str(points[2][0]), True, cor["preto"])
        mov2 = self.source.render("movs: " + str(points[2][1]), True, cor["preto"])
        points3 = self.source.render("points: " + str(points[3][0]), True, cor["preto"])
        mov3 = self.source.render("movs: " + str(points[3][1]), True, cor["preto"])
        points4 = self.source.render("points: " + str(points[4][0]), True, cor["preto"])
        mov4 = self.source.render("movs: " + str(points[4][1]), True, cor["preto"])

        out = False
        while not out:
            self.background()
            pygame.draw.rect(self.screen, (189, 196, 202), (posRet[0], posRet[1], 400, 400))
            pygame.draw.rect(self.screen, cor["preto"], (posRet[0], posRet[1], 400, 400), 3)

            # 监听键盘事件 esc键退出
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    out = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        out = True

            self.screen.blit(Records, (posRet[0] + 120, posRet[1] + 30))
            self.screen.blit(points0, (posRet[0] + 40, posRet[1] + 100))
            self.screen.blit(mov0, (posRet[0] + 200, posRet[1] + 100))
            self.screen.blit(points1, (posRet[0] + 40, posRet[1] + 150))
            self.screen.blit(mov1, (posRet[0] + 200, posRet[1] + 150))
            self.screen.blit(points2, (posRet[0] + 40, posRet[1] + 200))
            self.screen.blit(mov2, (posRet[0] + 200, posRet[1] + 200))
            self.screen.blit(points3, (posRet[0] + 40, posRet[1] + 250))
            self.screen.blit(mov3, (posRet[0] + 200, posRet[1] + 250))
            self.screen.blit(points4, (posRet[0] + 40, posRet[1] + 300))
            self.screen.blit(mov4, (posRet[0] + 200, posRet[1] + 300))
            pygame.display.update()

    # 目录
    def menu(self):
        self.background()

        iniciar = self.source.render("Start", True, cor["preto"])
        records = self.source.render("Records", True, cor["preto"])
        out = self.source.render("Quit", True, cor["preto"])
        creditos = self.source.render("make in china,  you are beautiful !!!!", True, cor["preto"])

        posIniciar = [self.width // 2 - 165, self.height // 2 + 140]
        posRecords = [self.width // 2 - 55, self.height // 2 + 140]
        posOut = [self.width // 2 + 65, self.height // 2 + 140]
        posCreditos = [self.width // 2 - 215, self.height // 2 + 200]

        quitMenu = False

        while not quitMenu:
            self.screen.blit(self.logo, (self.width // 2 - 200, self.height // 2 - 250))
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitMenu = True
                    return 1

            if posRecords[0] + 110 > mouse[0] > posRecords[0] and posRecords[1] + 40 > mouse[1] > posRecords[1]:
                pygame.draw.rect(self.screen, cor["azul"], (posRecords[0], posRecords[1], 110, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posRecords[0], posRecords[1], 110, 40), 1)
                if clique[0] == 1:
                    self.records()
                    self.background()
            else:
                pygame.draw.rect(self.screen, cor["azul_escuro"], (posRecords[0], posRecords[1], 110, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posRecords[0], posRecords[1], 110, 40), 1)

            if posIniciar[0] + 100 > mouse[0] > posIniciar[0] and posIniciar[1] + 40 > mouse[1] > posIniciar[1]:
                pygame.draw.rect(self.screen, cor["verde"], (posIniciar[0], posIniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posIniciar[0], posIniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    # todo 进行游戏
                    StartGame(self.size, self.width, self.height)
            else:
                pygame.draw.rect(self.screen, cor["verde_escuro"], (posIniciar[0], posIniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posIniciar[0], posIniciar[1], 100, 40), 1)

            if posOut[0] + 100 > mouse[0] > posOut[0] and posOut[1] + 40 > mouse[1] > posOut[1]:
                pygame.draw.rect(self.screen, cor["vermelho"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)
                if clique[0] == 1:
                    quitMenu = True
                    return 1
            else:
                pygame.draw.rect(self.screen, cor["vermelho_escuro"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)

            pygame.draw.rect(self.screen, cor["branco"], (posCreditos[0], posCreditos[1], 435, 40))
            self.screen.blit(creditos, (posCreditos[0] + 20, posCreditos[1] + 10))
            self.screen.blit(iniciar, (posIniciar[0] + 20, posIniciar[1] + 10))
            self.screen.blit(records, (posRecords[0] + 10, posRecords[1] + 10))
            self.screen.blit(out, (posOut[0] + 30, posOut[1] + 10))
            pygame.display.update()


# 地图类
class Map(object):
    def __init__(self, size, height, width, screen):
        self.size = size
        self.height = height
        self.width = width
        self.screen = screen

        self.statusObj = None
        self.player = None
        self.gold = None
        self.wumpus = None
        self.shutting = None
        self.abysses = None
        
        self.terra = pygame.image.load("./assets/terra.png")
        self.gram = pygame.image.load("./assets/grama.png")
        self.playerImage = pygame.image.load("./assets/jogadorComFlecha.png")
        self.abismo = pygame.image.load("./assets/abismo.png")
        self.vento = pygame.image.load("./assets/vento.png")
        self.wumpusImage = pygame.image.load("./assets/wumpus.png")
        self.pegadas = pygame.image.load("./assets/pegadas.png")
        self.shutImage = pygame.image.load("./assets/flecha.png")
        self.ouro = pygame.image.load("./assets/ouro.png")
        self.brilho = pygame.image.load("./assets/brilho.png")

        self.playerDisplay = self.playerImage
        self.shutDisplay = self.shutImage

    # 数据初始化
    def init(self, statusObj, player, gold, wumpus, shutting, abysses):
        self.statusObj = statusObj
        self.player = player
        self.gold = gold
        self.wumpus = wumpus
        self.shutting = shutting
        self.abysses = abysses

    # 展示地图
    def displayMap(self):
        for i in range(self.size):
            for j in range(self.size):
                x = 100 * i
                y = 100 * j
                k = [x, y]
                self.screen.blit(self.terra, (x, y))
                if x == 0 and y == 0 or k in self.player.mov:
                    self.screen.blit(self.gram, (x, y))

    # 更换形象
    def changeImage(self):
        if self.shutting.count <= 0:
            self.playerImage = pygame.image.load("./assets/jogadorSemFlecha.png")

    # 上移
    def moveUp(self):
        if self.player.status == PlayerDef.StatusAlive:
            self.player.moveUp()
            self.playerDisplay = pygame.transform.rotate(self.playerImage, 90)
            self.shutDisplay = pygame.transform.rotate(self.shutImage, 90)

    # 下移
    def moveDown(self):
        if self.player.status == PlayerDef.StatusAlive:
            self.player.moveDown()
            self.playerDisplay = pygame.transform.rotate(self.playerImage, -90)
            self.shutDisplay = pygame.transform.rotate(self.shutImage, - 90)

    # 右移
    def moveRight(self):
        if self.player.status == PlayerDef.StatusAlive:
            self.player.moveRight()
            self.playerDisplay = self.playerImage
            self.shutDisplay = self.shutImage

    # 左移
    def moveLeft(self):
        if self.player.status == PlayerDef.StatusAlive:
            self.player.moveLeft()
            self.playerDisplay = pygame.transform.flip(self.playerImage, True, False)
            self.shutDisplay = pygame.transform.flip(self.shutImage, True, False)

    # 死亡
    def die(self):
        flag = self.player.die(self.wumpus, self.abysses)
        if flag == 1:
            self.statusObj.msg = "Miss Wumpus!"
            self.statusObj.reset()
            pygame.display.update()
            dieOut = self.statusObj.dieTip()
            if dieOut == 1:
                return 1
        elif flag == 2:
            self.statusObj.msg = "Miss Abyss!"
            self.statusObj.reset()
            pygame.display.update()
            dieOut = self.statusObj.dieTip()
            if dieOut == 1:
                return 1
        return 0

    # 胜利
    def win(self):
        if self.player.win(self.wumpus, self.gold) == 1:
            self.statusObj.msg = "Had found gold!"
            self.statusObj.reset()
            pygame.display.update()
            vitoria = self.statusObj.winTip()
            if vitoria == 1:
                return 1
        return 0

    # 展示陷阱
    def displayAbysses(self):
        for i in self.abysses.local:
            if i in self.player.mov:
                self.screen.blit(self.abismo, (i[0], i[1]))

    # 展示风
    def displayWind(self):
        for i in self.abysses.local:
            posVento = [[i[0] + 100, i[1]], [i[0] - 100, i[1]], [i[0], i[1] + 100], [i[0], i[1] - 100]]
            for i in posVento:
                if i in self.player.mov:
                    self.screen.blit(self.vento, (i[0], i[1]))

    # 展示怪物
    def displayWumpus(self):
        if self.wumpus.pos in self.player.mov and self.wumpus.status == WumpusDef.StatusAlive:
            self.screen.blit(self.wumpusImage, (self.wumpus.pos[0], self.wumpus.pos[1]))

    # 展示脚丫
    def displayFootprints(self):
        posPegadas = [[self.wumpus.pos[0] + 100, self.wumpus.pos[1]], [self.wumpus.pos[0] - 100, self.wumpus.pos[1]],
                      [self.wumpus.pos[0], self.wumpus.pos[1] + 100], [self.wumpus.pos[0], self.wumpus.pos[1] - 100]]
        for i in posPegadas:
            if i in self.player.mov:
                self.screen.blit(self.pegadas, (i[0], i[1]))

    # 计算射出路线
    def calculateThrew(self):
        if self.shutting.count > 0:
            hit = self.shutting.calculateThrew(self.wumpus, self.abysses, self.player)
            self.verifyThrewView(hit)
            self.displayThrew()
            self.changeImage()
        else:
            self.statusObj.msg = "No bang shut !!!"
            self.screen.blit(self.playerDisplay, (self.player.x, self.player.y))
            pygame.display.update()

    # 展示射出路线
    def displayThrew(self):
        for i in self.shutting.threw:
            time.sleep(0.03)
            self.displayMap()
            self.displayGoldFlash()
            self.displayGold()
            self.displayAbysses()
            self.displayWind()
            self.displayWumpus()
            self.displayFootprints()
            self.screen.blit(self.playerDisplay, (self.player.x, self.player.y))
            self.screen.blit(self.shutImage, (i[0], i[1]))
            self.statusObj.reset()
            pygame.display.update()

    # 验证射中展示
    def verifyThrewView(self, hit):
        if hit == 1:
            self.statusObj.msg = "Your arrow hit the Wumpus!"
            self.statusObj.reset()
            pygame.display.update()
        elif hit == 2:
            self.statusObj.msg = "Your arrow fell into the abyss!"
            self.statusObj.reset()
            pygame.display.update()

    # 展示金子
    def displayGold(self):
        if self.gold.missGold(self.player) == 1:
            self.screen.blit(self.ouro, (self.gold.pos[0], self.gold.pos[1]))
            self.statusObj.msg = "Has Gold !!!"

    # 展示闪耀金光
    def displayGoldFlash(self):
        posFlash = [[self.gold.pos[0] + 100, self.gold.pos[1]], [self.gold.pos[0] - 100, self.gold.pos[1]],
                     [self.gold.pos[0], self.gold.pos[1] + 100], [self.gold.pos[0], self.gold.pos[1] - 100]]
        for i in posFlash:
            if i in self.player.mov:
                self.screen.blit(self.brilho, (i[0], i[1]))


# 状态提示类
class Status(object):
    def __init__(self, size, height, width, screen):
        self.size = size
        self.height = height
        self.width = width
        self.screen = screen

        self.player = None
        self.gold = None
        self.wumpus = None
        self.shutting = None
        self.abysses = None

        self.source = pygame.font.SysFont("", 30)
        self.sourceAviso = pygame.font.SysFont("", 70)
        self.cor = cor["branco"]
        self.msg = "Welcome to the world of Wumpus"

    # 数据初始化
    def init(self, player, gold, wumpus, shutting, abysses):
        self.player = player
        self.gold = gold
        self.wumpus = wumpus
        self.shutting = shutting
        self.abysses = abysses

    # 绘制
    def painting(self):
        pygame.draw.rect(self.screen, cor["cinza_escuro"], (0, self.height - 100, self.width, 100))
        pygame.draw.rect(self.screen, cor["preto"], (0, self.height - 100, self.width, 100), 3)
        pygame.draw.rect(self.screen, cor["branco"], (10, self.height - 40, self.width - 20, 30))
        pygame.draw.rect(self.screen, cor["preto"], (10, self.height - 40, self.width - 20, 30), 3)

    # 分数提示
    def pointsTip(self):
        string = self.source.render("points: " + str(self.player.point), True, self.cor)
        self.screen.blit(string, (15, self.height - 90))

    # 方向提示
    def directionTip(self):
        texto = "Direction: " + self.player.direction
        string = self.source.render(texto, True, self.cor)
        self.screen.blit(string, (self.width // 2 - 50, self.height - 90))

    # 怪物提示
    def wumpusTip(self):
        texto = "Wumpus: " + self.wumpus.status
        string = self.source.render(texto, True, self.cor)
        self.screen.blit(string, (self.width // 2 - 50, self.height - 70))

    # 金币提示
    def goldTip(self):
        string = self.source.render("Gold: " + self.gold.status, True, self.cor)
        self.screen.blit(string, (15, self.height - 70))

    # 射击数量提示
    def shuttingTip(self):
        string = self.source.render("Shutting: " + str(self.shutting.count), True, self.cor)
        self.screen.blit(string, (self.width - 115, self.height - 90))

    # 信息提示
    def infoTip(self):
        string = self.source.render(self.msg, True, cor["preto"])
        self.screen.blit(string, (15, self.height - 35))

    # 重置
    def reset(self):
        self.painting()
        self.pointsTip()
        self.wumpusTip()
        self.infoTip()
        self.goldTip()
        self.directionTip()
        self.shuttingTip()

    # 死亡提示
    def dieTip(self):
        aviso = self.sourceAviso.render("You Die Out!", True, cor["preto"])
        reiniciar = self.source.render("Restart", True, cor["preto"])
        out = self.source.render("Out", True, cor["preto"])

        posReiniciar = [self.width // 2 - 125, self.height // 2 - 50]
        posOut = [self.width // 2 + 20, self.height // 2 - 50]
        outAviso = False

        while outAviso != True:
            pygame.draw.rect(self.screen, (189, 196, 202), (self.width // 2 - 170, self.height // 2 - 150, 340, 160))
            pygame.draw.rect(self.screen, cor["preto"], (self.width // 2 - 170, self.height // 2 - 150, 340, 160), 3)
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    outAviso = True

            if posReiniciar[0] + 100 > mouse[0] > posReiniciar[0] and posReiniciar[1] + 40 > mouse[1] > posReiniciar[1]:
                pygame.draw.rect(self.screen, cor["verde"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    # todo 重开
                    StartGame(self.size, self.width, self.height)
            else:
                pygame.draw.rect(self.screen, cor["verde_escuro"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)

            if posOut[0] + 100 > mouse[0] > posOut[0] and posOut[1] + 40 > mouse[1] > posOut[1]:
                pygame.draw.rect(self.screen, cor["vermelho"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)
                if clique[0] == 1:
                    outAviso = True
            else:
                pygame.draw.rect(self.screen, cor["vermelho_escuro"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)

            self.screen.blit(aviso, (self.width // 2 - 155, self.height // 2 - 120))
            self.screen.blit(reiniciar, (posReiniciar[0] + 5, posReiniciar[1] + 10))
            self.screen.blit(out, (posOut[0] + 30, posOut[1] + 10))
            pygame.display.update()
        return 1

    # 暂停提示
    def pauseTip(self):
        aviso = self.sourceAviso.render("Pause", True, cor["preto"])
        reiniciar = self.source.render("Restart", True, cor["preto"])
        continuar = self.source.render("Continue", True, cor["preto"])
        out = self.source.render("Out", True, cor["preto"])

        posContinuar = [self.width // 2 - 55, self.height // 2 - 50]
        posReiniciar = [self.width // 2 - 165, self.height // 2 - 50]
        posOut = [self.width // 2 + 65, self.height // 2 - 50]

        outPausa = False

        while outPausa != True:
            pygame.draw.rect(self.screen, (189, 196, 202), (self.width // 2 - 180, self.height // 2 - 150, 360, 160))
            pygame.draw.rect(self.screen, cor["preto"], (self.width // 2 - 180, self.height // 2 - 150, 360, 160), 3)
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    outPausa = True
                    return 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        outPausa = True
                    return 0

            if posContinuar[0] + 110 > mouse[0] > posContinuar[0] and posContinuar[1] + 40 > mouse[1] > posContinuar[1]:
                pygame.draw.rect(self.screen, cor["azul"], (posContinuar[0], posContinuar[1], 110, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posContinuar[0], posContinuar[1], 110, 40), 1)
                if clique[0] == 1:
                    outPausa = True
                    return 0
            else:
                pygame.draw.rect(self.screen, cor["azul_escuro"], (posContinuar[0], posContinuar[1], 110, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posContinuar[0], posContinuar[1], 110, 40), 1)

            if posReiniciar[0] + 100 > mouse[0] > posReiniciar[0] and posReiniciar[1] + 40 > mouse[1] > posReiniciar[1]:
                pygame.draw.rect(self.screen, cor["verde"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    # todo 重开
                    StartGame(self.size, self.width, self.height)
            else:
                pygame.draw.rect(self.screen, cor["verde_escuro"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)

            if posOut[0] + 100 > mouse[0] > posOut[0] and posOut[1] + 40 > mouse[1] > posOut[1]:
                pygame.draw.rect(self.screen, cor["vermelho"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)
                if clique[0] == 1:
                    outPausa = True
                    return 1
            else:
                pygame.draw.rect(self.screen, cor["vermelho_escuro"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)

            self.screen.blit(aviso, (self.width // 2 - 70, self.height // 2 - 120))
            self.screen.blit(continuar, (posContinuar[0] + 5, posContinuar[1] + 10))
            self.screen.blit(reiniciar, (posReiniciar[0] + 5, posReiniciar[1] + 10))
            self.screen.blit(out, (posOut[0] + 30, posOut[1] + 10))
            pygame.display.update()

    # 胜利提示
    def winTip(self):
        aviso = self.sourceAviso.render("You Win!", True, cor["preto"])
        points = self.source.render("Points: " + str(self.player.point), True, cor["preto"])
        movs = self.source.render("Movs: " + str(len(self.player.mov)), True, cor["preto"])
        wumpusStatus = self.source.render("Wumpus: " + self.wumpus.status, True, cor["preto"])
        ouroStatus = self.source.render("Gold: " + self.gold.status, True, cor["preto"])
        reiniciar = self.source.render("Restart", True, cor["preto"])
        out = self.source.render("Out", True, cor["preto"])

        posReiniciar = [self.width // 2 - 125, self.height // 2 + 30]
        posOut = [self.width // 2 + 20, self.height // 2 + 30]
        outVitoria = False

        while outVitoria != True:
            pygame.draw.rect(self.screen, cor["cinza_claro"], (self.width // 2 - 170, self.height // 2 - 150, 340, 250))
            pygame.draw.rect(self.screen, cor["preto"], (self.width // 2 - 170, self.height // 2 - 150, 340, 250), 3)
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    outVitoria = True

            if posReiniciar[0] + 100 > mouse[0] > posReiniciar[0] and posReiniciar[1] + 40 > mouse[1] > posReiniciar[1]:
                pygame.draw.rect(self.screen, cor["verde"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    # todo 重开
                    StartGame(self.size, self.width, self.height)
            else:
                pygame.draw.rect(self.screen, cor["verde_escuro"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)

            if posOut[0] + 100 > mouse[0] > posOut[0] and posOut[1] + 40 > mouse[1] > posOut[1]:
                pygame.draw.rect(self.screen, cor["vermelho"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)
                if clique[0] == 1:
                    outVitoria = True
            else:
                pygame.draw.rect(self.screen, cor["vermelho_escuro"], (posOut[0], posOut[1], 100, 40))
                pygame.draw.rect(self.screen, cor["preto"], (posOut[0], posOut[1], 100, 40), 1)

            self.screen.blit(aviso, (self.width // 2 - 160, self.height // 2 - 120))
            self.screen.blit(points, (self.width // 2 - 160, self.height // 2 - 50))
            self.screen.blit(movs, (self.width // 2 - 160, self.height // 2 - 30))
            self.screen.blit(wumpusStatus, (self.width // 2 + 5, self.height // 2 - 50))
            self.screen.blit(ouroStatus, (self.width // 2 + 5, self.height // 2 - 30))
            self.screen.blit(reiniciar, (posReiniciar[0] + 5, posReiniciar[1] + 10))
            self.screen.blit(out, (posOut[0] + 30, posOut[1] + 10))
            pygame.display.update()
        return 1


def StartGame(size, width, height):
    screen = pygame.display.set_mode([width, height])

    storageObj = Storage()
    playerObj = Player(storageObj)
    shuttingObj = Shutting()
    wumpusObj = Wumpus(height, width)
    goldObj = Gold(height, width)
    abyssesObj = Abysses(size, height, width)

    # 随机生成布局
    wumpusObj.genWumpus()
    goldObj.genGold()
    abyssesObj.genAbysses()

    statusObj = Status(size, height, width, screen)
    mapObj = Map(size, height, width, screen)

    # 初始化
    statusObj.init(playerObj, goldObj, wumpusObj, shuttingObj, abyssesObj)
    mapObj.init(statusObj, playerObj, goldObj, wumpusObj, shuttingObj, abyssesObj)

    # 构建游戏开始
    game(statusObj, mapObj, playerObj, size, width, height, screen)


def game(statusObj, mapObj, playerObj, size, width, height, screen):
    keys = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_f, pygame.K_p, pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]
    out = False
    while not out:
        # 处理摁键事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out = True
            if event.type == pygame.KEYDOWN:
                if event.key not in keys:
                    statusObj.msg = "click key error!!!"
                else:
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if playerObj.y < (height - 200):
                            mapObj.moveDown()
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if playerObj.y >= 100:
                            mapObj.moveUp()
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if playerObj.x < (width - 100):
                            mapObj.moveRight()
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if playerObj.x >= 100:
                            mapObj.moveLeft()

                    if event.key == pygame.K_f:
                        mapObj.calculateThrew()

                    if event.key == pygame.K_p:
                        pausa = statusObj.pauseTip()
                        if pausa == 1:
                            out = True

        mapObj.displayMap()
        mapObj.displayGoldFlash()
        mapObj.displayGold()
        mapObj.displayWind()
        mapObj.displayAbysses()
        mapObj.displayWumpus()
        mapObj.displayFootprints()
        screen.blit(mapObj.playerDisplay, (playerObj.x, playerObj.y))
        statusObj.reset()

        die = mapObj.die()
        if die == 1:
            out = True
        win = mapObj.win()
        if win == 1:
            out = True
        pygame.display.update()
    menu = Menu(size, height, width, screen)
    menu.background()
