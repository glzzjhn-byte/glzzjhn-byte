import urllib.request
import base64

url1 = "https://github.com/glzzjhn-byte.png"
req1 = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req1) as response:
    b64_img1 = base64.b64encode(response.read()).decode('utf-8')
    img_src = f"data:image/png;base64,{b64_img1}"

url2 = "https://c4.wallpaperflare.com/wallpaper/836/907/746/lycoris-recoil-nishikigi-chisato-anime-anime-girls-short-hair-hd-wallpaper-preview.jpg"
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req2) as response:
        b64_img2 = base64.b64encode(response.read()).decode('utf-8')
        chisato_src = f"data:image/jpeg;base64,{b64_img2}"
except Exception:
    chisato_src = url2

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="650" height="480" viewBox="0 0 650 480">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code&amp;display=swap');
      text {{ font-family: 'Fira Code', Consolas, monospace; font-size: 14.5px; fill: #cccccc; }}
      .bg {{ fill: #0c0c0c; stroke: #444; stroke-width: 2; }}
      .cmd-text {{ fill: #ffffff; }}

      /* Timeline 1: !profile (0s to 3s) */
      .reveal-mask {{ animation: reveal 1s steps(10, end) forwards; }}
      .cursor-move {{ animation: moveCursor 1s steps(10, end) forwards, hideCursor 0.1s forwards 1.5s; }}
      .output {{ opacity: 0; animation: appear 0.1s forwards 1.5s; }}
      .profile-pic {{ opacity: 0; transform-origin: 95px 180px; animation: fadeIn 1.5s forwards 1.8s; }}
      .cursor-wait {{ opacity: 0; animation: appear 0.1s forwards 1.5s, blink 1s step-end 2.5, hideCursor 0.1s forwards 4s; }}

      /* Timeline 2: !LoveLife (4s to 8s) */
      .reveal-mask-2 {{ opacity: 0; animation: appear 0.1s forwards 4s, reveal 1s steps(9, end) forwards 4s; }}
      .cursor-move-2 {{ opacity: 0; animation: appear 0.1s forwards 4s, moveCursor 1s steps(9, end) forwards 4s, hideCursor 0.1s forwards 5.5s; }}
      
      .compile-text {{ opacity: 0; animation: appear 0.1s forwards 5.5s; }}
      .error-text {{ opacity: 0; animation: appear 0.1s forwards 7s; }}
      
      /* Chisato Summon (8.5s) */
      .chisato-pic {{ opacity: 0; transform-origin: center; animation: slideUpFade 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards 8.5s; }}
      .cursor-final {{ opacity: 0; animation: appear 0.1s forwards 8.5s, blink 1s step-end infinite 8.5s; }}

      /* Keyframes */
      @keyframes reveal {{ from {{ transform: translateX(0); }} to {{ transform: translateX(95px); }} }}
      @keyframes moveCursor {{ from {{ transform: translateX(0); }} to {{ transform: translateX(95px); }} }}
      @keyframes appear {{ to {{ opacity: 1; }} }}
      @keyframes hideCursor {{ to {{ opacity: 0; }} }}
      @keyframes fadeIn {{ from {{ opacity: 0; transform: scale(0.9); }} to {{ opacity: 1; transform: scale(1); }} }}
      @keyframes slideUpFade {{ from {{ opacity: 0; transform: translateY(40px) scale(0.8); }} to {{ opacity: 1; transform: translateY(0) scale(1); }} }}
      @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    </style>
    <clipPath id="circle-clip">
      <circle cx="95" cy="180" r="65" />
    </clipPath>
    <clipPath id="chisato-clip">
      <circle cx="510" cy="350" r="110" />
    </clipPath>
  </defs>

  <!-- Terminal Window Background -->
  <rect width="650" height="480" rx="6" class="bg" />
  <path d="M0 6 a 6 6 0 0 1 6 -6 h 638 a 6 6 0 0 1 6 6 v 24 h -650 z" fill="#2d2d2d" />
  <text x="15" y="20" fill="#fff" font-size="12">C:\\Windows\\System32\\cmd.exe</text>

  <!-- SEQUENCE 1: !profile -->
  <text x="15" y="60" class="cmd-text">@glzzjhn-byte> <tspan fill="#00A2FF">!profile</tspan></text>
  <rect x="155" y="45" width="100" height="20" fill="#0c0c0c" class="reveal-mask" />
  <text x="155" y="60" class="cmd-text cursor-move">_</text>

  <g class="output">
    <text x="190" y="110" fill="#fff" font-weight="bold" font-size="16">John Gabriel Ronao</text>
    <text x="190" y="130" fill="#888">System User</text>
    <text x="190" y="150" fill="#555">========================================</text>
    <text x="190" y="175"><tspan fill="#fff" font-weight="bold">Major:</tspan> Computer Engineering (3rd Year)</text>
    <text x="190" y="195"><tspan fill="#fff" font-weight="bold">Age  :</tspan> 21 Years</text>
    <text x="190" y="215"><tspan fill="#fff" font-weight="bold">Loc  :</tspan> Bicol, Philippines</text>
    <text x="190" y="235"><tspan fill="#fff" font-weight="bold">Dev  :</tspan> Java, C++, Python, Luau</text>
    <text x="190" y="255"><tspan fill="#fff" font-weight="bold">Tasks:</tspan> Forge IDE, NexusPOS, Roblox Dev</text>
    
    <!-- The waiting cursor before the next command -->
    <text x="15" y="300" class="cmd-text">@glzzjhn-byte> <tspan class="cursor-wait">_</tspan></text>
  </g>

  <!-- John Gabriel Profile Picture -->
  <g class="profile-pic">
    <circle cx="95" cy="180" r="68" fill="#555" />
    <image href="{img_src}" x="30" y="115" height="130" width="130" clip-path="url(#circle-clip)" />
  </g>

  <!-- SEQUENCE 2: !LoveLife -->
  <text x="155" y="300" class="cmd-text reveal-mask-2"><tspan fill="#F7DF1E">!LoveLife</tspan></text>
  <rect x="155" y="285" width="100" height="20" fill="#0c0c0c" class="reveal-mask-2" />
  <text x="155" y="300" class="cmd-text cursor-move-2">_</text>

  <!-- The Compile & Error Output -->
  <text x="15" y="335" fill="#888" class="compile-text">> Compiling relationship algorithms...</text>
  <text x="15" y="355" fill="#f44336" font-weight="bold" class="error-text">[FATAL ERROR] 0x404: Partner not found.</text>
  <text x="15" y="375" fill="#00FF00" class="error-text">> Initiating emergency anime fallback...</text>
  <text x="15" y="420" class="cmd-text error-text">@glzzjhn-byte> <tspan class="cursor-final">_</tspan></text>

  <!-- SEQUENCE 3: Chisato Appears -->
  <g class="chisato-pic">
    <circle cx="510" cy="350" r="113" fill="#555" />
    <!-- mix-blend-mode: multiply drops the white background natively! -->
    <image href="{chisato_src}" x="360" y="200" height="300" width="300" preserveAspectRatio="xMidYMid slice" clip-path="url(#chisato-clip)" style="mix-blend-mode: multiply; opacity: 0.9;" />
  </g>
</svg>"""

with open("terminal.svg", "w") as file:
    file.write(svg_content)
print("Successfully generated terminal.svg!")
