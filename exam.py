import os

train_dir = '/home/kitview/Documents/tensorflow1/models/research/object_detection/images/train/'

def progress(percent, width=50):

    if percent >= 100:
        percent = 100

    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")
    print('\r%s %d%% ' % (show_str, percent))

def is_valid_jpg(jpg_file):
    with open(jpg_file, 'rb') as f:
        f.seek(-2, 2)
        buf = f.read()
        f.close()
        return buf ==  b'\xff\xd9'  # Determine if jpg contains an incomplete ending

data_size = len([lists for lists in os.listdir(train_dir) if os.path.isfile(os.path.join(train_dir, lists))])
recv_size = 0
incompleteFile = 0
print('file tall : %d' % data_size)

for file in os.listdir(train_dir):
    if os.path.splitext(file)[1].lower() == '.jpg':
        ret = is_valid_jpg(train_dir + file)
        if ret == False:
            incompleteFile = incompleteFile + 1
            os.remove(train_dir + file) #delete incomplete images

    recv_per = int(100 * recv_size / data_size)
    progress(recv_per, width=30)
    recv_size = recv_size + 1

progress(100, width=30)
print('\nincomplete file : %d' % incompleteFile)