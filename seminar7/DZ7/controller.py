import view
import logger
import model

def search ():
  fio = view.find_fio()
  base1 = logger.get_data()
  model.init(fio, base1)
  model.searchind( base1,fio)
  
