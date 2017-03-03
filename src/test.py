#! /usr/bin/python#
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/21 18:21:41$"

def pi(num):
    return num * 3.14


list =[nums for nums in range(1,11)]
for ans in map(pi,list):
    print(ans)
