import urllib.request
import base64

# 1. Fetch your profile picture and convert it to Base64 code
url = "https://github.com/glzzjhn-byte.png"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    img_data = response.read()
    b64_img = base64.b64encode(img_data).decode('utf-8')
    img_src = f"data:image/png;base64,{b64_img}"

# 2. Build the Animated SVG string
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="650" height="320" viewBox="0 0 650 320">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code&amp;display=swap');
      text {{ font-family: 'Fira Code', Consolas, monospace; font-size: 14.5px; fill: #cccccc; }}
      .bg {{ fill: #0c0c0c; stroke: #444; stroke-width: 2; }}
      .cmd-text {{ fill: #ffffff; }}

      /* Keyframe Animation Timeline */
      .reveal-mask {{ animation: reveal 1s steps(10, end) forwards; }}
      .cursor-move {{ animation: moveCursor 1s steps(10, end) forwards, hideCursor 0.1s forwards 1.5s; }}
      .output {{ opacity: 0; animation: appear 0.1s forwards 1.5s; }}
      .cursor-new {{ opacity: 0; animation: appear 0.1s forwards 1.5s, blink 1s step-end infinite 1.5s; }}
      .profile-pic {{ opacity: 0; transform-origin: 95px 180px; animation: fadeIn 2s forwards 2s; }}

      @keyframes reveal {{ from {{ transform: translateX(0); }} to {{ transform: translateX(90px); }} }}
      @keyframes moveCursor {{ from {{ transform: translateX(0); }} to {{ transform: translateX(90px); }} }}
      @keyframes appear {{ to {{ opacity: 1; }} }}
      @keyframes hideCursor {{ to {{ opacity: 0; }} }}
      @keyframes fadeIn {{ from {{ opacity: 0; transform: scale(0.9); }} to {{ opacity: 1; transform: scale(1); }} }}
      @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    </style>
    <clipPath id="circle-clip">
      <circle cx="95" cy="180" r="65" />
    </clipPath>
  </defs>

  <!-- Terminal Window -->
  <rect width="650" height="320" rx="6" class="bg" />
  <path d="M0 6 a 6 6 0 0 1 6 -6 h 638 a 6 6 0 0 1 6 6 v 24 h -650 z" fill="#2d2d2d" />
  <text x="15" y="20" fill="#fff" font-size="12">C:\\Windows\\System32\\cmd.exe</text>

  <!-- The Typing Sequence -->
  <text x="15" y="60" class="cmd-text">@glzzjhn-byte> <tspan fill="#00A2FF">!profile</tspan></text>
  <!-- Black box that slides off to "reveal" the text -->
  <rect x="155" y="45" width="100" height="20" fill="#0c0c0c" class="reveal-mask" />
  <text x="155" y="60" class="cmd-text cursor-move">_</text>

  <!-- The Profile Stats (Appears at 1.5s) -->
  <g class="output">
    <text x="190" y="110" fill="#fff" font-weight="bold" font-size="16">John Gabriel Ronao</text>
    <text x="190" y="130" fill="#888">System User</text>
    <text x="190" y="150" fill="#555">========================================</text>
    <text x="190" y="175"><tspan fill="#fff" font-weight="bold">Major:</tspan> Computer Engineering (3rd Year)</text>
    <text x="190" y="195"><tspan fill="#fff" font-weight="bold">Age  :</tspan> 21 Years</text>
    <text x="190" y="215"><tspan fill="#fff" font-weight="bold">Loc  :</tspan> Bicol, Philippines</text>
    <text x="190" y="235"><tspan fill="#fff" font-weight="bold">Dev  :</tspan> Java, C++, Python, Luau</text>
    <text x="190" y="255"><tspan fill="#fff" font-weight="bold">Tasks:</tspan> Forge IDE, NexusPOS, Roblox Dev</text>
    
    <text x="15" y="300" class="cmd-text">@glzzjhn-byte> <tspan class="cursor-new">_</tspan></text>
  </g>

  <!-- The Face (Fades in slowly at 2.0s) -->
  <g class="profile-pic">
    <circle cx="95" cy="180" r="68" fill="#555" />
    <image href="{img_src}" x="30" y="115" height="130" width="130" clip-path="url(#circle-clip)" />
  </g>
</svg>"""

with open("terminal.svg", "w") as file:
    file.write(svg_content)
print("Successfully generated terminal.svg!")
