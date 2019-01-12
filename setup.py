from distutils.core import setup #如果没有需要先安装

setup(
      name='Telecontrol',  #打包后的包文件名 
      version='1.6',  #版本
      description='a Telecontrol',   
      author=' Mr.yan',   
      license="Apache-2.0",
      author_email=' mryan050415@gmail.com',   
      url=' https://github.com/SuperSystemStudio/TelecontrolCodeRepairwoman',   
      py_modules=['TelecontrolCodeRepairwoman'],  #与前面的新建文件名一致 
      entry_points={
        'console_scripts': [
            'Telecontrol start = main:main',#pip安装完成后可使用demo命令调用demo下的main方法
        ],
      },
)