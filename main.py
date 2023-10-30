'''
Generate a QR code
'''
import qrcode


class QRCode:
    def __init__(self, size: int, border: int):
        self.qr = qrcode.QRCode(box_size=size, border=border)

    def create_qr(self, filename: str, foreground_color: str, background_color: str):
        '''
        Generate QR image
        '''
        user_input: str = input('Enter text: ')
