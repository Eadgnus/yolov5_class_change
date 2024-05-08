import os


def update_yolo_labels(input_folder, output_folder, class_mapping):
    # 입력 폴더의 모든 파일 목록 가져오기
    file_list = os.listdir(input_folder)

    for file_name in file_list:
        # 파일 경로 생성
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name)

        # 라벨 파일 열기
        with open(input_file_path, 'r') as file:
            lines = file.readlines()

        # 라벨 파일 수정
        modified_lines = []
        for line in lines:
            # 클래스(class) 정보 추출
            label_info = line.strip().split(' ')
            class_index = int(label_info[0])
            if class_index in class_mapping:
                # 클래스(class) 수정
                class_name = class_mapping[class_index]
                label_info[0] = str(class_name)

            # 수정된 라인 추가
            modified_line = ' '.join(label_info)
            modified_lines.append(modified_line)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # 수정된 라벨 파일 저장
        with open(output_file_path, 'w') as file:
            file.write('\n'.join(modified_lines))


# 입력 폴더와 출력 폴더 경로 설정

input_folder = r"E:\aggregate\datasets\aggregate_volume_datasets/test/labels"
output_folder = r"E:\aggregate\datasets\aggregate_volume_datasets/test/new_labels"

# 클래스(class) 매핑 설정(왼쪽이 현재: 오른쪽이 바뀔것)
class_mapping = {
    0: '0',
    1: '1',
    2: "6",
    3: "5",
    4: "2",
    5: "3",
    6: "4",
    7: "7",
    8: "8",
    9: "9",
    10: "10"
    # 위에서 아래껄 로 바껴야 함
    # names: ['0', '100', '50', '60', '70', '80', '90']
    #                   0       1       2       3       4       5       6
    # names: ['0', '100', '70', '80', '90', '60', '50', '40', '30', '20', '10']
    #                   0       1       2       3       4         5     6       7       8       9       10
}

# 라벨 파일 수정 및 저장
update_yolo_labels(input_folder, output_folder, class_mapping)
