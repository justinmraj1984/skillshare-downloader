from downloader import Downloader

cookie = """
muted=true; device_session_id=7ffe02db-a84b-4ef5-9c16-c361b77dc3d4; show-like-copy=1; visitor_tracking=utm_campaign%3DBrand_EN-ROW%26utm_source%3DGoogle%26utm_medium%3Dpaidsearch%26utm_term%3Dskillshare%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; first_landing=utm_campaign%3DBrand_EN-ROW%26utm_source%3DGoogle%26utm_medium%3Dpaidsearch%26utm_term%3Dskillshare%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; G_ENABLED_IDPS=google; YII_CSRF_TOKEN=ZlB5WTBvTENaTzFFMW5rZ0RvWjFkSXoyMDZVdURzQziNgITNx0UIIUHJXT_fJ768h-Yr8_awzmo3MaIS1UyABQ%3D%3D; __stripe_mid=00ae2334-754c-4138-8fde-22673909786c4376f2; __stripe_sid=ddd2ae75-0f98-48b4-b14c-0f223adce5b06e97b4; G_AUTHUSER_H=0; ss_hide_default_banner=1631509792.363
"""

dl = Downloader(cookie=cookie)

# download by class URL:
# dl.download_course_by_url ('https://www.skillshare.com/classes/Visual-Thinking-Drawing-Data-to-Communicate-Ideas/1746654720')

# or by class ID:
dl.download_course_by_class_id(34882377)
