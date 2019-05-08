# https://blog.csdn.net/spring_willow/article/details/80111993

import tensorflow as tf
#取上述代码中一部分进行实验
tf.flags.DEFINE_integer('num_seqs', 100, 'number of seqs in one batch')
tf.flags.DEFINE_integer('num_steps', 100, 'length of one seq')
tf.flags.DEFINE_integer('lstm_size', 128, 'size of hidden state of lstm')

#通过print()确定下面内容的功能
FLAGS = tf.flags.FLAGS #FLAGS保存命令行参数的数据

# FLAGS._parse_flags() #将其解析成字典存储到FLAGS.__flags中  版本问题这个函数么有了

FLAGS.flag_values_dict()
print(FLAGS.__flags)
