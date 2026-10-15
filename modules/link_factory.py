import urllib.parse

class LinkFactory:
    def __init__(self, aff_id="11315710905"):
        self.aff_id = aff_id

    def create(self, product, platform_code):
        # 1. Buat URL Pencarian Asli Shopee
        # Contoh: https://shopee.co.id/search?keyword=Sepatu%20Sneakers
        raw_search_url = f"https://shopee.co.id/search?keyword={urllib.parse.quote(product)}"
        
        # 2. Encode (Bungkus) URL pencarian tersebut agar aman disisipkan
        encoded_target = urllib.parse.quote(raw_search_url)
        
        # 3. Rakit Deep Link Afiliasi Resmi (Gunakan shopee.co.id, BUKAN s.shopee.co.id)
        # Parameter resmi untuk melacak komisi: redir, affiliate_id, dan sub_id
        final_link = f"https://shopee.co.id/universal-link?redir={encoded_target}&affiliate_id={self.aff_id}&sub_id={self.aff_id}_{platform_code}"
        
        return final_link
