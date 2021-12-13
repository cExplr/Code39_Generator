import sys
from PIL import Image, ImageDraw
# References : https://en.wikipedia.org/wiki/Code_39

TEN_CHARS = "ABCDEFGHIJ"
TWENTY_CHARS = "KLMNOPQRST"
THIRTY_CHARS = "UVWXYZ-. *"
template = {}
CHAR_MAPPING = {}

BLACK = (0,0,0)
WHITE = (255,255,255)

ONE_UNIT_PIXELS = 1 

def init_char_mapping():
	template = {'1':"21112", '2':"12112" ,'3':'22111','4':'11212',\
				'5':'21211', '6':"12211" ,'7':'11122','8':'21121',\
				'9':'12121', '0':"11221" }

	for i in range(0,10):
		temp = template[str(i)]
		CHAR_MAPPING[str(i)] = temp[:2] + "0" + temp[2:]
	
	for i in range(len(TEN_CHARS)):
		index = (( 10 + i + 1) % 10)
		temp = template[str(index)]
		CHAR_MAPPING[TEN_CHARS[i]] = temp[:3] + "0" + temp[3:]

	for i in range(len(TWENTY_CHARS)):
		index = (( 20 + i + 1) % 10)
		temp = template[str(index)]
		CHAR_MAPPING[TWENTY_CHARS[i]] = temp[:4] + "0" + temp[4:]

	for i in range(len(THIRTY_CHARS)):
		index = (( 30 + i + 1) % 10)
		temp = template[str(index)]
		CHAR_MAPPING[THIRTY_CHARS[i]] = temp[:1] + "0" + temp[1:]

	return CHAR_MAPPING

def create_barcode_image(barcode, black=BLACK, white=WHITE, save=False):
	imageWidth = ONE_UNIT_PIXELS * len(barcode) * 3
	imageHeight = 70
	barcodeImage = Image.new(mode="RGB", size=(imageWidth, imageHeight),  color=white)
	d = ImageDraw.Draw(barcodeImage)
	#d.line(xy=[10,10,10,120] , fill = (0,0,0), width=ONE_UNIT_PIXELS)
	x = 0
	for i in range(len(barcode)):
		if barcode[i] == '0':
			d.line(xy=[x,0,x,imageHeight], fill=white, width=ONE_UNIT_PIXELS)
			x += ONE_UNIT_PIXELS*2
		elif barcode[i] == '1':
			d.line(xy=[x,0,x,imageHeight], fill=black, width=ONE_UNIT_PIXELS)
			x += ONE_UNIT_PIXELS*2
		elif barcode[i] == '2':
			d.line(xy=[x,0,x,imageHeight], fill=black, width=ONE_UNIT_PIXELS*2)
			x += ONE_UNIT_PIXELS*3
	if(save):
		barcodeImage.save("./barcode.jpg")

	barcodeImage.show()

def main():

	CHAR_MAPPING = init_char_mapping()
	START = STOP = CHAR_MAPPING["*"]
	while(True):
		
		value = input("Enter Value : " ).upper()
		try:
			barcode = START
			for i in value:
				barcode += CHAR_MAPPING[i]
			barcode += STOP
		except:
			print("please")
			pass
		print(value  + " : " + barcode)
		create_barcode_image(barcode)


main()
