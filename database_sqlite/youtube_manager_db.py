import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
    Create Table IF Not EXISTS videos (
               id INTEGER PRIMARY KEY, 
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')
    

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("Database is Empty")
    else:
        for row in rows:
            print(row)
    return rows

    
def add_video():
    vid_name = input("Enter Video Name: ")
    vid_time = input("Enter Video Time: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (vid_name, vid_time))
    conn.commit()

def update_video():
    videos = list_all_videos()
    index = int(input("Enter the Number to update: "))
    if 1 <= index <= len(videos):
        vid_name = input("Enter new Video Name: ")
        vid_time = input("Enter new Video Time: ")
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (vid_name, vid_time, index))
        conn.commit()
    else:
        print("Invalid Index Selected. ")


def delete_video():
    videos = list_all_videos()
    index = int(input("Enter the Number to Delete: "))
    if 1 <= index <= len(videos):
        cursor.execute("DELETE FROM videos WHERE id = ?", (index,))
        conn.commit()
    else:
        print("Invalid Index Selected. ")


def main():
    while True:
        print("\n Youtube Manager app with DB | Type an Option")
        print("*" * 50)
        print('\n')
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid Choice! Please type the correct option")
    conn.close()

if __name__ == '__main__':
    main()