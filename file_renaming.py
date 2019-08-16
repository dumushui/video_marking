import re
import glob
from IPython.display import HTML
import os


class files_renaming():
    ''' 
    Desc:
        initialize with file_path, collect needed file and yeild
    Args:
        file_path: folder dir that containing needed files
    Return:
        changing file name and yeild next file path
    '''
    def __init__(self, file_path, with_label_marked=False):
        self.tail = '.mp4'
        self.file_path = file_path
        self.old_file = ''
        self.new_file = ''
        # default setting on data folder, change it if u need
        self.files = glob.glob('data\*.mp4')
        # select unprocessed files with the length of file name < 67 
        self.files = set([i for i in self.files if len(i) < 67])
        if self.files:
            self.file = self.files.pop()
        else:
            raise ValueError(f"没有可以处理的文件")
        
    def pop_update(self):
        if self.files:
            self.file = self.files.pop()
            return self.file
        else:
            raise ValueError(f"已经没有可以处理的文件")

    def to_csv(self, label):
        if os.path.exists('data.csv'):
            try:
                with open('data.csv','a+') as f:
                    f.write(f"{re.findall(r'data\\(.*).mp4',self.file)[0]}{label}")
            except:
                
        pass
    
    def write_txt(self):
        pass
    
    def to_one_txt(self):
        pass
    
    def rename(self, label):
#        if '\\\\' not in self.file:
#            print(self.files)
#            self.file = self.file.replace('\\','\\\\')
        self.new_file = f"{re.findall(r'(.*).mp4',self.file)[0]}{label}.mp4"
        try:
            os.rename(self.file,self.new_file)
            self.old_file = self.file
        except:
            raise ValueError(f'wrong file path {self.file}')
        
    
    
    def file_retrace(self):
        try:
            os.rename(self.new_file,self.old_file)
        except:
            raise ValueError(f'wrong file path {self.file}')
            
    def showvideo(self,autoplay=True, loop=True):
        display(HTML(f"""<video autoplay={autoplay} loop={loop} width="640" height="480" controls><source src="{self.file}" type="video/mp4"></video>"""))
        

if __name__ == '__main__':
    import os
    fr = files_renaming(os.getcwd())
    


