import qrcode

DEFAULT_SIZE = 30
DEFAULT_PADDING = 2
DEFAULT_FG_COLOR = '#000'
DEFAULT_BG_COLOR = '#FFF'

class MyQr:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, foreground_color: str, background_color: str):
        user_input: str = input('Enter the QR code text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=foreground_color, back_color=background_color)
            qr_image.save(file_name)

            print(f'Successfully created! ({file_name})')
        except (ValueError, OSError, qrcode.exceptions.DataOverflowError) as e:
            print(f'Error: {e}')

def main():
    myqr: MyQr = MyQr(size=DEFAULT_SIZE, padding=DEFAULT_PADDING)
    myqr.create_qr('sample.png', foreground_color=DEFAULT_FG_COLOR, background_color=DEFAULT_BG_COLOR)
     
if __name__ == '__main__':
    main()
    