import os


class FileUtils:
    #保存数据
    def save(self,path,filename,content):
        if not os.path.exists(path):
            os.makedirs(path)

        file_path = path + '/' + filename
        f = open(file_path, 'a+')
        f.write(content)
        f.close()
