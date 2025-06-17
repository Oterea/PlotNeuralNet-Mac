import sys

sys.path.append('../')
from pycore.tikzeng import *

width_scale = 4
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 64, 16, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=16 / width_scale),

    # to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 32, 32, offset="(5,0,0)", to="(conv1-east)", height=32, depth=32, width=32 / width_scale),
    to_connection("conv1", "conv2"),
    to_Conv("conv3", 16, 64, offset="(3,0,0)", to="(conv2-east)", height=16, depth=16, width=64 / width_scale),
    to_Conv("conv4", 8, 128, offset="(3,0,0)", to="(conv3-east)", height=8, depth=8, width=128 / width_scale),
    to_Conv("conv5", 4, 128, offset="(3,0,0)", to="(conv4-east)", height=4, depth=4, width=128 / width_scale),
    # to_connection("pool1", "conv2"),
    # to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    # to_SoftMax("soft1", 10, "(3,0,0)", "(pool1-east)", caption="SOFT"),
    # to_connection("pool2", "soft1"),
    # to_Sum("sum1", offset="(1.5,0,0)", to="(soft1-east)", radius=2.5, opacity=0.6),
    # to_connection("soft1", "sum1"),
    to_end()
]

if __name__ == '__main__':
    filename = os.path.basename(__file__).split('.')[0]  # 由于直接使用脚本运行，直接获取文件名更为合适

    to_generate(arch, filename + '.tex')

    os.system('pdflatex ' + filename + '.tex')  # 调用命令行，使用pdflatex命令，将tex生成为pdf
    os.remove(filename + '.log')  # 删除多余中间文件
    os.remove(filename + '.aux')  # 同上
    os.remove(filename + '.tex')  # 同上
