import qrcode
from PIL import Image

URL = "https://regularizaauto.sspc.gob.mx/"

qr =qrcode.QRCode(
    version=1,
    box_size=25,
    border=5
)

qr.add_data(URL)
qr.make(fit=True)

imagen = qr.make_image()
imagen.save("QR_Pagina.png")