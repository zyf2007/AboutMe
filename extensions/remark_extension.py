from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as et

# 语法匹配规则："[备注内容](标注文字)
REMARK_PATTERN = r"\"(\[.*?\])(\(.*?\))"

class RemarkExtension(Extension):
    def extendMarkdown(self, md):
        # 注册解析器：匹配到语法时，调用 RemarkInlineProcessor 处理
        md.inlinePatterns.register(
            RemarkInlineProcessor(REMARK_PATTERN, md),
            "remark",  # 扩展名称
            175,       # 优先级（高于普通链接、强调等）
        )

class RemarkInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        # 解析语法：拆分「备注内容」和「标注文字」
        remark_text = m.group(1).strip("[]")  # 提取 [备注内容]
        label_text = m.group(2).strip("()")   # 提取 (标注文字)
        
        # 构建 HTML 结构：用 span 包裹标注文字，通过 data-remark 存备注，配合 CSS 实现悬停
        span = et.Element("span")
        span.set("class", "remark-label")       # 给 CSS 做钩子
        span.set("data-remark", remark_text)   # 存储备注内容（悬停时显示）
        span.text = label_text                  # 标注文字本身
        
        return span, m.start(0), m.end(0)

def makeExtension(**kwargs):
    return RemarkExtension(**kwargs)