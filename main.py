import segno
from colorama import Fore

def generateQr(data, name):
    '''
        This function takes the data entered by the user, 
        generates a QR code and saves it as an image 
        file with the desired name.
        '''
    data_to_qr = segno.make(data, error='q')
    data_to_qr.save(name, scale=10, dark='black', light=None)
    print(Fore.GREEN + f'QR code generated successfully and saved as "{name}"')

if __name__ == "__main__":
    while True:
        print(Fore.YELLOW + '-------------QR SVG GENERATOR (Press CTRL+C to exit)-------------')
        # user input to generate qr code
        data_input = input(Fore.RESET + 'Insert text or link to generate QR code: ')

        # user input for generated file name, appends the file type
        qr_img_name = "qr_files/" + input('File name ' + Fore.RED + '(if a file with that name already exists it will be replaced!): ' + Fore.RESET) + '.svg'
        
        generateQr(data_input, qr_img_name)
        





