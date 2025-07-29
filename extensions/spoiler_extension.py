from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from xml.etree.ElementTree import Element

# 定义正则表达式匹配 ||隐藏内容|| 格式
SPOILER_RE = r'\|\|(.*?)\|\|'

class SpoilerProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        # 创建 span 元素并添加 spoiler 类
        spoiler = Element('span')
        spoiler.set('class', 'spoiler')
        spoiler.text = m.group(1)  # 获取隐藏的内容
        return spoiler, m.start(0), m.end(0)

class SpoilerExtension(Extension):
    def extendMarkdown(self, md):
        # 注册自定义处理器，优先级为 175（高于普通文本）
        md.inlinePatterns.register(SpoilerProcessor(SPOILER_RE), 'spoiler', 175)

def makeExtension(**kwargs):
    return SpoilerExtension(**kwargs)
