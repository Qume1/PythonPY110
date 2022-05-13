import json
import pickle
txt_file = "output.txt"
json_file = "output.json"
pickle_file = "output.pickle"
if __name__ == "__main__":
    list_ = [i ** 2 for i in range(1, 11)]
    with open(txt_file, "w") as f:
        f.write(str(list_))

    with open(json_file, "w") as f:
        with open(txt_file, "r") as d:
            json.dump(json.load(d), f, indent=4)

    with open(pickle_file, "wb") as f:
        with open(txt_file, "r") as d:
            pickle.dump(pickle.load(d), f)

    with open(pickle_file, "rb") as f:
        obj = pickle.load(f)

    pass
