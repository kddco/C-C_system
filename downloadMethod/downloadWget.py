import wget

print('Beginning file download with wget module')
url = 'https://www.cmrdb.cs.pu.edu.tw/assets/img/star.jpg'
wget.download(url, 'C:/Users/wayne/Desktop/')