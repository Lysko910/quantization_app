from quantization import quantization
import json


def makeQuantization(img, options, parameters):
    obj = quantization(options=options, parameters=parameters)
    obj.show(img, "Original")

    if options["Algorithm_1"]:
        k_mean_img = obj.K_means(img, parameters["parameter1"], parameters["parameter2"])
        obj.show(k_mean_img, "k_mean_img")

    if options["Algorithm_2"]:
        # TO DO
        obj.show(img, "Algorithm 2")
        print("Algorithm 2")

    if options["Algorithm_3"]:
        # TO DO
        obj.show(img, "Algorithm 3")
        print("Algorithm 3")

    if options["Algorithm_4"]:
        # TO DO
        obj.show(img, "Algorithm 3")
        print("Algorithm 4")
    del obj


def load_default_parameters():
    # read defaults from json file and parse
    with open('default_parameters.json', 'r') as f:
        data = json.load(f)
    # print(data)
    parameters = {"parameter1": data['Algorithm_1'][0],
                  "parameter2": data['Algorithm_1'][1],
                  "parameter3": data['Algorithm_2'][0],
                  "parameter4": data['Algorithm_2'][1],
                  "parameter5": data['Algorithm_3'][0],
                  "parameter6": data['Algorithm_3'][1],
                  "parameter7": data['Algorithm_4'][0],
                  "parameter8": data['Algorithm_4'][1]}

    return parameters
