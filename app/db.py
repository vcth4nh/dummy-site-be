dummy_data = [
    {
        "id": 4,
        "content": "Chào mọi người, mình có tin vui muốn chia sẻ! Mình đã điều chỉnh lệnh gọi API list_objects_v2 của S3 và bây giờ nó nhanh hơn 20%. 🎉",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 6,
        "content": "Chào mọi người, mình vừa hoàn thành báo cáo tài chính quý 2. Tình hình rất khả quan! 📊",
        "img": "af2ddcc0-b401-4c13-914a-04cdc0ed2756.jpg",
        "date": "2024-07-29"
    },
    {
        "id": 7,
        "content": "Mình vừa thử nhà hàng mới ở phố bên, đồ ăn rất ngon và giá cả hợp lý. Mọi người nên thử! 🍲",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 8,
        "content": "Đội mình vừa vượt qua mốc 1000 người dùng đăng ký. Cảm ơn mọi người đã nỗ lực! 🚀",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 9,
        "content": "Mình mới xem bộ phim mới ra mắt hôm qua, rất hay và xúc động. Khuyên mọi người nên xem! 🎬",
        "img": "af2ddcc0-b401-4c13-914a-04cdc0ed2756.jpg",
        "date": "2024-07-29"
    },
    {
        "id": 11,
        "content": None,
        "img": "af2ddcc0-b401-4c13-914a-04cdc0ed2756.jpg",
        "date": "2024-07-29"
    },
    {
        "id": 15,
        "content": "Mình vừa nhận được kết quả kiểm tra sức khỏe, mọi thứ đều ổn. Nhớ giữ gìn sức khỏe mọi người! 🩺",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 16,
        "content": "Dự án mới của chúng ta đã chính thức khởi động. Hãy cùng nhau cố gắng để đạt được mục tiêu! 💪",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 17,
        "content": "Mình vừa tham gia một khóa học online về phát triển bản thân, rất bổ ích và thú vị. Mọi người nên thử! 📚",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 18,
        "content": "Chúng ta có một cuộc họp quan trọng vào ngày mai. Nhớ chuẩn bị kỹ và đến đúng giờ nhé! ⏰",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 19,
        "content": "Mình vừa thử một bài tập thể dục mới, rất hiệu quả và thú vị. Ai muốn thử không? 🏋️",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 20,
        "content": "Cuối tuần này trời đẹp, mình dự định đi picnic. Ai muốn tham gia thì đăng ký nhé! 🌞",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 21,
        "content": "Mình vừa đọc xong một cuốn sách rất hay về quản lý thời gian. Để mình chia sẻ vài điểm thú vị với mọi người! 📖",
        "img": "af2ddcc0-b401-4c13-914a-04cdc0ed2756.jpg",
        "date": "2024-07-29"
    },
    {
        "id": 28,
        "content": "Có ai biết sửa lỗi phần mềm này không? Mình đang gặp vấn đề và cần giúp đỡ. 💻",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 30,
        "content": "Mình vừa thử nấu một món ăn mới, rất ngon và đơn giản. Để mình chia sẻ công thức với mọi người! 🍴",
        "img": None,
        "date": "2024-07-29"
    },
    {
        "id": 31,
        "content": "Chào mọi người, mình muốn tổ chức một buổi gặp mặt cuối tuần này. Ai có ý kiến gì không? 👫",
        "img": "af2ddcc0-b401-4c13-914a-04cdc0ed2756.jpg",
        "date": "2024-07-29"
    },
    {
        "id": 32,
        "content": "Mình vừa khám phá một ứng dụng mới rất hữu ích cho công việc. Mọi người nên thử xem sao! 📱",
        "img": None,
        "date": "2024-07-29"
    }
]


def get_msgid(msgid):
    if msgid > len(dummy_data):
        return dummy_data[len(dummy_data)]
    return dummy_data[msgid]


def delete_msg(msgid):
    return None


def create_msg(msg, img_name):
    return 0


def get_msg(offset, length) -> list[dict]:
    if offset > len(dummy_data):
        offset = len(dummy_data) - 1

    limit = min(offset + length, len(dummy_data))
    return dummy_data[offset:limit]


def get_img_name(imgid):
    return "af2ddcc0-b401-4c13-914a-04cdc0ed2756.jpg"


def create_img(msgid, img_name):
    return None


def delete_img(msgid):
    return None


def get_total_msg():
    return len(dummy_data)
