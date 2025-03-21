def main(name_file):
    with open(name_file, "r") as log:
        mass = ['0']
        line_number = range(len(log.readlines()))
        log.seek(0)
        for i in line_number:
            # print(log.readline().split()[1:])
            # log.seek(0)
            mass.append(0)
            for word in log.readline().split()[1:]:
                # print(word)
                # print(len(word))
                mass[i] = str(mass[i]) + str(len(word))
                # print(mass[i])
            print(i, " ", mass[i])




if __name__=="__main__":
    main("Xorg.0.log")

