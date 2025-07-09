import json
file_path = "youtube.txt"
def loaddata():
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(file_path, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos, start = 1 ):
        print(f"{index}. Video Name: {video['name']}, Duration: {video['time']}")
    # print('\n')
    print('*' * 70)

def add_video(videos):
    vid_name = input("Enter Video Name: ")
    vid_time = input("Enter Video Time: ")
    videos.append({'name': vid_name, 'time': vid_time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Number to update: "))
    if 1 <= index <= len(videos):
        vid_name = input("Enter new Video Name: ")
        vid_time = input("Enter new Video Time: ")
        videos[index-1] = {'name': vid_name, 'time': vid_time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected. ")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Number to be Deleted: "))
    if 1 <= index <= len(videos):
        del videos[index -1]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected. ")


def main():
    videos = loaddata()

    while True:
        print("\n Youtube Manager | Type an Option")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice! Please type the correct option")


if __name__ == "__main__":
    main()
