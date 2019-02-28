import hashlib
import argparse


class File():

    def __init__(self, path):
        self.path = path

    def hashsum(self):
        with open(self.path) as f:
            file = f.read()
            hashsum = hashlib.md5(file.encode('utf-8')).hexdigest()
            return hashsum


class Manifest():
    manifest_path = None

    def check(self, name, obj):
        with open(self.manifest_path) as file:
            lines = file.readlines()
            for line in lines:
                if line == name + ':' + str(obj) + '\n':
                file_name, file_hash = line.strip().split(':')
                if file_name == name and file_hash == str(obj):
                    print('Win')
                    return True
            print('New file.')
            Manifest.write_hash(self, name, obj)
            return None

    def write_hash(self, name, obj):
        with open(self.manifest_path, 'w') as file:
            file.write(str(name) + ':' + str(obj) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--calc', nargs='+', dest='files', default=['file.txt', 'file2.txt'])
    parser.add_argument('--manif', nargs='+', dest='Manifest', default='Manifest.txt')

    pars = parser.parse_args()
    print(pars.files)
    print(pars.Manifest)
    Manifest.manifest_path = pars.Manifest
    for i in pars.files:
        file = File(i)
        Manifest().check(file.path, file.hashsum())