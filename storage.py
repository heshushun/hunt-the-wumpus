#!/usr/bin/python
# -*- coding: utf-8 -*-


# 持久化类
class Storage(object):
    def __init__(self):
        self.fileName = "./assets/points.txt"

    # 读取
    def quiryDB(self):
        points = []
        fileData = open(self.fileName, "r")
        for i in fileData:
            k = i.split()
            g = [int(k[0]), int(k[1])]
            points.append(g)
        fileData.close()
        return points

    # 存
    def saveDB(self, point, mov):
        fileData = open(self.fileName, "r")
        lines = fileData.readlines()
        string = str(point) + " " + str(len(mov)) + "\n"
        lines.append(string)
        fileData = open(self.fileName, "w")
        fileData.writelines(lines)
        fileData.close()