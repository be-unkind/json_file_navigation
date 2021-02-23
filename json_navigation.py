'''comfortable navigation through json file'''
import json

def get_file_location():
    '''
    Return file location, inputted by user. 
    '''
    print('Input file location.')
    file_location = str(input())
    return file_location

def json_to_dict():
    '''
    Return dictionary from json file.
    '''
    file_location = get_file_location()
    read_file = open(file_location, 'r', encoding='utf-8')
    result_dict = json.load(read_file)
    return result_dict

def get_information(json_dict):
    '''
    Return value/-s, found by key, inputted by user. 
    '''
    print('---')
    for key in list(iter(json_dict.keys())):
        print(f'The keys are: {key}')
    print('---')
    print('Input wanted key.')
    user_key = str(input())
    if isinstance(json_dict[user_key], str) or\
         isinstance(json_dict[user_key], int) or\
             isinstance(json_dict[user_key], float):
             return json_dict[user_key]
    elif isinstance(json_dict[user_key], dict):
        return get_information(json_dict[user_key])
    elif isinstance(json_dict[user_key], list):
        print('---')
        print(f'Input number in range: 0 to {len(json_dict[user_key])-1}')
        user_index = int(input())
        print('---')
        return json_dict[user_key][user_index]

if __name__ == '__main__':
    print(get_information(json_to_dict()))




