class Bmw:
        
    def __init__(self):
        self.models = ['i8', 'x1', 'x5', 'x6']
   
    
    def outModels(self):
        print('Estes são os modelos disponíveis para BMW')
        for model in self.models:
            print('\t%s ' % model)