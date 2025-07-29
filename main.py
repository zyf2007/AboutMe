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