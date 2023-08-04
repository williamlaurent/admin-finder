import requests
from bs4 import BeautifulSoup

def load_urls(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def load_admin_pages(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def is_admin_page(url, admin_pages):
    # Tambahkan / pada akhir URL jika tidak ada
    if not url.endswith("/"):
        url += "/"

    # Cek apakah halaman admin ada pada URL
    for page in admin_pages:
        response = requests.get(url + page)
        if response.status_code == 200:
            return True, url + page

    return False, None

if __name__ == "__main__":
    admin_pages_file = "admin_url.txt"
    urls_file = "urls.txt"

    admin_pages = load_admin_pages(admin_pages_file)
    target_urls = load_urls(urls_file)

    for url in target_urls:
        is_admin, admin_url = is_admin_page(url, admin_pages)
        if is_admin:
            print(f"Admin page ditemukan pada {admin_url}")
        else:
            print(f"Tidak dapat menemukan halaman admin pada {url}")
