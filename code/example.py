from downloader import Downloader

cookie = """
muted=true; device_session_id=89627427-e0b5-469f-ba1c-6e2e6cd69435; show-like-copy=0; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; __stripe_mid=f691fad2-2dba-4b32-b90f-ac7c3b2038c975f39a; g_state={"i_l":0}; ss_hide_default_banner=1632578297.592; _fbp=fb.1.1632684278712.1791162368; YII_CSRF_TOKEN=Z3dnbGNPMzhWbTczUTlVYzBlaE5TNk5WMk1RZG12ZFCgI7Uvqm7eOl6PAoy1NsEvFyLGUmuhl2G2tqjS3epDrA%3D%3D; __stripe_sid=73e628aa-a49e-4b2e-ba43-c67dc61b789aebffc8
"""

dl = Downloader(cookie=cookie)

# OPTION 1: download by class URL:
# dl.download_course_by_url ('https://www.skillshare.com/classes/Writing-production-ready-ETL-pipelines-in-Python-using-Pandas/395128062')

# OPTION 2: download by class ID:
# dl.download_course_by_class_id(1814307821, False)

# OPTION 3: download by skillshare api data:
# Use the class id to construct the below api and execute in the browser
# https://api.skillshare.com/classes/1814307821
# save the api response into a file - 1814307821.json and pass the class id and parameter
dl.download_course_by_data(1814307821);

