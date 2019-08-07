from PIL import Image, ImageFont

from handright import Template, handwrite

text = "我能吞下玻璃而不伤身体。"
template = Template(
    background=Image.new(mode="1", size=(1024, 2048), color=1),
    font_size=100,
    font=ImageFont.truetype("path/to/my/font.ttf"),
)
for image in handwrite(text, template):
    image.show()