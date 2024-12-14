import os
from PIL import Image
from reportlab.pdfgen import canvas

def images_to_pdf(input_folder, output_folder):
    """
    将主文件夹下的子文件夹或单文件夹中的图片合并为 PDF 文件。
    
    Parameters:
        input_folder (str): 输入文件夹路径，可能是包含子文件夹的主文件夹，也可能是单个图片文件夹。
        output_folder (str): 输出 PDF 文件夹路径。
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 判断输入路径是包含多个子文件夹的主文件夹还是单一文件夹
    if all(os.path.isdir(os.path.join(input_folder, name)) for name in os.listdir(input_folder)):
        # 输入路径包含多个子文件夹
        for folder_name in sorted(os.listdir(input_folder)):
            folder_path = os.path.join(input_folder, folder_name)
            if os.path.isdir(folder_path):
                create_pdf(folder_path, os.path.join(output_folder, f"{folder_name}.pdf"))
    else:
        # 输入路径是单个文件夹
        folder_name = os.path.basename(os.path.normpath(input_folder))
        pdf_path = os.path.join(output_folder, f"{folder_name}.pdf")
        create_pdf(input_folder, pdf_path)
        

def create_pdf(folder_path, output_pdf_path):
    """
    将单个文件夹内的图片合并为 PDF 文件。

    Parameters:
        folder_path (str): 图片所在文件夹路径。
        output_pdf_path (str): 输出 PDF 文件路径。
    """
    if os.path.isdir(folder_path):
            image_files = sorted(
                [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
            )
            
            if not image_files:
                print(f"文件夹 {folder_path} 中没有找到图片，跳过...")
                return

            c = canvas.Canvas(output_pdf_path)
            for img_path in image_files:
                try:
                    with Image.open(img_path) as img:
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                        width, height = img.size
                        c.setPageSize((width,height))
                        c.drawImage(img_path,x=0,y=0)
                        c.showPage()
                except Exception as e:
                    print(f"加载图片失败: {img_path}，错误: {e}")
            
            c.save()
                        
            print(f"生成 PDF: {output_pdf_path}")

if __name__ == "__main__":
    # 输入文件夹路径和输出文件夹路径
    input_folder = "E:\\__easyHelper__\\Comics\\test"  # 替换为包含子文件夹的主文件夹路径
    output_folder = "E:\\__easyHelper__\\Comics\\output"  # 替换为存储 PDF 的文件夹路径

    # 调用函数
    images_to_pdf(input_folder, output_folder)
