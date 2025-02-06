import csv

def write_csv(dialogs_array):
    with open("dialogs.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dialogs_array)
def check_csv(channel_id):
    dialogs_array = []
    with open("dialogs.csv", "r") as csvfile:
        dialogs = csv.reader(csvfile)
        for line in dialogs:
            for value in line:
                if int(value) == int(channel_id):
                    return True
        return False
