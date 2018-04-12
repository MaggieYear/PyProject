#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Role:

    """
    角色类
    卧底
    平民
    """
    def __init__(self,key_word="",role_id = 0):
        self.key_word = key_word
        self.role_id = role_id  #平民-0；卧底-1；

class User(Role):
    """
    用户类
    玩家
    """
    def __init__(self,id,role_id):
        self.id = id  #玩家id
        self.role_id = role_id

