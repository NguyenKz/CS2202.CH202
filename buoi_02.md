
# Các mức độ của Tri thức ngôn ngữ.

- **Phonetic/Phonological analysis (Speech)**: Phân tích âm thanh, phán âm.
- **OCR/Tokenization (Text)**: Phân tích văn bản.
- **Morphological analysis**: Phân tích tiếng việt, tiếng anh.
- **Syntactic analysis**: Phân tích cú pháp.
- **Semantic analysis**: Phân tích ngữ nghĩa.
- **Pragmatic analysis**: Phân tích ngữ dụng.
- **Discourse processing**: Phân tích luận văn.

# Các bài toán của NLP cơ bản

## Stemming: -> Dùng cho search engine/ Tổng hợp tiến nói.
- Loại bỏ đuôi biến cách của từ.
  - VD: running -> run, studies -> studi
  - Chú ý: Chỉ loại bỏ đuôi biến cách, không phục hồi từ gốc.


## Lemmatization: -> Dùng cho search engine/ Tổng hợp tiến nói.
- Phục hồi từ gốc của từ.
  - VD: running -> run, studies -> study
  - Chú ý: Lọai bỏ đuôi biến cách và phục phồi từ gốc.

## Text normalization:
- Chuẩn hóa văn bản.
  - VD: "Hello, world!" -> "hello, world!"
  - Chú ý: Chuẩn hóa văn bản.

## Sentiment segmentation:
- Dùng dấu chấm phân tách câu có những trường hơp: TP. HCM, 13.5, abc.com -> Không chỉ dùng dấu chấm. (Mới phát biểu -> Ghi điểm)
- Khó: Bị nhập nhằng dấu câu. Từng ngôn ngữ có cách phân tách khác nhau. Và mỗi người cũng có cách phân tách khác nhau (Không theo chuẩn).
- Quy ước: <s>....</s> Hệ thống dùng cập dấu <s>....</s> để phân tách câu, huấn luyện model.

## Word segmentation:
- Phân tách từ.
  - VD: "Xin chào cả nhà" -> "Xin_chào cả_nhà" (Chuẩn hóa để dùng chung rule với tiếng anh)
  - Chú ý: Phân tách từ.
  - Quy ước: dùng "_" để nối các word trong từ, vd: "Xin_chào cả_nhà"

## Part-of-speech tagging:
- Phân tích từ loại.
  - VD: "Xin chào cả nhà" -> "Xin_chào cả_nhà" (Chuẩn hóa để dùng chung rule với tiếng anh)
  - Chú ý: Phân tích từ loại.
  - Quy ước: dùng "_" để nối các word trong từ, vd: "Xin_chào cả_nhà"
  - VD: "<s>Hắn/B đã/... lập/V gia_đình/B, nhưng/.... gia_đình_ấy/B đã/... tan_vỡ/V</s>"

## Constituency parsing:
- ![VD](imgs/IMG_7191.png)
- Lư dạng cây cho dễ nhìn thôi.
  

## Dependency parsing:
- ![Lưu dạng cây](imgs/IMG_7192.png)
- ![Luư dạng nhãn mịn](imgs/IMG_7193.png)
- Lư dạng cây cho dễ nhìn thôi.

## Semantic role labeling:
- Vai trò ngữ nghĩa của từ.
- ![VD](imgs/IMG_7194.png)

## Time Annotation:
- Trả lời các câu hỏi liên quan tới thời gian.

## Error Tagging:
- Ứng dụng trong sửa lỗi chính tả.
- VD: My friend told me ì i knew about Skateboard. -><TIP idxxx><org>knew</org><suggestion>know</suggestion></TIP>

## Pragmatics vs discourse processing:
- Dùng trong tóm tắt văn bản.

### Discourse processing:
- Quan tâm tới tính mạch lạc.
- VD: "Tôi đi học, mẹ đi làm" -> "Tôi đi học còn mẹ đi làm"
  - Thêm "còn" để mạch lạc.
- VD: Mô tả ảnh -> chỉ ra 1 danh sách các từ -> Dùng discourse sắp xếp lại để tóm tắt cho giống với một câu có nghĩa.
  
## Coreference resolution:
- Xác định các từ chỉ cùng 1 dối tượng.
- Vd: "Lan đi chợ, cô ấy hay mua quà cho mẹ."
  - "cô ấy" chỉ tới Lan.

## Segmentation:
- Phân tích cảm xúc, từng khía cảnh của câu.


# Các vấn đề của NLP
- VD: 
  - "Con mèo trắng này" vs "Con mèo này trắng."
  - "Tôi đang cố khắc phục điểm yếu này" vs "Điểm yếu này tôi đang cố khắc phục."


# Quy trình thu thập dữ liệu
- Thu thập raw text
- Phát triển guideline
- Phát triển annotation tool và các tool tiền xử lý.
- ![Huấn luyện annotator](imgs/IMG_7196.png)
- Markup Annotaion.
- Kiểm tra chéo.
- Clean up corrupted data.
- Công bố corpus và guideline.
- 