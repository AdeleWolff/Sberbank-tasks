import csv
import sklearn
import sklearn.neighbors as nb

def prepare_data(main_data, additional_data):
    known_features = []
    known_labels = []
    unknown_features = []

    for index, line in enumerate(main_data):
        label = int( line[1] )
        line = [line[0], line[2]] + additional_data[index]
        line = [int(float(element) if element else 0 ) for element in line]

        if label == -1:
            unknown_features.append(line)
            continue
        known_labels.append(label)
        known_features.append(line)

    return known_features, known_labels, unknown_features


def read(filename):
    with open(filename, "r") as f_input:
        reader = csv.reader(f_input)
        lines = []
        for row in reader:
            lines.append(row)
    return lines[0], lines[1:]


def write(lines):
    with open("AlexanderSubbotin-15052019-SberbankIndustry.csv", "w") as f_output:
        # writer = csv.writer(f_output)
        # writer.writerows(lines)
        f_output.writelines(lines)


def main():
    filename_main = "inn_info_public.csv"
    filename_additional = "pays.csv"
    header_line_main, lines_main = read(filename_main)
    header_line_additional, lines_additional = read(filename_additional)

    X, y, features = prepare_data(lines_main, lines_additional)

    knn_classifier = nb.KNeighborsClassifier()

    knn_classifier.fit(X, y)
    predicted_labels = knn_classifier.predict(features)

    write( [ "{},{}\n".format(feature[0], predicted_labels[i]) for i, feature in enumerate(features) ] )


if __name__ == "__main__":
    main()

