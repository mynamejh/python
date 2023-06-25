import os

def add_file(file_path):
    if os.path.exists(file_path):
        print("이미 존재하는 파일입니다.")
    else:
        with open(file_path, 'w') as file:
            print("새 파일이 생성되었습니다.")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("파일이 삭제되었습니다.")
    else:
        print("파일이 존재하지 않습니다.")

def modify_file(file_path, new_content):
    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("파일이 수정되었습니다.")
    else:
        print("파일이 존재하지 않습니다.")

# 파일 추가 예제
file_path = './hey.txt'
add_file(file_path)

# 파일 삭제 예제
#file_path = './hey.txt'
#delete_file(file_path)

# 파일 수정 예제
file_path = './hey.txt'
new_content = '내용추가하기!!!.'
modify_file(file_path, new_content)
