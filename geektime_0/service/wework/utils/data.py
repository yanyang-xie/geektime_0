import yaml


class Data:
    @classmethod
    def load_yaml(cls, path):
        with open(path) as f:
            data = yaml.load(f, yaml.Loader)
            return data

    @classmethod
    def export_yaml(cls, data, path):
        with open(path, 'w') as f:
            yaml.dump(data, f)

