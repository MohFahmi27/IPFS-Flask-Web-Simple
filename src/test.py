import cv2

tss = 'untitddled.png'
path = r'C:\D_Drive\anxd\TA\IPFS-Flask-Web-Simple\static\uploads\%s' % (tss)
img = cv2.imread(path, 0)
det = cv2.QRCodeDetector()
val, pts, st = det.detectAndDecode(img)
hashf = val.split('/')[-1].split('?')[0]
print(hashf)