from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as et

# 语法匹配规则：^[备注内容](标注文字)
REMARK_PATTERN = r"\^(\[.*?\])(\(.*?\))"

class PinyinRemarkExtension(Extension):
    def extendMarkdown(self, md):
        # 注册解析器：匹配到语法时，调用 PinyinRemarkInlineProcessor 处理
        md.inlinePatterns.register(
            PinyinRemarkInlineProcessor(REMARK_PATTERN, md),
            "pinyin_remark",  # 扩展名称（避免与旧版冲突）
            175,              # 优先级（高于普通链接、强调等）
        )

class PinyinRemarkInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        # 解析语法：拆分「备注内容」和「标注文字」
        remark_text = m.group(1).strip("[]")  # 提取 [备注内容]
        label_text = m.group(2).strip("()")   # 提取 (标注文字)
        
        # 构建 HTML 结构：用 div 包裹备注和文字，实现类似拼音的垂直布局
        container = et.Element("span")  # 外层容器（保持行内元素）
        container.set("class", "pinyin-container")
        
        # 备注（上）
        remark_span = et.Element("span")
        remark_span.set("class", "pinyin-remark")
        remark_span.text = remark_text
        
        # 标注文字（下）
        label_span = et.Element("span")
        label_span.set("class", "pinyin-label")
        label_span.text = label_text
        
        # 将备注和文字添加到容器中
        container.append(remark_span)
        container.append(label_span)
        
        return container, m.start(0), m.end(0)

def makeExtension(**kwargs):
    return PinyinRemarkExtension(**kwargs)