# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:32:02 2020

@author: 劉又聖
"""

class Dish:
    """ 儲存一道菜所擁有的資訊 """
    def __init__(self, dish_name, rest_name, tags=[]):
        self.__dish_name = dish_name      # 菜色名稱
        self.__rest_name = rest_name      # 餐廳、店家名稱
        self.__tags      = tags           # 該菜色的標籤
        self.__time      = None           # 餐廳、店家營業時間   使用24小時制
        self.__phone     = None           # 餐廳、店家聯絡方式   可能不止一種
    
    def __contains__(self, tag):
        """ 用於 in operator """
        return self.hasTag(tag)

    def __str__(self):
        result = f"""
        Dish Name       = {self.__dish_name}
        Restaurant Name = {self.__rest_name}
        Type            = {self.__tags}
        """
        return result
    
    def hasTag(self, tag):
        """ Return Bool, 判斷使否有此標籤 """
        return True if tag in self.__tags else False
    
    # Set Function
    def setDishName(self, value):
        """ 設定菜色名稱 """
        self.__dish_name = value
    
    def setRestName(self, value):
        """ 設定餐廳、店家名稱 """
        self.__rest_name = value
    
    def addTag(self, tag):
        """ 新增標籤 """
        if isinstance(tag, (list, tuple)):
            for t in tag:
                if t not in self.__tags:
                    self.__tags.append(t)
        else:
            if tag not in self.__tags:
                self.__tags.append(tag)
    
    # Get Function
    getDishName = lambda self : self.__dish_name
    getRestName = lambda self : self.__rest_name
    getTags     = lambda self : self.__tags
    getAllAttrs = lambda self : [ self.__dish_name, self.__rest_name, self.__tags ]
    
    # Delete Tag
    def __rmSingleTag(self, tag):
        # 找對應的標籤
        idx = 0
        for t in self.__tags:
            if t == tag:
                break
            idx += 1
        # 有找到則刪除且回傳True，沒找到回傳False
        if idx >= len(self.__tags):
            return False
        else:
            self.__tags.pop(idx)
            return True
    
    def rmTag(self, tag):
        """ 移除菜色標籤 """
        if isinstance(tag, (list, tuple)):
            # 一次刪除多個標籤
            del_count = 0
            for del_tag in tag:
                if self.__rmSingleTag(del_tag):
                    del_count += 1
            return del_count
        else:
            # 一次刪除一個標籤
            return self.__rmSingleTag(tag)
