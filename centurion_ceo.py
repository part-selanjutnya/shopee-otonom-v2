import os
import json
import time
from datetime import datetime

from modules.brain_intent import IntentEngine
from modules.link_factory import LinkFactory
from modules.radar_x import RadarX
from modules.radar_tiktok import RadarTikTok
from modules.radar_fb import RadarFB
from modules.radar_ig import RadarIG
from modules.radar_pinterest import RadarPinterest

class CenturionCEO:
    def __init__(self):
        self.brain = IntentEngine()
        self.factory = LinkFactory()
        self.divisions = [RadarX(), RadarTikTok(), RadarFB(), RadarIG(), RadarPinterest()]
        
        self.log_path = "database/memory.json"
        self.trend_path = "database/live_trends.json"
        self.command_path = "database/target_manual.txt"

    def analyze_realtime_trends(self):
        hot_keywords = []
        context = ""
        
        # 1. BACA REMOTE CONTROL (FILE TXT)
        if os.path.exists(self.command_path):
            try:
                with open(self.command_path, "r", encoding="utf-8") as f:
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                
                if len(lines) > 1 and lines[0].upper() == "AKTIF":
                    hot_keywords = lines[1:]
                    context = "INSTRUKSI MUTLAK CEO (VIA TXT)"
            except Exception:
                pass

        # 2. JIKA TXT NONAKTIF/KOSONG, GUNAKAN AI OTONOM
        if not hot_keywords:
            current_hour = (datetime.utcnow().hour + 7) % 24
            current_day = datetime.utcnow().day
            
            if 11 <= current_hour <= 14:
                context = "Jam Istirahat / Cuaca Siang"
                hot_keywords = ["Diskon Shopee Food", "Kipas Angin Portable", "Sunscreen SPF 50"]
            elif 18 <= current_hour <= 22:
                context = "Prime Time Hiburan Malam"
                hot_keywords = ["Lampu Tidur Estetik", "Skincare Malam", "TWS Bass Booster"]
            else:
                context = "Waktu Santai / Dini Hari"
                hot_keywords = ["Outfit OOTD Pria", "Sprei Kasur Anti Kusut", "Tas Selempang Anti Air"]

            if current_day >= 25 or current_day <= 1:
                hot_keywords.append("Smartphone Terbaru Promo Gajian")
                context += " (Efek Tanggal Gajian)"

        live_trends = {
            "X/Twitter": f"{hot_keywords[0]} (Terkunci)",
            "TikTok": f"{hot_keywords[min(1, len(hot_keywords)-1)]} (Terkunci)",
            "Meta/FB": f"{hot_keywords[min(2, len(hot_keywords)-1)]} (Terkunci)",
            "Instagram": f"{hot_keywords[0]} (Terkunci)",
            "Pinterest": f"{hot_keywords[min(1, len(hot_keywords)-1)]} (Terkunci)",
            "Market_Context": context,
            "Last_Updated": datetime.utcnow().isoformat() + "Z"
        }
        
        os.makedirs("database", exist_ok=True)
        with open(self.trend_path, "w") as f:
            json.dump(live_trends, f, indent=4)
            
        return hot_keywords

    def save_log(self, data):
        history = []
        if os.path.exists(self.log_path):
            try:
                with open(self.log_path, "r") as f: history = json.load(f)
            except: pass
            
        history.append(data)
        if len(history) > 100: history = history[-100:]
        with open(self.log_path, "w") as f: json.dump(history, f, indent=4)

    def execute_operations(self):
        print("🚀 [CEO] Mengecek Satelit Komando dan Menganalisa Tren...")
        active_trends = self.analyze_realtime_trends()
        
        import random
        for div in self.divisions:
            prospect = div.scan()
            prospect['target'] = random.choice(active_trends)
            score = self.brain.analyze(prospect['target'])
            
            plat_code = prospect['platform'][:3].upper().replace("/", "")
            link = self.factory.create(prospect['target'], plat_code)
            
            print(f"📡 [{prospect['platform']}] Target: {prospect['target']} (Skor: {score}%)")
            print(f"🔗 Link: {link}\n")
            
            self.save_log({
                "time": datetime.utcnow().isoformat() + "Z",
                "platform": prospect['platform'],
                "target_product": prospect['target'],
                "intent_score": score
            })
            time.sleep(1.5)

if __name__ == "__main__":
    CenturionCEO().execute_operations()
