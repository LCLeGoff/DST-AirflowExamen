import json
import os
import pandas as pd


class JsonClassUtils:
    def __init__(self):
        pass

    @staticmethod
    def write_obj_json(add, obj, rw='w'):
        out_file = open(add, rw)
        json.dump(obj, out_file, indent=2)
        out_file.close()

    @staticmethod
    def import_obj_json(add):
        in_file = open(add, 'r')
        new_dict = json.load(in_file)
        in_file.close()
        return new_dict

    def transform_data_into_csv(self, parent_folder='../raw_files', n_files=None):

        files = sorted(os.listdir(parent_folder), reverse=True)
        if n_files:
            files = files[:n_files]

        dfs = []
        for file in files:
            data = self.import_obj_json(os.path.join(parent_folder, file))
            if len(data) != 0:
                for d in data:
                    dfs.append(
                        {
                            'temperature': d['main']['temp'],
                            'city': d['name'],
                            'pression': d['main']['pressure'],
                            'date': file.split('.')[0]
                        }
                    )

        df = pd.DataFrame(dfs)

        print('\n', df.head(10))

        return df


