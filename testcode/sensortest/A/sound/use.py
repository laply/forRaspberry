import Sound

def run():
    sound = Sound.Control(0)
    while True:
        data = sound.dataConvt()
        print(data)

if __name__ == "__main__":
    run()