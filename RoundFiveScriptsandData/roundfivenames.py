from namemaker import makefilenames

foldernames = ['RoundFive']
letternames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3']
basicpath = 'C:\\Users\\admin\\Documents\\UCB\\Irene\\RoundFiveRecs\\'
extension = '.wav'

filenames = makefilenames(foldernames, letternames, numbers, basicpath, extension)

print(filenames)
