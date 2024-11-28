import easyocr
import os

# 初始化 EasyOCR 读取器
reader = easyocr.Reader(['en'])

# 遍历文件夹
main_folder = "/home/yiny/Insight_Miner_Dataset/train_vis"
target_folder = "/home/yiny/Insight_Miner_Dataset/text_output"
os.makedirs(target_folder, exist_ok=True)

for root, dirs, files in os.walk(main_folder):
    for file in files:
        if file.lower().endswith(".png"):
            file_path = os.path.join(root, file)
            try:
                # 使用 EasyOCR 提取文字
                results = reader.readtext(file_path, detail=0)
                extracted_text = "\n".join(results)

                # 保存到 TXT 文件
                txt_file_name = os.path.splitext(file)[0] + ".txt"
                txt_file_path = os.path.join(target_folder, txt_file_name)
                with open(txt_file_path, "w", encoding="utf-8") as txt_file:
                    txt_file.write(extracted_text)
                print(f"提取完成: {txt_file_path}")
            except Exception as e:
                print(f"处理文件时出错: {file_path}, 错误: {e}")