"""
图片转base64工具 - convert_images.py
功能：将images目录下的图片转换为base64并更新报告
"""

import base64
import os

def image_to_base64(image_path):
    """将图片转换为base64编码"""
    with open(image_path, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
    
    # 获取文件扩展名
    ext = os.path.splitext(image_path)[1][1:].lower()
    if ext in ['jpg', 'jpeg']:
        mime_type = 'image/jpeg'
    elif ext == 'png':
        mime_type = 'image/png'
    elif ext == 'gif':
        mime_type = 'image/gif'
    else:
        mime_type = 'image/png'
    
    return f"data:{mime_type};base64,{encoded}"

def generate_report_with_images():
    """生成包含base64图片的报告"""
    images_dir = 'images'
    # 读取已含base64图片的报告文件
    report_path = '课程设计报告_含图片.md'
    
    # 图片文件列表（中文文件名映射）
    image_files = {
        'wordcloud': ['wordcloud.png', '词云.png', '词云图.png'],
        'bar': ['bar.png', '柱状图.png'],
        'line': ['line.png', '折线图.png'],
        'pie': ['pie.png', '饼图.png'],
        'radar': ['radar.png', '雷达图.png'],
        'scatter': ['scatter.png', '散点图.png'],
        'funnel': ['funnel.png', '漏斗图.png'],
        'before_main': ['before_main.png', '改进前.png'],
        'after_wordcloud': ['after_wordcloud.png', '改进后词云.png'],
        'after_bar': ['after_bar.png', '改进后柱状图.png'],
        'after_sidebar': ['after_sidebar.png', '改进后侧边栏.png']
    }
    
    # 读取原始报告
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换图片引用为base64
    for key, filenames in image_files.items():
        found_path = None
        for filename in filenames:
            image_path = os.path.join(images_dir, filename)
            if os.path.exists(image_path):
                found_path = image_path
                break
        
        if found_path:
            print(f"正在转换: {found_path}")
            base64_str = image_to_base64(found_path)
            # 替换相对路径为base64
            for filename in filenames:
                old_ref = f"./images/{filename}"
                content = content.replace(old_ref, base64_str)
            print(f"转换完成: {found_path}")
        else:
            print(f"警告: 文件不存在 - {key}")
    
    # 保存更新后的报告
    new_report_path = '课程设计报告_含图片.md'
    with open(new_report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n报告已保存到: {new_report_path}")
    print("所有图片已嵌入报告中！")

if __name__ == '__main__':
    generate_report_with_images()