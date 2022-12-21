from operator import itemgetter

import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import img_to_array, load_img


class FeatureExtractor:
    def __init__(self):
        # # Use VGG-16 as the architecture, ImageNet for the weight
        # base_model = VGG16(weights='imagenet')
        # # Customize the model to return features from fully-connected layer
        # self.model = Model(inputs=base_model.input,
        #                    outputs=base_model.get_layer('fc1').output)
        pass

    def extract(self, img):
        x = np.expand_dims(img, axis=0)
        x = preprocess_input(x)
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)


def eucledian_distance(x, y):
    eucl_dist = np.linalg.norm(x - y)
    return eucl_dist


Extractor = FeatureExtractor()


def get_most_similar(books, image_url, max_result_num):

    pred = Extractor.extract(img)

    books_and_scores = []
    for book in books:
        img = load_img(image_url, target_size=(224, 224))
        img = img_to_array(img) / 255.0
        cover = load_img(book.cover, target_size=(224, 224))
        cover = img_to_array(cover) / 255.0
        cover_pred = Extractor.extract(img)

        score = eucledian_distance(pred, cover_pred)
        books_and_scores.append((book, score))

    books_and_scores.sort(key=itemgetter(1))
    return books_and_scores[:max_result_num]
