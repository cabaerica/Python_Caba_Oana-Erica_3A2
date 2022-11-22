import re

def function3(txt, list):
    return [el for el in txt if any([re.search(r, el) for r in list])]                                             
                                                  
def main():
    print(function3(['Maria', 'face','1', 'prajituri.'], ["\d", "\wri", "\wte", "\d{2}"])) 
      
main()   