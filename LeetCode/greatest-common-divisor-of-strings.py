# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def funct():
    str1 = "ABABAB"
    str2 = "ABAB"

    temp = str1 if len(str1) < len(str2) else str2
    for x in range(len(temp), 0, -1):
        if len(str1) % len(temp[:x]) == 0 and len(str2) % len(temp[:x]) == 0:
            result1 = str1.split(temp[:x])

            answer1 = False if "".join(result1) else True
            result2 = str2.split(temp[:x])
            answer2 = False if "".join(result2) else True
            if answer1 and answer2:
                return temp[:x]

    return ""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(funct())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
