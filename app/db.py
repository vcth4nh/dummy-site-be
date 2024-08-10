import os
import time
import sqlite3

from helper import validate_hex_color

dummy_data = [
    {
        "id": 4,
        "content": "Chào mọi người, mình có tin vui muốn chia sẻ! Mình đã điều chỉnh lệnh gọi API list_objects_v2 của S3 và bây giờ nó nhanh hơn 20%. 🎉",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 6,
        "content": "Chào mọi người, mình vừa hoàn thành báo cáo tài chính quý 2. Tình hình rất khả quan! 📊",
        "img": "msg/sample.jpg",
        "time": "2024-07-29"
    },
    {
        "id": 7,
        "content": "Mình vừa thử nhà hàng mới ở phố bên, đồ ăn rất ngon và giá cả hợp lý. Mọi người nên thử! 🍲",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 8,
        "content": "Đội mình vừa vượt qua mốc 1000 người dùng đăng ký. Cảm ơn mọi người đã nỗ lực! 🚀",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 9,
        "content": "Mình mới xem bộ phim mới ra mắt hôm qua, rất hay và xúc động. Khuyên mọi người nên xem! 🎬",
        "img": "msg/sample.jpg",
        "time": "2024-07-29"
    },
    {
        "id": 11,
        "content": None,
        "img": "msg/sample.jpg",
        "time": "2024-07-29"
    },
    {
        "id": 15,
        "content": "Mình vừa nhận được kết quả kiểm tra sức khỏe, mọi thứ đều ổn. Nhớ giữ gìn sức khỏe mọi người! 🩺",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 16,
        "content": "Dự án mới của chúng ta đã chính thức khởi động. Hãy cùng nhau cố gắng để đạt được mục tiêu! 💪",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 17,
        "content": "Mình vừa tham gia một khóa học online về phát triển bản thân, rất bổ ích và thú vị. Mọi người nên thử! 📚",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 18,
        "content": "Chúng ta có một cuộc họp quan trọng vào ngày mai. Nhớ chuẩn bị kỹ và đến đúng giờ nhé! ⏰",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 19,
        "content": "Mình vừa thử một bài tập thể dục mới, rất hiệu quả và thú vị. Ai muốn thử không? 🏋️",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 20,
        "content": "Cuối tuần này trời đẹp, mình dự định đi picnic. Ai muốn tham gia thì đăng ký nhé! 🌞",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 21,
        "content": "Mình vừa đọc xong một cuốn sách rất hay về quản lý thời gian. Để mình chia sẻ vài điểm thú vị với mọi người! 📖",
        "img": "msg/sample.jpg",
        "time": "2024-07-29"
    },
    {
        "id": 28,
        "content": "Có ai biết sửa lỗi phần mềm này không? Mình đang gặp vấn đề và cần giúp đỡ. 💻",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 30,
        "content": "Mình vừa thử nấu một món ăn mới, rất ngon và đơn giản. Để mình chia sẻ công thức với mọi người! 🍴",
        "img": None,
        "time": "2024-07-29"
    },
    {
        "id": 31,
        "content": "Chào mọi người, mình muốn tổ chức một buổi gặp mặt cuối tuần này. Ai có ý kiến gì không? 👫",
        "img": "msg/sample.jpg",
        "time": "2024-07-29"
    },
    {
        "id": 32,
        "content": "Mình vừa khám phá một ứng dụng mới rất hữu ích cho công việc. Mọi người nên thử xem sao! 📱",
        "img": None,
        "time": "2024-07-29"
    }
]

count = len(dummy_data) + 1

theme_dummy_data = {
    "msg_color": "#000000",
    "bg_color": "#000000",
    "bg_img": "bg/sample.jpg"
}


def open_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_name = os.environ.get("DB_NAME")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    return conn, c


def test_db():
    with open_db() as (conn, cur):
        # Create table
        cur.executescript('''
        CREATE TABLE IF NOT EXISTS msg (id INTEGER PRIMARY KEY, content TEXT, image TEXT, time DATETIME DEFAULT CURRENT_TIMESTAMP, deleted INTEGER DEFAULT 0);
        CREATE TABLE IF NOT EXISTS theme (msg_color TEXT, bg_color TEXT, bg_img TEXT)
        ''')
        conn.commit()


def get_msgid(msgid) -> dict:
    if msgid > len(dummy_data):
        return dummy_data[len(dummy_data)]
    return dummy_data[msgid]


def delete_msg(msgid):
    for i in range(len(dummy_data)):
        if dummy_data[i]["id"] == msgid:
            del dummy_data[i]
            break


def create_msg(msg, img_name) -> None:
    global count
    epoch = int(time.time())
    count += 1
    data = {
        "id": count,
        "content": msg,
        "img": img_name,
        "time": epoch
    }
    dummy_data.append(data)


def get_msg(offset, length) -> list[dict]:
    if offset > len(dummy_data):
        offset = len(dummy_data) - 1

    limit = min(offset + length, len(dummy_data))
    return dummy_data[offset:limit]


def get_total_msg() -> int:
    return len(dummy_data)


def get_theme() -> dict:
    return theme_dummy_data


def set_theme(msg_color, bg_color, bg_img_path):
    if msg_color is not None and validate_hex_color(msg_color):
        theme_dummy_data["msg_color"] = msg_color
    if bg_color is not None and validate_hex_color(bg_color):
        theme_dummy_data["bg_color"] = bg_color
    if bg_img_path is not None:
        theme_dummy_data["bg_img"] = bg_img_path
    return theme_dummy_data

# def set_theme_default():
#     theme_dummy_data["msg_color"] = "#000000"
#     theme_dummy_data["bg_color"] = "#000000"
#     theme_dummy_data["bg_img"] = "msg/sample.jpg"
#     return theme_dummy_data
