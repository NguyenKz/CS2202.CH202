# Computational Linguistics vs Natural Language Processing

- **Computational Linguistics**: Khám phá tri thức ngôn ngữ
  - Focusos theo đặt điểm, ngữ pháp
  - VD: Dịch 1 câu:
    - Xem xet từ tiến anh -> tiếng việt: Từ loại, ngữ pháp -> map nghĩa.
    - Điều chỉnh cấu trúc từ loại và ngữ pháp, tạo từ điển.....
  - Không thể xây dựng thuật toán đủ tốt cho nhiều ngôn ngữ.
  
- **Natural Language Processing**: Xử lý ngôn ngữ tự nhiên
  - Focuses theo machine learning.
  - Hoàn toàn dựa vào data.
  - Đòi hỏi nhiều data, và data phải cân bằng.
    - VD: Dạy lớp A và B nhưng A nhiều Đata hơn thì kết quả sẽ lệch về A.
  - Không sử lý được những hiện tượng ngôn ngữ "hiếm" và những trường hợp "nhập nhằng".
  - Nếu thuần máy học:
    - Không biết làm sao để điều chỉnh thuật toán.
  - VD: Dịch 1 câu:
    - Dựa vào data: training data -> model -> predict.
    - Điều chỉnh training data và model để cải thiện kết quả.
- Cách tiếp cận của CL và NLP khác nhau.
- Nên kết hợp cả 2 để có kết quả tốt hơn.
  - Đầu tiên dùng NLP -> xem kết quả -> giải quyết trường hợp không có kết quả tốt bằng CL.


# Tại sao cần tri thức ngôn ngữ?
 Phân tích nghĩa của câu sau? Cần tri thức ngôn ngữ gì để hiểu đúng nghĩa câu này?
 1. Học sinh học sinh học.
    1. Ranh giới từ "_" -> Học sinh -> Học_sinh học Sinh_học.
 2. Cổ đeo vòng cổ.
 3. Ông già đi nhanh.
    1. Dùng ranh giới từ "_" và "loại từ" vẫn chưa đủ để hiểu câu này.
    2. "Ông gìa" đi nhanh | Ông "già đi" nhanh. -> Phân tích cú pháp.
       1. Hình tố. (Chủ ngữ)
       2. Phụ thuộc. (Vị từ)
 4. Nam kể về tai nạn hôm qua.
   
 Tiếng việt: Từ không bị khoản trắng chia cách, vd: học sinh, giáo viên, ...
 Tiếng anh: Từ bị khoản trắng chia cách, vd: student, teacher, ...
 -> Phải chuẩn hóa từ vựng, vd: học sinh học sinh học. -> học_sinh học sinh_học.
    - Cách này không đúng với câu (2): Cổ đeo vòng cổ. -> cổ_đeo vòng cổ | cổ đeo vòng_cổ. (vòng của cổ)
      - Có thể phân loại theo loại từ: cổ trong "vòng cổ" là "cổ" trong "cổ họng" (danh từ), "cổ" trong "cổ sửa" (tính từ).
  