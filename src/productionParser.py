class ProductionParser:
    def __init__(self, productionString):
        
        ps = productionString
        ps = ps.split("=")
        
        self.productionNr = int(ps[0])
        
        self.indexPairs = ps[1].split(",")
        for i in range(len(self.indexPairs)):
            pair = self.indexPairs[i].split("-")
            self.indexPairs[i] = (int(pair[0]), int(pair[1]))


