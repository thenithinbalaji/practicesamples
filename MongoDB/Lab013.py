import unittest
from mongosetup import *


'''
Description : Complete the below method using MongoDB methods to insert a 'Books' document into
'Library' Database.

Points to note :
Try to use collections.insert_many([dictionaries]) method
The document is available only after it is inserted in the DB


'''


def createBookDocuments():

    # connect to 'Library' data base in MongoDB
    # connect to 'Books' collection
    collections = getCollectionsFromLibraryDB("Books")
    # user insert_many() method to create the document in MongoDB
    dict = [{"Title":"Concepts of Physics", "Author":"HC Verma", "ISBN":93842},
            {"Title":"Concepts of Physics 2", "Author":"HC Verma", "ISBN": 83992},
            {"Title":"Python Programming", "Author":"Guido Van Russom", "ISBN":28923}
    ]
    inserted_doc_id = collections.insert_many(dict)

    return inserted_doc_id


class TestLab11(unittest.TestCase):
    def test_LibraryBooksCollection(self):
        # call create Book document
        createBookDocuments()
        # Test the created record
        books_data = getCollectionsFromLibraryDB(
            "Books").find()
        print(books_data)

        self.assertIsNotNone(
            books_data, "No Books data found. It is suppose to be found.")
        self.assertTrue(len(list((books_data))) >= 5,
                        "Insert Many records failed")


if __name__ == '__main__':
    unittest.main()
