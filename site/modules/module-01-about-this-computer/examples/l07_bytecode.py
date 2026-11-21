import dis

source = "cores = 8\ndoubled = cores * 2\nprint(doubled)"
dis.dis(source)
