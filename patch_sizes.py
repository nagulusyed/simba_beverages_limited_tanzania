import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Chunk 1: Kombucha
target_kombu = """      <div class="prod-card kombu">
        <div class="prod-bottle-zone"><div class="prod-glow kombu-glow"></div>
          <svg width="75" height="165" viewBox="0 0 75 165" fill="none"><defs><linearGradient id="kg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#3D2200"/><stop offset="50%" stop-color="#6B3E00"/><stop offset="100%" stop-color="#2A1800"/></linearGradient></defs>
          <rect x="14" y="0" width="10" height="5" rx="2" fill="#C8841A"/><rect x="11" y="5" width="53" height="8" rx="3" fill="#A06A10"/>
          <rect x="8" y="13" width="59" height="130" rx="6" fill="url(#kg)"/><rect x="8" y="30" width="59" height="96" fill="#4A2800" opacity="0.8"/>
          <text x="37" y="70" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="7" fill="#F5A623">OLA</text>
          <text x="37" y="80" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="6" fill="#F5A623">KOMBUCHA</text>
          <text x="37" y="92" text-anchor="middle" font-family="Arial,sans-serif" font-size="5" fill="rgba(245,166,35,0.6)">PROBIOTIC TEA</text>
          <circle cx="37" cy="55" r="10" fill="rgba(245,166,35,0.15)" stroke="#F5A623" stroke-width="0.8"/>
          <text x="37" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="8">🍵</text>
          <ellipse cx="37" cy="143" rx="29" ry="5" fill="#2A1800"/></svg>
        </div>
        <div class="prod-category">Probiotic Tea</div><div class="prod-name">Ola Kombucha</div>
        <div class="prod-desc">Naturally fermented sparkling kombucha tea packed with probiotics and organic nutrients to refresh and revitalize.</div>
        <div class="size-tags"><span class="size-tag">330ml Can</span><span class="size-tag">500ml</span></div>
      </div>"""
      
repl_kombu = """      <div class="prod-card kombu">
        <div class="prod-bottle-zone"><div class="prod-glow kombu-glow"></div>
          <svg width="80" height="160" viewBox="0 0 80 160" fill="none"><defs><linearGradient id="kg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#3D2200"/><stop offset="50%" stop-color="#6B3E00"/><stop offset="100%" stop-color="#2A1800"/></linearGradient></defs>
          <rect x="32" y="0" width="16" height="8" rx="3" fill="#6B3E00"/><rect x="28" y="8" width="24" height="16" rx="2" fill="url(#kg)"/>
          <path d="M28 24 Q16 36 14 52 L66 52 Q64 36 52 24 Z" fill="url(#kg)"/><rect x="14" y="50" width="52" height="88" rx="4" fill="url(#kg)"/>
          <rect x="17" y="62" width="46" height="62" rx="3" fill="#F8F4EE"/>
          <path d="M17 62 L21 55 L25 60 L32 53 L40 58 L48 53 L55 60 L59 55 L63 62Z" fill="#C8841A"/>
          <circle cx="40" cy="83" r="14" fill="#C8841A"/>
          <ellipse cx="36" cy="80" rx="3" ry="2.5" fill="#1A0F02"/><ellipse cx="44" cy="80" rx="3" ry="2.5" fill="#1A0F02"/>
          <path d="M36 86 Q40 90 44 86" stroke="#8B3A0A" stroke-width="1.2" fill="none" stroke-linecap="round"/>
          <text x="40" y="103" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="4.5" fill="#1A0F02">OLA KOMBUCHA</text>
          <rect x="17" y="118" width="46" height="6" fill="#C8841A"/>
          <path d="M14 138 Q14 142 18 142 L62 142 Q66 142 66 138 L66 136 L14 136 Z" fill="#2A1800"/></svg>
        </div>
        <div class="prod-category">Probiotic Tea</div><div class="prod-name">Ola Kombucha</div>
        <div class="prod-desc">Naturally fermented sparkling kombucha tea packed with probiotics and organic nutrients to refresh and revitalize.</div>
        <div class="size-tags"><span class="size-tag">330ml</span></div>
      </div>"""

