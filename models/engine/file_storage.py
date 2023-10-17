# models/engine/file_storage.py

# Add this import at the top of the file
from models.user import User

# ...

class FileStorage:
    # ...
    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        exists; otherwise, do nothing). If the file doesn’t exist, no
        exception should be raised"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                content = json.load(f)
            for key, value in content.items():
                class_name = value['__class__']
                if class_name == 'User':
                    obj = User(**value)
                else:
                    obj = eval(class_name)(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
