
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
- ![VD](imgs/IMG_7191.HEIC)