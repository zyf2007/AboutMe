export PYTHONPATH=$PYTHONPATH:.

. ./var.sh
LOCAL_DIR="./site"
REMOTE_DIR="/aboutme"

# 构建站点
mkdocs build

echo 清理多余的语言包...
find site/assets/javascripts/lunr/min \
  -type f ! -name 'lunr.zh.min.js' \
           ! -name 'lunr.en.min.js' \
           ! -name 'lunr.multi.min.js' \
           ! -name 'lunr.stemmer.support.min.js' \
  -delete

echo 开始同步文件到 "$FTP_SERVER"...
lftp -u "$FTP_USER","$FTP_PASS" "$FTP_SERVER" <<EOF
set ftp:ssl-allow yes
set ftp:ssl-force yes
set ssl:verify-certificate no

mirror -R --delete \
  --verbose \
  --ignore-time \
  $LOCAL_DIR $REMOTE_DIR

put -O $REMOTE_DIR/assets/images $LOCAL_DIR/assets/images/favicon.png

quit
EOF

echo 正在删除site文件夹
rm -rf ./site
echo 正在将源文件同步到git仓库
git add .
git commit -m "Auto Update"
git push
echo aboutme网站更新完成了喵~
