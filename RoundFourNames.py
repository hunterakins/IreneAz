from namemaker import makefilenames

foldernames = ['5mm', '4mm', '3mm', '2mm', '1mm']
letternames = ['A', 'B', 'C', 'D']
numbers = ['1', '2', '3']
basicpath = 'C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFour\\'
extension = '.wav'

filenames = makefilenames(foldernames, letternames, numbers, basicpath, extension)

