class Nissan:
        
    def __init__(self):
        self.models = ['altima', '370z', 'cube', 'rogue']
  
    
    def outModels(self):
        print('Estes são os modelos disponíveis para Nissan')
        for model in self.models:
            print('\t%s ' % model)