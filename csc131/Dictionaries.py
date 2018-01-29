#
#1/26/18
'''edited 1/29/18'''
#

def get_personal_data() ->dict:
    """
    :return: Returns a dictionary of personal information.
    """
    personal_data = {"name": "Jim", "a_role": "teacher"}
    return personal_data

def main() -> int:
    default_dict = dict()
    print(default_dict)
    initialized_dict = dict([('name', 'Jim'),('a_role', 'joker')])
    print(initialized_dict)
    simple_init_dict = dict(name = 'Jim', a_role = 'teacher')
    print(simple_init_dict)
    return 0

if __name__ == '__main__':
    main()
