import qrcode as qr
print("Enter Your Link or text :>>\n")
var = str(input())
img = qr.make(var)
print("Saved.>>")
img.save("Result.png")