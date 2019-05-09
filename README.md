# QQSpaceLoger

## 使用

`python QQSpaceLog.py`

在弹出的QQ空间登陆页面中手动登陆(请在30秒内完成登陆),之后将自动以截图形式记录说说

## 预配置

### 安装库
```
pip install selenium
pip install time
pip install bs4
```

### 下载chromedriver驱动文件

下载当前项目中的`chromedriver.exe`并放在与**QQSpaceLog.py**同级目录下
若要修改`chromedriver.exe`文件的位置或名称 请修改代码第`8`行

### 配置文件

手动创建 **D:\QQlog\img** 文件夹

手动创建 **D:\QQlog\qq.ini** 文件

若要修改此地址 请修改代码中对应 `22 30 74 77 80 85` 行

## 效果

每张说说的截图储存在**D:\QQlog\img\** 文件夹下,每张图片的名称是 时间+名称+.png
**D:\QQlog\index.html**上为记录汇总

