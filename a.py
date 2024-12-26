import gdown

# URL file Google Drive
url = "https://archive.org/download/ghost-spectre-windows-10/WIN10.PRO.21H1.X64.GHOSTSPECTRE.%28WPE%29.ISO"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win10.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
