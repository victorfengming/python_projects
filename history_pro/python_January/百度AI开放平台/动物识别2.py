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
wenjianlujing = 'picture/animal/10.jpg'
image = get_file_content(wenjianlujing)
""" 调用通用物体识别 """
result = client.advancedGeneral(image)
print(result)

# print("ellwo")