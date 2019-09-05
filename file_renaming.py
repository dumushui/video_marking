import re
import glob
from IPython.display import HTML
import os
from pathlib import Path


class files_renaming():
    ''' 
    Desc:
        initialize with data_dir, collect needed file and yeild
    Args:
        data_dir: folder dir that containing needed files
    Return:
        changing file name and yeild next file path
    '''
    def __init__(self, data_dir, with_label_marked=False):
        self.tail = '.mp4'
        self.code_dir = Path().resolve()
        self.data_dir = self.code_dir/data_dir
        self.old_file = ''
        self.new_file = ''
        # default setting on data folder, change it if u need
        self.files = list(self.data_dir.glob('*.mp4'))
        # select unprocessed files with the length of file name < 67 
        self.files = set([i for i in self.files if len(i.name) < 67])
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
        tmp = re.findall(r'data\\(.*).mp4',self.file)[0]
        try:
            with open('data.csv','a+') as f:
                f.write(f"{tmp},{label}")
        except:
            print("failed on output label to csv file")
    
    def write_txt(self):
        with open(f"{re.findall(r'(.*).mp4',self.file)[0]}.txt",'w') as f:
            f.write(label)
        
    
    def to_one_txt(self):
        pass
    
    def rename(self, label):
#        if '\\\\' not in self.file:
#            print(self.files)
#            self.file = self.file.replace('\\','\\\\')
        self.new_file = self.file.parent/f'{self.file.stem}{label}{self.file.suffix}'
        try:
            self.old_file = self.file
            self.file.rename(self.new_file)
        except:
            raise ValueError(f'wrong file path {self.file}')
        
    
    
    def file_retrace(self):
        try:
            os.rename(self.new_file,self.old_file)
        except:
            raise ValueError(f'wrong file path {self.file}')
            
    def showvideo(self,autoplay=True, loop=True):
        relative_dir = self.file.relative_to(self.code_dir)
        display(HTML(f"""<video autoplay={autoplay} loop={loop} width="640" height="480" controls><source src="{str(relative_dir)}" type="video/mp4"></video>"""))
        

if __name__ == '__main__':
    import os
    data_dir = 'data'
    fr = files_renaming(data_dir)
    
    


