import urllib.parse

class LinkFactory:
    def __init__(self, aff_id="11315710905"):
        self.aff_id = aff_id

    def create(self, product, platform_code):
        # 1. ENCODE KATA KUNCI PRODUK
        keyword = urllib.parse.quote(product)
        
        # 2. FILTER PROFIT AFILIASI (Sangat Penting!)
        # Parameter 'cboption=1' biasanya menyaring produk Mall/Star Seller (Garansi Komisi)
        # Parameter 'is_affiliate=1' (jika didukung) atau filter relevansi tinggi
        # Kita tambahkan parameter tambahan untuk memaksa hasil pencarian berkualitas tinggi
        raw_search_url = f"https://shopee.co.id/search?keyword={keyword}&cboption=1&order=desc&sortBy=sales"
        
        # 3. ENCODE URL PENCARIAN
        encoded_target = urllib.parse.quote(raw_search_url)
        
        # 4. RAKIT DEEP LINK AFILIASI
        final_link = f"https://shopee.co.id/universal-link?redir={encoded_target}&affiliate_id={self.aff_id}&sub_id={self.aff_id}_{platform_code}"
        
        return final_link
