import requests
import json

sid = input("Please enter account session id: ")
msToken = input("Please enter account msToken: ")
sec_uid = input("Please enter your account sec_uid: ") 

def main():
    global sid
    global msToken
    global sec_uid
    checkurl = "https://api31-core-useast1a.tiktokv.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&filter_private=1&max_cursor=0&sec_user_id={sec_uid}&count=20&iid=7100986988781913861&device_id=7100986933613987334&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=240501&version_name=24.5.1&device_platform=android&ab_version=24.5.1&ssmix=a&device_type=ASUS_Z01QD&device_brand=Asus&language=en&os_api=25&os_version=7.1.2&openudid=33a70a9b89bddd2d&manifest_version_code=2022405010&resolution=1600*900&dpi=300&update_version_code=2022405010&_rticket=1655036346529&current_region=GB&app_type=normal&sys_region=US&mcc_mnc=234234&timezone_name=America%2FChicago&residence=GB&ts=1655036345&timezone_offset=-21600&build_number=24.5.1&region=US&uoo=0&app_language=en&carrier_region=GB&locale=en&op_region=GB&ac2=wifi"
    checkreq = requests.get(checkurl)
    checkjson = dict(json.loads(checkreq.text))
    total = len(checkjson['aweme_list'])
    for i in range(total):
        videolist = (checkjson['aweme_list'][i]['group_id'])
        #print(videolist)
        privurl = f"https://api31-normal-useast1a.tiktokv.com/aweme/v1/aweme/modify/visibility/?aweme_id={videolist}&type=2&device_id=7100986933613987334&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=240501&version_name=24.5.1&device_platform=android&ab_version=24.5.1&ssmix=a&device_type=ASUS_Z01QD&device_brand=Asus&language=en&os_api=25&os_version=7.1.2&openudid=33a70a9b89bddd2d&manifest_version_code=2022405010&resolution=900*1600&dpi=300&update_version_code=2022405010"
        privhed = {
            'cookie': f'msToken={msToken}; sessionid={sid}'}
        privreq = requests.get(privurl, headers=privhed)
        if '"status_code":0' in (privreq.text):
            print(f"Succsesfully Privated video [{videolist}]")
        else:
            print(f"Error occured whilst privating video [{videolist}]")
main()
