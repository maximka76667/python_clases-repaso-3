from Multimedia import Multimedia

multimedia1 = Multimedia("Terminator", "James Cameron", "mov", 108)
multimedia2 = Multimedia("Terminator", "James Cameron", "mp4", 108)
multimedia3 = Multimedia("Terminator 2", "James Cameron", "mp4", 108)

print(multimedia1.__eq__(multimedia2))  # True
print(multimedia1.__eq__(multimedia3))  # False