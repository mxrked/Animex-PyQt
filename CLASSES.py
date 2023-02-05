from GLOBALS import  *
import GLOBALS

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def setUsername(self, username):
        self._username = username

    def setPassword(self, password):
        self._password = password

    def getUsername(self):
        return self._username

    def getPassword(self):
        return self._password



class Product:
    def __init__(self, productID, productName, productPrice, productImg, productQuantity, productSubTotal):
        self._productID = productID
        self._productName = productName
        self._productPrice = productPrice
        self._productImg = productImg
        self._productQuantity = productQuantity
        self._productSubTotal = productSubTotal

    def setProductID(self, productID):
        self._productID = productID

    def setProductName(self, productName):
        self._productName = productName

    def setProductPrice(self, productPrice):
        self._productPrice = productPrice

    def setProductImg(self, productImg):
        self._productImg = productImg

    def setProductQuantity(self, productQuantity):
        self._productQuantity = productQuantity

    def setProductSubTotal(self, productSubTotal):
        self._productSubTotal = productSubTotal

    def getProductID(self):
        return self._productID

    def getProductName(self):
        return self._productName

    def getProductPrice(self):
        return self._productPrice

    def getProductImg(self):
        return self._productImg

    def getProductQuantity(self):
        return self._productQuantity

    def getProductSubTotal(self):
        return self._productSubTotal



# Figures
tanjirouKamadoFigure_OBJ = Product("storeItem_1", "Tanjirou Kamado Figure", 40.75, "imgs/figures/tanjirouKamadoFigure.png", 0, 0.0)

# Manga
jojoSDCVol1Manga_OBJ = Product("storeItem_2", "Stardust Crusaders Vol.1", 23.30, "imgs/manga/jojoSDCVol1.png", 0, 0.0)

# Clothing
mobWorkingOutBlackTshirtClothing_OBJ = Product("storeItem_3", "Mob working out black T-shirt", 26.40, "imgs/clothing/mobWorkingOutBlackTshirt.png", 0, 0.0)
