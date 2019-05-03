# incomplete_image
Detect incomplete downloaded images

# Determine if jpg contains an incomplete ending
def is_valid_jpg(jpg_file):
    with open(jpg_file, 'rb') as f:
        f.seek(-2, 2)
        buf = f.read()
        f.close()
        return buf ==  b'\xff\xd9'  

# Delete incomplete images       
os.remove(train_dir + file) 
