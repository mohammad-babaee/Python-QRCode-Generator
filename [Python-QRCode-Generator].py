import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black" , back_color="white")
    img.save("qrimage.png")

print ("Welcome to the Python QR Code Generator ")

web_link = input("Please Enter Your Fav Link : ")

generate_qrcode(web_link)

# Developer : Mohammad Babaee