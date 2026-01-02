import json
import os

# 文件路径配置

## 配置保存位置
CONFIG_DIR = os.path.dirname(os.path.adspth(__file__))
## COOKIE保存位置
COOKIE_FILE = os.path.join(CONFIG_DIR, 'cookies.json')
## 数据保存位置
DATA_DIR = os.path.join(CONFIG_DIR, 'data')

# 创建data文件夹, 确保data文件夹存在
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 请求头配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.bilibili.com/',
    'Origin': 'https://www.bilibili.com/',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

# B站API地址
class BiliAPI:
    """B站API接口地址"""
    # 登录相关
    QR_GENERATE = 'https://passport.bilibili.com/x/passport-login/web/qrcode/generate'  # 获取二维码
    QR_POLL = 'https://passport.bilibili.com/x/passport-login/web/qrcode/poll'  # 轮询登录状态
    NAV_INFO = 'https://api.bilibili.com/x/web-interface/nav'  # 获取用户导航信息
    
    # 数据相关
    HISTORY = 'https://api.bilibili.com/x/web-interface/history/cursor'  # 观看历史
    FOLLOW = 'https://api.bilibili.com/x/relation/followings'  # 关注列表
    FAVORITE_LIST = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all'  # 收藏夹列表
    FAVORITE_RESOURCE = 'https://api.bilibili.com/x/v3/fav/resource/list'  # 收藏夹内容
    SPACE_VIDEO = 'https://api.bilibili.com/x/space/wbi/arc/search'  # UP主视频列表

# 获取COOKIES
def load_cookies():
    '''
    从文件中加载COOKIE
    returns: 
        dict: Cookie字典, 如果文件不存在就返回空字典
    '''

    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, 'r', encoding='utf-8') as f :
            return json.load(f)
    return {}

# 保存COOKIE到文件中
def save_cookies(cookies: dict):
    '''
    获取到了cookies, 把他保存在COOKIE_FILE
    args:
        dict: 获取到的cookie字典
    '''
    with open(COOKIE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cookies, f, ensure_ascii=False, indent=2)

# 获取用户的mid
def get_mid():
    '''
    从COOKIE中获取用户的MID
    returns:
        str: 用户的MID, 不存在就返回None
    '''
    cookies = load_cookies()
    return cookies.get('DedeUserID')
