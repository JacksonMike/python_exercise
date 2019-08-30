#复制文件流程
#获取要复制的文件名
oldFileName = input("请输入要复制的文件名:")
#打开要复制的文件
oldFile = open(oldFileName,"r")
#newFileName = "附件" + oldFileName
position = oldFileName.rfind(".")
newFileName = oldFileName[0:position] + "附件" + oldFileName[position:]
#创建一个新的文件
newFile = open(newFileName,"w")
#从旧文件中读取数据,并写入到新文件中
while True:
    content = oldFile.read(1024)
    if len(content) == 0:
        break
    newFile.write(content)
#关闭两个文件
oldFile.close()
newFile.close()