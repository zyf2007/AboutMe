// 在 MkDocs 的额外 JS 中添加（如 mkdocs.yml 的 extra_javascript 配置）
document.addEventListener('DOMContentLoaded', function() {
    // 获取所有拼音容器
    const pinyinContainers = document.querySelectorAll('.pinyin-container');
    
    pinyinContainers.forEach(container => {
        const remark = container.querySelector('.pinyin-remark');
        const label = container.querySelector('.pinyin-label');
        
        // 设置备注宽度与下方文字一致
        remark.style.width = `${label.offsetWidth}px`;
    });
});