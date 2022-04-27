import pandas as pd
import re
import time



def extract_range_values(x):
    match = re.findall(r"([0-9]+)", x, re.I)
    if match:
        if len(match)  == 2:
            if int(match[0]) < int(match[1]):
                return range(int(match[0]), int(match[1]))
            else:
                # raise Exception("Error: First integer in age group is larger than the second.")
                return range(int(match[1]), int(match[0]))
        elif len(match) == 1:
            return match[0]
        else:
            print("No match for %s" % x)
            pass


class Transform(object):
    @staticmethod
    def age_to_range(data):
        ''' 
            parameters:
                data: age column from pandas dataframe
         '''
        data.AgeCategory = data.AgeCategory.apply(extract_range_values)
        return data

    @classmethod
    def clean_data(cls, data):
        # for i in data.columns:
        #     print('Column: ', i)
        #     print(data[i].unique())
        #     time.sleep(5)

        print('\n\nDropping duplicates...')
        data = data.drop_duplicates()

        print('\n\nDropping null values...')
        data = data.dropna()

        print('\n\nTransforming AgeCategory to range values...')
        data = cls.age_to_range(data)

        # t1 = time.time()
        # data = data.replace(['Yes', 'No'], [1, 0])
        # t2 = time.time()
        # print('TIME: ', t2 - t1)



        print('\n\nSuccess.')

        return data

    
        
""" 

"""