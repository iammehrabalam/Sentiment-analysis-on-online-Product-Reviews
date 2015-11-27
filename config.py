REGEX = {
    "happy": ":\-?[\)\]D]",
    "sad": ":'?\-?\(",
    'shock': ":\-O|:\-\(\)",
    "uneasy": ":\-/",
    "evil": ">:\-[\(D]",
    " ": "(http[s]?:\/\/)?([\w_-]+(?:(?:\.[\w_-]+)+))" +
         "([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
}


# turney POS list
SENTI_POS = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG',
             'VBN', 'VBP', 'VBZ']
# ,'NN', 'NNS', 'NNP', 'NNPS'
FIRST_LIST = ["JJ", "RB", "RBR", "RBS", "NN", "NNS"]
SECOND_LIST = ["JJ", "NN", "NNS", "VB", "VBD", "VBN", "VBG"]
THIRD_LIST = ["NN", "NNS"]

# ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
POS_LIST = {
    'VB': 'v',
    'VBD': 'v',
    'VBG': 'v',
    'VBN': 'v',
    'VBP': 'v',
    'VBZ': 'v',
    'JJ': 'a',
    'JJR': 'a',
    'JJS': 'a',
    'RB': 'r',
    'RBR': 'r',
    'RBS': 'r',
    'NN': 'n',
    'NNS': 'n',
    'NNPS': 'n',
}

# Amazon Config

AMAZON_SEARCH_INDEX = ['All', 'Beauty', 'Grocery', 'PetSupplies',
                       'OfficeProducts', 'Electronics', 'Watches',
                       'Jewelry', 'Luggage', 'Shoes', 'KindleStore',
                       'Automotive', 'MusicalInstruments', 'GiftCards',
                       'Toys', 'SportingGoods', 'PCHardware', 'Books', 'Baby',
                       'HomeGarden', 'VideoGames', 'Apparel',
                       'Marketplace', 'DVD', 'Music', 'HealthPersonalCare']

AMAZON_ACCESS_KEY_ID = "AKIAJF6RPKBHOO5S4VCA"
AMAZON_ACCESS_SECRET_KEY = "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"
AMAZON_ASSOCIATE_TAG = "oldbooks-21"

AMAZON_XPATH = {
    "_items": "Items/Item",
    "brand": "ItemAttributes/Publisher",
    "category_name": "ItemAttributes.Title",
    "description": "EditorialReviews/EditorialReview/Content",
    "id": "ASIN",
    "reviews_url": "ItemLinks/ItemLink",
    "image_url": "LargeImage/URL",
    "product_name": "ItemAttributes/Title"
}
