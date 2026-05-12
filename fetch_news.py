import feedparser
import urllib.parse
from datetime import datetime, timedelta

# 關鍵字設定 (涵蓋商辦、廠辦、資料中心、標售、上市櫃重訊)
keywords = '("商用不動產" OR "辦公室" OR "商辦" OR "廠辦" OR "資料中心" OR "飯店" OR "旅館" OR "商場" OR "標售" OR "土地買賣" OR "取得不動產" OR "處分不動產")'
query = urllib.parse.quote(f'{keywords} when:1d')
rss_url = f'https://news.google.com/rss/search?q={query}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

def fetch_news():
    feed = feedparser.parse(rss_url)
    items = []
    for entry in feed.entries:
        items.append(f"""
        <div class='card mb-3 shadow-sm'>
            <div class='card-body'>
                <h5 class='card-title'><a href='{entry.link}' target='_blank' style='text-decoration:none; color:#2c3e50;'>{entry.title}</a></h5>
                <p class='card-text'><small class='text-muted'>來源：{entry.source.get('title', '媒體')} | 發布時間：{entry.published}</small></p>
            </div>
        </div>
        """)
    return "".join(items)

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>台灣商用不動產 24H 快訊</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>body {{ background: #f4f7f6; padding-top: 20px; }} .container {{ max-width: 800px; }}</style>
</head>
<body>
    <div class="container">
        <h2 class="text-center mb-4">🏢 台灣商用不動產即時新聞</h2>
        <p class="text-center text-secondary">最後更新 (UTC+8): {(datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')}</p>
        <hr>
        {fetch_news()}
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
