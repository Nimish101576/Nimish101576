import qrcode

url = "http://127.0.0.1:5500/Travel%20website.html"
qr = qrcode.make(url)
qr.save("travel_qr.png")