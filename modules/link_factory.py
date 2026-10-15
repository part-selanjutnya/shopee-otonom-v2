# FUNGSI: Pabrik Universal Link Shopee Anti-404
import urllib.parse

class LinkFactory:
    def __init__(self, aff_id="11315710905"):
        self.aff_id = aff_id

    def create(self, product, platform_code):
        encoded = urllib.parse.quote(product)
        return f"https://s.shopee.co.id/universal-link?q={encoded}&aff_id={self.aff_id}&subid={self.aff_id}_{platform_code}"