# Chunk 2: Ginger Punch
target_ginger = """      <div class="prod-card ginger">
        <div class="prod-bottle-zone"><div class="prod-glow ginger-glow"></div>
          <svg width="75" height="165" viewBox="0 0 75 165" fill="none"><defs><linearGradient id="gg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#2A3A10"/><stop offset="50%" stop-color="#4A6A18"/><stop offset="100%" stop-color="#1A2808"/></linearGradient></defs>
          <rect x="14" y="0" width="10" height="5" rx="2" fill="#8AAA3D"/><rect x="11" y="5" width="53" height="8" rx="3" fill="#6A8A2D"/>
          <rect x="8" y="13" width="59" height="130" rx="6" fill="url(#gg)"/><rect x="8" y="30" width="59" height="96" fill="#2A4A08" opacity="0.8"/>
          <text x="37" y="68" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="7" fill="#F5A623">GINGER</text>
          <text x="37" y="78" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="7" fill="#F5A623">PUNCH</text>
          <text x="37" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="5" fill="rgba(245,166,35,0.6)">SPICED BEVERAGE</text>
          <circle cx="37" cy="54" r="10" fill="rgba(245,166,35,0.15)" stroke="#F5A623" stroke-width="0.8"/>
          <text x="37" y="57" text-anchor="middle" font-family="Arial,sans-serif" font-size="9">🫚</text>
          <ellipse cx="37" cy="143" rx="29" ry="5" fill="#1A2808"/></svg>
        </div>
        <div class="prod-category">Spiced Beverage</div><div class="prod-name">Ginger Punch</div>
        <div class="prod-desc">Zesty, fiery, and bold ginger beverage brewed from the finest local ginger root and natural spices.</div>
        <div class="size-tags"><span class="size-tag">330ml Can</span><span class="size-tag">500ml</span><span class="size-tag">1.5L</span></div>
      </div>"""

repl_ginger = """      <div class="prod-card ginger">
        <div class="prod-bottle-zone"><div class="prod-glow ginger-glow"></div>
          <svg width="80" height="160" viewBox="0 0 80 160" fill="none"><defs><linearGradient id="gg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#2A3A10"/><stop offset="50%" stop-color="#4A6A18"/><stop offset="100%" stop-color="#1A2808"/></linearGradient></defs>
          <rect x="32" y="0" width="16" height="8" rx="3" fill="#4A6A18"/><rect x="28" y="8" width="24" height="16" rx="2" fill="url(#gg)"/>
          <path d="M28 24 Q16 36 14 52 L66 52 Q64 36 52 24 Z" fill="url(#gg)"/><rect x="14" y="50" width="52" height="88" rx="4" fill="url(#gg)"/>
          <rect x="17" y="62" width="46" height="62" rx="3" fill="#F8F4EE"/>
          <path d="M17 62 L21 55 L25 60 L32 53 L40 58 L48 53 L55 60 L59 55 L63 62Z" fill="#4A6A18"/>
          <circle cx="40" cy="83" r="14" fill="#4A6A18"/>
          <ellipse cx="36" cy="80" rx="3" ry="2.5" fill="#F8F4EE"/><ellipse cx="44" cy="80" rx="3" ry="2.5" fill="#F8F4EE"/>
          <path d="M36 86 Q40 90 44 86" stroke="#F8F4EE" stroke-width="1.2" fill="none" stroke-linecap="round"/>
          <text x="40" y="103" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="4.5" fill="#1A0F02">GINGER PUNCH</text>
          <rect x="17" y="118" width="46" height="6" fill="#8B1A1A"/>
          <path d="M14 138 Q14 142 18 142 L62 142 Q66 142 66 138 L66 136 L14 136 Z" fill="#1A2808"/></svg>
        </div>
        <div class="prod-category">Spiced Beverage</div><div class="prod-name">Ginger Punch</div>
        <div class="prod-desc">Zesty, fiery, and bold ginger beverage brewed from the finest local ginger root and natural spices.</div>
        <div class="size-tags"><span class="size-tag">330ml</span></div>
      </div>"""

# Chunk 3: Hard Rock
target_energy = """      <div class="prod-card energy">
        <div class="prod-bottle-zone"><div class="prod-glow energy-glow"></div>
          <svg width="75" height="165" viewBox="0 0 75 165" fill="none"><defs><linearGradient id="eg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#1A0A3A"/><stop offset="50%" stop-color="#3A1A6A"/><stop offset="100%" stop-color="#0A051A"/></linearGradient></defs>
          <rect x="14" y="0" width="10" height="5" rx="2" fill="#7B3DAA"/><rect x="11" y="5" width="53" height="8" rx="3" fill="#5A2A88"/>
          <rect x="8" y="13" width="59" height="130" rx="6" fill="url(#eg)"/><rect x="8" y="30" width="59" height="96" fill="#120828" opacity="0.85"/>
          <path d="M41 40 L30 62 L38 62 L34 80 L48 55 L39 55 Z" fill="#F5A623"/>
          <text x="37" y="95" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="7" fill="#F5A623">HARD</text>
          <text x="37" y="105" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="7" fill="#F5A623">ROCK</text>
          <text x="37" y="116" text-anchor="middle" font-family="Arial,sans-serif" font-size="5" fill="rgba(245,166,35,0.6)">ENERGY DRINK</text>
          <ellipse cx="37" cy="143" rx="29" ry="5" fill="#0A051A"/></svg>
        </div>
        <div class="prod-category">Energy Drink</div><div class="prod-name">Hard Rock</div>
        <div class="prod-desc">High-performance energy drink formulated to deliver sustained physical stamina and mental focus.</div>
        <div class="size-tags"><span class="size-tag">250ml Can</span><span class="size-tag">500ml Can</span></div>
      </div>"""

