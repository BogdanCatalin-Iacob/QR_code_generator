'''
Generate a QR code
'''
import qrcode


class QRCode:
    '''
    Define the qr code
    '''
    def __init__(self, size: int, border: int):
        self.qr = qrcode.QRCode(box_size=size, border=border)

    def create_qr(self, filename: str, foreground_color: str, background_color: str):
        '''
        Generate QR image
        '''
        user_input: str = input('Enter text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(
                fill_color=foreground_color, back_color=background_color)
            qr_image.save(filename)

            print(f'Succesfully created! ({filename})')

        except Exception as err:
            print(f'Error {err}')


def main():
    '''
    create the qr code with specific settings
    '''
    myqr = QRCode(size=30, border=2)
    myqr.create_qr(
        'sample.png', foreground_color='black', background_color='green')


if __name__ == '__main__':
    main()
