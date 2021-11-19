from utils import BAD_RETURN_CODE, SCORES_FILE_NAME
import re


def add_score(diff, username):
    index = 0
    points = (diff * 3) + 5
    try:
        with open(SCORES_FILE_NAME) as scoresFile:
            if username in scoresFile.read():
                my_file = open(SCORES_FILE_NAME, "r")
                lines = my_file.readlines()
                for x in lines:
                    value = x
                    if re.search(r"\b{}\b".format(username), x):
                        numbers = []
                        for word in value.split():
                            if word.isdigit():
                                numbers.append(int(word))
                        new_score = numbers[0] + points
                        for line in lines:
                            if line == x:
                                lines[index] = username + ", " + str(new_score) + "\n"
                                my_file.close()
                                my_file = open(SCORES_FILE_NAME, "w")
                                my_file.writelines(lines)
                                my_file.close()
                    index = index + 1
            elif username not in scoresFile.read():
                my_file = open(SCORES_FILE_NAME, "r")
                lines = my_file.readlines()
                my_file.close()
                lines.append(username + ", " + str(points) + "\n")
                my_file = open(SCORES_FILE_NAME, "w")
                my_file.writelines(lines)
                my_file.close()
    except BaseException:
        return BAD_RETURN_CODE


add_score(3, "agam")

