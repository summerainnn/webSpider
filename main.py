import requests_html
import json

baseUrl = "http://cs.hitsz.edu.cn/szll/qzjs"

session = requests_html.HTMLSession()


'''
'#line_u8_0 > div.teacher-box > dl:nth-child(1) > dd' 任职
'#line_u8_0 > div.teacher-box > dl:nth-child(2) > dd' 电话
'#line_u8_0 > div.teacher-box > dl:nth-child(3) > dd' 传真
'#line_u8_0 > div.teacher-box > dl:nth-child(4) > dd > a' email
'#line_u8_0 > div.teacher-box > dl:nth-child(5) > dd' 研究方向
'#line_u8_0 > div.teacher-box > a' 简历地址
'''
# print(list(data.links)[0])

dataList = []
for i in range(1, 7):
    for j in range(8):
        if i == 1 and j > 3:
            break
        response = session.get(baseUrl + "/" + str(i) + ".htm")
        if i == 6:
            response = session.get(baseUrl+".htm")
        name = response.html.find('#line_u8_'+str(j)+' > div.teacher-left > p')[0].text
        position = response.html.find('#line_u8_'+str(j)+' > div.teacher-box > dl:nth-child(1) > dd')[0].text
        phone = response.html.find('#line_u8_'+str(j)+' > div.teacher-box > dl:nth-child(2) > dd')[0].text
        fax = response.html.find('#line_u8_'+str(j)+' > div.teacher-box > dl:nth-child(3) > dd')[0].text
        email = response.html.find('#line_u8_'+str(j)+' > div.teacher-box > dl:nth-child(4) > dd > a')[0].text
        field = response.html.find('#line_u8_'+str(j)+' > div.teacher-box > dl:nth-child(5) > dd')[0].text
        resume = response.html.find('#line_u8_'+str(j)+' > div.teacher-box > a')
        resume = str(list(resume[0].links)[0])
        # print(resume)
        resume = resume.replace("../../info", "http://cs.hitsz.edu.cn/info")
        resume = resume.replace("../info", "http://cs.hitsz.edu.cn/info")
        # print(resume)
        data = {}
        data['position'] = position
        data['phone'] = phone
        data['fax'] = fax
        data['email'] = email
        data['field'] = field
        data['resume'] = resume
        data['name'] = name
        dataList.append(data)

with open("result.json", "w") as f:
    f.write(json.dumps(dataList,ensure_ascii=False))

print(len(dataList))
