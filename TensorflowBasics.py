#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 14:10:15 2018
@author: dilekcelik
"""

import tensorflow as tf

W = tf.Variable(tf.zeros((2,2)), name="weights")
R = tf.Variable(tf.random_normal((2,2)), name="random_weights")

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(W))
    print(sess.run(R))

