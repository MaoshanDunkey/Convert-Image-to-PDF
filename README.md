# Convert-Image-to-PDF
使用Python实现将主文件夹下的所有子文件夹或单一文件夹中的图片自动合并成PDF。

Use Python to automatically merge images from all subfolders under the main folder or from a single folder into a PDF.

# 安装说明(Installation Instructions)
需要安装Pillow和Reportlab。

Need to install Pillow, Reportlab.

    pip install pillow
    pip install reportlab

# 如何使用(How to use)
修改convert.py中变量*input_folder*和*output_folder*的值，其中*input_folder*为图片所在的文件夹路径，*output_folder*为合并后的PDF所在的文件夹路径。例如有如下的文件目录结构:

    iinput_folder/                                       
    └─comics/                   
        ├─Vol.01/                   
        │ ├──  000.jpg                  
        │ ├──  001.jpg                  
        │ ├──  002.jpg                  
        │ └──  003.jpg     
        │             
        └─Vol.02/                   
          ├──  000.jpg                  
          ├──  001.jpg                  
          ├──  002.jpg                  
          └──  003.jpg    

则*input_folder* = "input_folder\\comics"。
假设输出文件存在一个空的文件夹output_folder下，则*output_folder* = "output_folder"。运行convert.py，output_folder的文件目录结构变为：

    output_folder/                                       
    ├─Vol.01.pdf
    │             
    └─Vol.02.pdf                  

当然，也可以输入单一文件夹的路径。即*input_folder* = "input_folder\\comics\\Vol.01"。

Modify the values of the variables *input_folder* and *output_folder* in convert.py, where *input_folder* is the path to the folder containing the images, and *output_folder* is the path to the folder where the merged PDF will be saved. For example, the file directory structure is as follows:

    iinput_folder/                                       
    └─comics/                   
        ├─Vol.01/                   
        │ ├──  000.jpg                  
        │ ├──  001.jpg                  
        │ ├──  002.jpg                  
        │ └──  003.jpg     
        │             
        └─Vol.02/                   
          ├──  000.jpg                  
          ├──  001.jpg                  
          ├──  002.jpg                  
          └──  003.jpg    

Then *input_folder* = "input_folder\\comics". Assuming the output file exists in an empty folder called output_folder, then *output_folder* = "output_folder". After running convert.py, the file directory structure of output_folder becomes:

    output_folder/                                       
        ├─Vol.01.pdf
        │             
        └─Vol.02.pdf

Of course, you can also input the path of a single folder. That is, *input_folder* = "input_folder\\comics\\Vol.01".