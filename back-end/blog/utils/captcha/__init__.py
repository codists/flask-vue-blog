# @Date: 2021/5/24
# @Author: Hugh
# @Email: 609799548@qq.com

import string
import random

from PIL import Image, ImageDraw, ImageFont


def generate_random(number=4, source=None):
    if source is None:
        source = string.digits
    return ''.join(random.sample(source, number))


class Captcha:
    SOURCE = string.ascii_letters + string.digits

    def __init__(self, image_size=(100, 30), fontsize=25, line_number=2):
        """
        :param image_size: 图形验证码尺寸
        :param fontsize: 图形验证码字体大小
        :param line_number: 图形验证码干扰线条数
        """
        self.image_size = image_size
        self.fontsize = fontsize
        self.line_number = line_number

    @staticmethod
    def __generate_random_color(start=0, end=255):
        """生成随机的颜色"""
        return random.randint(start, end), random.randint(start, end), random.randint(start, end)

    def __generate_line(self, draw, width, height):
        """绘制干扰线"""
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=self.__generate_random_color(), width=2)

    def __generate_points(self, draw, point_chance, width, height):
        """绘制干扰点"""
        chance = min(100, max(0, int(point_chance)))  # 大小限制在 [0, 100]
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=self.__generate_random_color())

    @staticmethod
    def __generate_random_font():
        fonts = [
            'LHANDW.TTF',
            'Lobster-Regular.ttf',
            'verdana.ttf'
        ]
        return 'utils/captcha/font/' + random.choice(fonts)

    def generate_graph_captcha(self, random_number):
        width, height = self.image_size  # 验证码图片的宽和高
        # 创建图片
        # R：Red（红色）0-255
        # G：G（绿色）0-255
        # B：B（蓝色）0-255
        # A：Alpha（透明度）
        image = Image.new('RGBA', (width, height), self.__generate_random_color(0, 100))
        font = ImageFont.truetype(self.__generate_random_font(), self.fontsize)  # 验证码的字体
        draw = ImageDraw.Draw(image)  # 创建画笔
        text = random_number  # 生成字符串
        font_width, font_height = font.getsize(text)  # 获取字体的尺寸
        draw.text(((width - font_width) / 2, (height - font_height) / 2), text, font=font,
                  fill=self.__generate_random_color(150, 255))  # 填充字符
        for _ in range(0, self.line_number):  # 绘制干扰线
            self.__generate_line(draw, width, height)
        self.__generate_points(draw, 10, width, height)  # 绘制干扰点
        return image
