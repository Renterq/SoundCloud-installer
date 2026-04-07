import yt_dlp

def soundcloud_indir(url):
    print(f"\n🎧 İndiriliyor: {url}")

    ydl_opts = {
        'format': 'bestaudio/best', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3', 
            'preferredquality': '192', 
        }],
        'outtmpl': '%(title)s.%(ext)s', 
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ İndirme ve dönüştürme başarıyla tamamlandı!\n")
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")

if __name__ == "__main__":
    print("--- SoundCloud MP3 İndirici ---")
    while True:
        link = input("SoundCloud Linkini Girin (Çıkmak için 'q' yazın): ")
        if link.lower() == 'q':
            print("Görüşmek üzere!")
            break
        elif "soundcloud.com" in link:
            soundcloud_indir(link)
        else:
            print("Lütfen geçerli bir SoundCloud linki girin.")





