import zipfile
import os

def compression(floder_Name):
    folder_name = f'{floder_Name}'
    # work_Path = f'{work_Path}'

    new_zips= zipfile.ZipFile(f'{folder_name}/{folder_name}.zip', 'w')

    arr = os.listdir(floder_Name)
    empty = []
    file_name = None

    for i in range(len(arr)):
        empty.append(arr[i].split('.'))

    for i in range(len(arr)):
        if len(empty[i]) == 2:
            if empty[i][1] == 'mp4' or empty[i][1] == 'avi':
                file_name = empty[i][0]+'.'+empty[i][1]
                # empty는 ['aa', 'mp4'] 이런식으로 조정되어있음
    for folder, subfolders, files in os.walk(f'{folder_name}'):
        # 2번 안들어가게 하려면 os.walk 에서 고쳐줘야함..
        # print(f'folder:{folder}')
        # print(f'subfolders:{subfolders}')
        # print(f'files:{files}')
        


        for file in files:
            if file == f'{folder_name}.zip':
                pass

            elif file == file_name:
                # 확장자명에 따라서 folder_name.mp4 이런식으로 추가 해줘야할수도
                pass

            else:
                new_zips.write(os.path.join(folder, file), compress_type = zipfile.ZIP_DEFLATED)

    print('compression is finished')
    new_zips.close()

# compression(folder_name)

# 안에 내부 파일이 있어야 zip 파일안에 파일이 존재함
# zip파일은 만들어져서 혹시 신호들어 왔을때 용량이 일정기간 이상이면 pass 하게 만들어야할듯

