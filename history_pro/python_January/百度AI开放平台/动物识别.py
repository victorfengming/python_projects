from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '15468830'
API_KEY = '95r1wfD7k0Sivj1413qhlH2m'
SECRET_KEY = 'EGckLagIcWSmy3GvQdFesK6hEMl72dRL'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('picture/animal/10.jpg')

""" 调用通用物体识别 """
client.advancedGeneral(image)

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用通用物体识别 """
client.advancedGeneral(image, options)


""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["baike_num"] = 5

""" 带参数调用动物识别 """
result = client.animalDetect(image, options)
print(result)