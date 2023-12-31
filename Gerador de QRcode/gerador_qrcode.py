import qrcode

numero_qrcode = 'a003'

imagem = qrcode.make(f"https://pagnando-production.up.railway.app/{numero_qrcode}")
imagem.save(f'QRCode{numero_qrcode}.png')
