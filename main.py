import segno

# user input to generate qr code
data_input = input('Insert text or link to generate QR code: ')

# user input for generated file name, appends the file type
qr_img_name = input('File name (if a file with that name already exists it will be replaced!): ') + '.svg'

def generateQr(data, name):
    '''
        This function takes the data entered by the user, 
        generates a QR code and saves it as an image 
        file with the desired name.
        '''
    data_to_qr = segno.make(data, error='q')
    data_to_qr.save(name, scale=10, dark='black', light=None)
    print(f'QR code generated successfully and saved as "{name}"')

if __name__ == "__main__":
    generateQr(data_input, qr_img_name)




