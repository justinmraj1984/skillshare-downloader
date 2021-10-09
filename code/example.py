from downloader import Downloader

cookie = """
device_session_id=c4e1081a-69ff-4ecb-b4f1-22970c962899; show-like-copy=0; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; __stripe_mid=6f825e99-e2f6-4a47-b255-a74bb62cf4370a93b3; ss_hide_default_banner=1633363624.252; YII_CSRF_TOKEN=MUxXNnZydnVVVktScjBVTllQYU14T2JDRm83anhDcTIWODmN8SxFO7lgT8Tq4OrL-wdHKFy7FXC5h0SoKEMKZg%3D%3D; __stripe_sid=00ff429e-c1b9-4207-a150-6e600ca11e89fe8c61
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
dl.download_course_by_data(1251041283);

