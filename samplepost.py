import requests
import random,time
import json
import pytest
data=[]
dict={}
url = 'http://dummy.restapiexample.com/api/v1/create'

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
my_list=[]
for i in range(0, 10):
    dict['name'] = str("abc" + str(random.randint(0, 5000)) + "fgh")
    dict['salary'] = str("ghi" + str(random.randint(0, 5000)) + "fgh")
    dict['age'] = str("xyz" + str(random.randint(0, 5000)) + "fgh")
    my_list.append(dict)
    dict={}

@pytest.mark.webtest2
@pytest.mark.parametrize("input_data",my_list)
def test_10cases(input_data):

        x = requests.post(url,headers=headers,data=dict)

        print (x.status_code)
        print (x.text)
        time.sleep(1)


our_list=[]
file=open("test_data.txt","r")
for i in file.readlines():

  our_list.append(i)
print (our_list)
@pytest.mark.webtest1
@pytest.mark.parametrize("test_input", our_list)
def testCases(test_input):

    a=test_input.split('=')

    x = requests.post(url, headers=headers, data=json.loads(a[0]))

    assert x.status_code==int(a[1])
    if x.status_code==int(a[1]):
      print ("pass")
    else:
      print ("failed")
