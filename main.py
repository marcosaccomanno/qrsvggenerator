import segno
from colorama import Fore

def generateQr(data):
    '''
        This function takes the data entered by the user, 
        generates a QR code and saves it as a SVG image.
        '''
    # qr code is generated
    data_to_qr = segno.make(data, error='q')
    # output image name is defined
    file_name = 'qr_files/' + data + '.svg'
    # output image is saved as SVG
    data_to_qr.save(file_name, scale=10, dark='black', light=None)
    # success message is displayed
    print(Fore.GREEN + f'QR code generated successfully and saved in the "qr_files" folder.')

if __name__ == "__main__":
    program_active = True
    while program_active == True:
        print(Fore.YELLOW + '-------------QR SVG GENERATOR-------------' +  Fore.RESET)
        # user enters text or link to generate qr code
        data_input = input('Insert text or link to generate QR code: ')
        # function for generating qr code is called
        generateQr(data_input)
        # ask if the user wants to generate another qr code
        program_continue = input(Fore.YELLOW + 'Generate another QR? (y/n): ' + Fore.RESET)
        if program_continue != 'y':
            print(Fore.YELLOW + '------------------------------------------' +  Fore.RESET)
            # program ends
            program_active = False





