import qrcode

url=input("Enter the url?")

filename=input("Enter the filename you want to save it as?")
if not(filename.endswith(".png")):
    filename=filename+".png"

img=qrcode.make(url)
img.save(filename)