repl_energy = """      <div class="prod-card energy">
        <div class="prod-bottle-zone"><div class="prod-glow energy-glow"></div>
          <svg width="80" height="160" viewBox="0 0 80 160" fill="none"><defs><linearGradient id="eg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#1A0A3A"/><stop offset="50%" stop-color="#3A1A6A"/><stop offset="100%" stop-color="#0A051A"/></linearGradient></defs>
          <rect x="32" y="0" width="16" height="8" rx="3" fill="#3A1A6A"/><rect x="28" y="8" width="24" height="16" rx="2" fill="url(#eg)"/>
          <path d="M28 24 Q16 36 14 52 L66 52 Q64 36 52 24 Z" fill="url(#eg)"/><rect x="14" y="50" width="52" height="88" rx="4" fill="url(#eg)"/>
          <rect x="17" y="62" width="46" height="62" rx="3" fill="#120828"/>
          <path d="M17 62 L21 55 L25 60 L32 53 L40 58 L48 53 L55 60 L59 55 L63 62Z" fill="#F5A623"/>
          <circle cx="40" cy="83" r="14" fill="#F5A623"/>
          <path d="M41 78 L35 86 L41 86 L38 92 L45 83 L41 83 Z" fill="#120828"/>
          <text x="40" y="103" text-anchor="middle" font-family="Arial Black,sans-serif" font-size="5" fill="#F5A623">HARD ROCK</text>
          <rect x="17" y="118" width="46" height="6" fill="#F5A623"/>
          <path d="M14 138 Q14 142 18 142 L62 142 Q66 142 66 138 L66 136 L14 136 Z" fill="#0A051A"/></svg>
        </div>
        <div class="prod-category">Energy Drink</div><div class="prod-name">Hard Rock</div>
        <div class="prod-desc">High-performance energy drink formulated to deliver sustained physical stamina and mental focus.</div>
        <div class="size-tags"><span class="size-tag">330ml</span></div>
      </div>"""

# Chunk 4: Select Dropdown
target_select = """              <select id="productSelect" class="calc-select">
                <option value="nkolomoka_250">Vin Nkolomoka 250ml</option>
                <option value="nkolomoka_500" selected>Vin Nkolomoka 500ml</option>
                <option value="nkolomoka_1l">Vin Nkolomoka 1 Litre</option>
                <option value="nkolo_mboka">Nkolo Mboka 330ml</option>
                <option value="ola_kombucha_can">Ola Kombucha 330ml Can</option>
                <option value="ola_kombucha_500">Ola Kombucha 500ml</option>
                <option value="ginger_punch_can">Ginger Punch 330ml Can</option>
                <option value="ginger_punch_500">Ginger Punch 500ml</option>
                <option value="ginger_punch_1l5">Ginger Punch 1.5L</option>
                <option value="hard_rock_250">Hard Rock 250ml Can</option>
                <option value="hard_rock_500">Hard Rock 500ml Can</option>
              </select>"""

repl_select = """              <select id="productSelect" class="calc-select">
                <option value="nkolomoka_330" selected>Vin Nkolomoka 330ml</option>
                <option value="nkolo_mboka_330">Nkolo Mboka 330ml</option>
                <option value="ola_kombucha_330">Ola Kombucha 330ml</option>
                <option value="ginger_punch_330">Ginger Punch 330ml</option>
                <option value="hard_rock_330">Hard Rock 330ml</option>
              </select>"""

if target_kombu in html:
    html = html.replace(target_kombu, repl_kombu)
    print("Replaced Kombucha")
else:
    print("Failed to find Kombucha")

if target_ginger in html:
    html = html.replace(target_ginger, repl_ginger)
    print("Replaced Ginger Punch")
else:
    print("Failed to find Ginger Punch")
    
if target_energy in html:
    html = html.replace(target_energy, repl_energy)
    print("Replaced Hard Rock")
else:
    print("Failed to find Hard Rock")
    
if target_select in html:
    html = html.replace(target_select, repl_select)
    print("Replaced Select dropdown")
else:
    print("Failed to find Select dropdown")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
