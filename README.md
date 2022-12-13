# vmturbo
Hệ thống giám sát, phân tích các thông số chi tiết xác định lỗi thiếu CPU, RAM, Network IO hoặc IOPS Storage

## Bước 1. Đường link download các công cụ dùng cho cài đặt, triển khai, kích hoạt license vmTurbo:
https://onedrive.live.com/?authkey=%21AAw1AJYZ4X7tIBg&id=B2EF85D309C9F6D4%21259855&cid=B2EF85D309C9F6D4 

## Bước 2. Sau khi download về máy PC nếu là Windows 10/11 hoặc Windows 2k12,2k16/2k19.

Lưu ý: 
- Có thể bị lỗi chữ ký số SHA1 do file OVA mình làm đã lâu từ trước 2017, nên khi deploy lên máy chủ VMWware vSphere các phiên bản 7.x hoặc 8.x sẽ bị báo lỗi
![image](https://user-images.githubusercontent.com/106635733/207253119-6afe1b60-d14e-4cbc-b7ba-7e0f47e4b24e.png)

- Lúc đó hãy download thêm bản VMware OVF Tool cho WIndows hoặc Linux, iOS... để có thể convert file OVA cũ của mình thành SHA1 OVA mới,
- Sau khi cài xong VMware OVF Tool, thì hãy dùng CMD chạy ở trạng thái Run as Administration:
và gõ 2 lệnh sau:
cd "C:\Program Files\VMware\VMware OVF Tool\"
ovftool.exe --allowExtraConfig --shaAlgorithm=SHA1 D:\Setup\VMTurbonomic\vmturbo64-opsmgr-5.5.7.ova D:\Setup\VMTurbonomic\vmturbo64-opsmgr-sha1_557.ova

ví dụ: màn hình lệnh
![image](https://user-images.githubusercontent.com/106635733/207253528-b1c0dced-83b9-4477-8347-d6fd19b939ec.png)


## Bước 3. Dùng quyền Root hoặc AD User thuộc nhóm ESX Admins hoặc được phân quyền tương đương Root và Deploy file OVA đã được download về hoặc được tạo mới từ lệnh VMware OVF Tool.
