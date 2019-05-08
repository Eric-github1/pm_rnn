# -*- coding: utf-8 -*-
# https://blog.csdn.net/zhongzhongzhen/article/details/79303858?utm_source=blogxgwz7 岁月如歌
import tensorflow as tf
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_float(
    'flag_float',0.01,'input a float'
)
tf.app.flags.DEFINE_integer(
    'flag_int',400,'input a int'
)
tf.app.flags.DEFINE_string(
    'flag_string',"wang","input a string"
)
# print(FLAGS)

print(FLAGS.flag_float)


# 运行结果
# (tf-gpu) eric@eric-Y480:~/workspace/pyth_and_dl/pm_rnn/mytutorial$ python learn_flags.py
# 0.01

# (tf-gpu) eric@eric-Y480:~/workspace/pyth_and_dl/pm_rnn/mytutorial$ python learn_flags.py -h
# Traceback (most recent call last):
#   File "learn_flags.py", line 13, in <module>
#     print(FLAGS.flag_float)
#   File "/home/eric/anaconda3/envs/tf-gpu/lib/python3.6/site-packages/tensorflow/python/platform/flags.py", line 84, in __getattr__
#     wrapped(_sys.argv)
#   File "/home/eric/anaconda3/envs/tf-gpu/lib/python3.6/site-packages/absl/flags/_flagvalues.py", line 632, in __call__
#     name, value, suggestions=suggestions)
# absl.flags._exceptions.UnrecognizedFlagError: Unknown command line flag 'h'

# 运行结果2
# (tf-gpu) eric@eric-Y480:~/workspace/pyth_and_dl/pm_rnn/mytutorial$ python learn_flags.py --flag_float 0.1
# 0.1
