import Encryption
import ImagePatterns
from cryptography.fernet import Fernet

if __name__ == "__main__":
    
    
    #imageLoc = r'C:\Users\yaron\Documents\ImageTagger\testimg.jpg'
    imageLoc = r'C:\Users\yaron\Documents\ImageTagger\mntn.jpg'
    #imageLoc = r'C:\Users\yaron\Documents\ImageTagger\wp.jpg'
    #imageLoc = r'C:\Users\yaron\Documents\ImageTagger\selfie.jpg'
    
    loadLoc = r'C:\Users\yaron\Documents\ImageTagger\Encrypted.jpg'

    #copyLoc = r'C:\Users\yaron\Documents\ImageTagger\duplicate.jpg'
    copyLoc = r'C:\Users\yaron\Documents\ImageTagger\duplicate.png'

    #x = Encryption.textToPixelArray(b"The Rain In Spain Falls Mainly On The Plane")
    #ImagePatterns.patternEvenDistribution(imageLoc,copyLoc, x)
    
    x = ImagePatterns.returnEvenDistribution(loadLoc)
    #x = ImagePatterns.returnEvenDistribution(copyLoc)
    Encryption.decrypt(x)

    #ImagePatterns.patternClockStriping(imageLoc, 128, copyLoc)
    #ImagePatterns.patternBottom(imageLoc,128, copyLoc )
    print("success")
    exit()