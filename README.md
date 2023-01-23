# retroArch_playlist_generator

## 原理
&emsp;&emsp;由于switch RetroArch不能很好地支持中文文件名，需要使用playlist功能来显示。具体而言需要实现两个功能，一是根据rom生成playlist，二是修改rom文件名。请在电脑上建立游戏文件夹，作为rom顶层目录，然后在该目录下按平台建立各个rom的目录。例如顶层目录是**G:/game/test/**，目录下有**fc/**，**gba/**，**ps/**，**sfc/** 等平台。本工具会按指定的rom顶层目录，读取各个文件夹作为平台名，并逐平台生成playlist文件。逐平台生成playlist时，将其下各个rom重命名为"平台名+编号"的形式。

## 使用
### 目录组织
&emsp;&emsp;将各个rom按平台组织。各个平台的rom文件夹再在放在同一个目录下。此目录就称为rom顶层文件夹。
之后将顶层文件夹下的各个rom文件夹直接复制到retroarch指定的rom顶层文件夹下就可以。我通常是放在/rom/下

### 修改代码
&emsp;&emsp;需要安装python3，然后修改main.py。
rom_top_path改成rom顶层文件夹
switch_top_path改成retroArch中rom的目标文件夹
将os.rename那句代码放开注释，如果你需要重命名rom文件。

### 注意事项
&emsp;&emsp;没有充分测试
建议重命名前，把rom单独复制来做。

# enjoy ^__^

# 使用本代码生成列表的rom全部自动免费，不允许卖钱。要卖钱就别用。
