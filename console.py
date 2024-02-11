#!/usr/bin/python3
"""Console module"""
import cmd
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity",
               "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg_list[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + '.' + arg_list[1]
        all_objs = models.storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + '.' + arg_list[1]
        all_objs = models.storage.all()
        if key in all_objs:
            del all_objs[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg_list = arg.split()
        if arg_list and arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        all_objs = models.storage.all()
        class_objs = [str(obj) for obj in all_objs.values()
                      if not arg_list or obj.__class__.__name__ == arg_list[0]]
        print(class_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + '.' + arg_list[1]
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        setattr(all_objs[key], arg_list[2], arg_list[3])
        models.storage.save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        count = 0
        all_objs = models.storage.all()
        for obj in all_objs.values():
            if obj.__class__.__name__ == arg_list[0]:
                count += 1
        print(count)

    def default(self, line):
        """Handles default case"""
        args = line.split(".")
        if len(args) != 2:
            print("*** Unknown syntax:", line)
            return
        if args[1][:5] == "show(" and args[1][-1] == ")":
            class_name = args[0]
            id_ = args[1][5:-1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            key = class_name + '.' + id_
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        elif args[1][:8] == "destroy(" and args[1][-1] == ")":
            class_name = args[0]
            id_ = args[1][8:-1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            key = class_name + '.' + id_
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")
        elif args[1][:7] == "update(" and args[1][-1] == ")":
            class_name = args[0]
            params = args[1][7:-1].split(", ")
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if len(params) < 3:
                print("** instance id missing **")
                return
            key = class_name + '.' + params[0]
            all_objs = models.storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return
            if len(params) < 4:
                print("** attribute name missing **")
                return
            if len(params) < 5:
                print("** value missing **")
                return
            setattr(all_objs[key], params[1], params[2])
            models.storage.save()
        elif args[1][:7] == "update(" and args[1][-1] == ")":
            class_name = args[0]
            id_dict = args[1][7:-1].split(", ")
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if len(id_dict) < 2:
                print("** instance id missing **")
                return
            id_ = id_dict[0]
            key = class_name + '.' + id_
            all_objs = models.storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return
            if len(id_dict) < 3:
                print("** dictionary missing **")
                return
            try:
                dictionary = eval(id_dict[1])
            except Exception as e:
                print("** wrong dictionary format **")
                print(str(e))
                return
            for k, v in dictionary.items():
                setattr(all_objs[key], k, v)
            models.storage.save()
        else:
            print("*** Unknown syntax:", line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
