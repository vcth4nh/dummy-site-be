# dummy-site-be


## Requirement
Must:
- Có trang login bằng pin 6 sô
- Sau khi login thì có thể gửi tin nhắn với 1 người duy nhất (giống chat với ChatGPT, ngoại trừ việc ChatGPT không phản hồi)
- Có thể gửi ảnh, video không quá 50mb

Should:
- Có thể thay theme

Nice:
- Có thể gửi sticker, gif


## Deploy
1. Rename `.env.example` -> `.env`
2. Change `.env` content
3. ```shell
    docker compose up
   ```