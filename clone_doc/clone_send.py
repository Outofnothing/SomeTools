import itchat
import os

itchat.auto_login(hotReload=True)
itchat.send('Login success.', toUserName='filehelper')
suffixes = ['.doc', '.docx', '.ppt', '.pptx', '.pdf', '.png', '.jpg', '.bmp', '.txt']


@itchat.msg_register(itchat.content.TEXT)
def get_files(msg):
    if msg['ToUserName'] != 'filehelper':
        return
    else:
        usb_path = msg['Text']
        if os.path.exists(usb_path):
            g = os.walk(usb_path)
            for path, dir_list, file_list in g:
                for file_name in file_list:
                    if os.path.splitext(file_name)[-1] in suffixes:
                        file_path = os.path.join(path, file_name)
                        itchat.send_file(file_path, "filehelper")


itchat.run()
