def define_env(env):

    @env.macro
    def asciinema(cast_file):
        import uuid
        player_id = f"asciinema-player-{uuid.uuid4().hex[:8]}"
        html = """
<html>
<head>
  <link rel="stylesheet" type="text/css" href="https://114514.zroevn.cn/imgs/asciinema-player.css" />
</head>
<body>
  <div id='"""+player_id+"""'></div>
  <script src="https://114514.zroevn.cn/imgs/asciinema-player.min.js"></script>
  <script>
    AsciinemaPlayer.create('"""+cast_file+"""', document.getElementById('"""+player_id+"""'),
    {
        loop: true,
        autoplay: true
    });
  </script>
  <p style="font-size: 14px;margin: 4px 0 0;text-align: right;">
  ♥️ Recorded with <a href="https://asciinema.org/" target="_top">asciinema</a>
</p>
</body>
</html>
"""
        return html



    
    @env.macro
    def music_player(id):
        return f"""
<div class="music-player" id="player-{id}">
    <script>
        (function(){{
        const isMobile = /android|iphone|ipad|ipod|windows phone|blackberry|mobile|tablet/.test(navigator.userAgent.toLowerCase());
        const desktopUrl = "https://music.163.com/outchain/player?type=2&id={id}&auto=0&height=86";
        const mobileUrl = "https://music.163.com/m/outchain/player?type=2&id={id}&auto=0&height=86";
        
        
        const iframeHtml = `<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=${{window.innerWidth}}height=86 src="${{isMobile ? mobileUrl : desktopUrl}}"></iframe>`;
        
        
        document.getElementById('player-{id}').innerHTML = iframeHtml;
        }})()
    </script>
</div>
"""


    @env.macro
    def anime_list(animes):
        """
        生成响应式追番列表
        
        参数:
            animes: 包含番剧信息的列表，每个元素是字典，包含:
                - title: 番剧标题
                - cover: 封面图片URL
                - href: 点击跳转到的链接
                - status: 观看状态(可选)
                - score: 评分(可选)
        """
        # 生成番剧列表HTML
        html = """
<style>
.anime-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1.5rem;
    padding: 1rem 0;
}

.anime-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.anime-card:hover {
    transform: translateY(-5px);
}

.anime-cover {
    width: 100%;
    aspect-ratio: 2/3;
    object-fit: cover;
    display: block;
}

.anime-title {
    padding: 0.75rem;
    font-weight: 600;
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem; /* 默认字体大小 */
}

.anime-meta {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 0 0.75rem 0.75rem;
    font-size: 0.7rem; /* 默认元数据字体大小 */
    color: #666;
}

/* 手机设备适配 - 一行显示3个 */
@media (max-width: 768px) {
    .anime-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 0.75rem;
        padding: 0.5rem;
    }
    
    .anime-title {
        padding: 0.5rem 0.25rem;
        font-size: 0.55rem; /* 手机端标题字体缩小 */
    }
    
    .anime-meta {
        padding: 0 0.25rem 0.5rem;
        font-size: 0.45rem; /* 手机端元数据字体缩小 */
    }
}
</style>

<div class="anime-grid">
        """
        
        # 添加每个番剧卡片
        for anime in animes:
            # 基础卡片内容
            card = f"""
            <div class="anime-card">
                <a href="{anime['href']}">
                <img src="{anime['cover']}" alt="{anime['title']}的封面" class="anime-cover"></a>
                <div class="anime-title">{anime['title']}</div>
            """
            
            # 添加元数据(状态和评分)如果存在
            if 'status' in anime or 'score' in anime:
                card += '<div class="anime-meta">'
                if 'status' in anime:
                    card += f'<span>{anime["status"]}</span>'
                if 'score' in anime:
                    card += f'<span>★ {anime["score"]}</span>'
                card += '</div>'
                
            card += '</div>'
            html += card
        
        html += '</div>'
        return html
