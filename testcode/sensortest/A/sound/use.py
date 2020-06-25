import Sound


def run():
    sound = Sound.Control(0)

    while True:
        threshold = sound.dataConvt()
        print(threshold)

if __name__=="__main__":
    run()