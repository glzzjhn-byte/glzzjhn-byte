import base64
import urllib.request

url1 = "https://github.com/glzzjhn-byte.png"
req1 = urllib.request.Request(url1, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req1) as response:
  b64_img1 = base64.b64encode(response.read()).decode("utf-8")
  img_src = f"data:image/png;base64,{b64_img1}"

url_logo = "https://i.postimg.cc/kXLj3Gjq/logo.png"
req_logo = urllib.request.Request(
    url_logo, headers={"User-Agent": "Mozilla/5.0"}
)
with urllib.request.urlopen(req_logo) as response:
  b64_logo = base64.b64encode(response.read()).decode("utf-8")
  logo_src = f"data:image/png;base64,{b64_logo}"

url2 = "https://i.makeagif.com/media/3-14-2024/o9Frsc.gif"
req2 = urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req2) as response:
  b64_img2 = base64.b64encode(response.read()).decode("utf-8")
  gif_src = f"data:image/gif;base64,{b64_img2}"

svg_template = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="680" height="640"'
    ' viewBox="0 0 680 640">\n'
    "  <defs>\n"
    "    <style>\n"
    "      @import"
    " url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&amp;display=swap');\n"
    "      text { font-family: 'Fira Code', Consolas, monospace;"
    " font-size: 13.5px; fill: #cccccc; }\n"
    '      .bg { fill: #0c0c0c; stroke: #333; stroke-width: 1.5; }\n'
    "      .cmd-text { fill: #ffffff; }\n"
    "      .accent { fill: #00A2FF; font-weight: 600; }\n"
    "      .gold { fill: #FFB300; font-weight: 600; }\n"
    "      .dim { fill: #777777; }\n"
    "\n"
    "      /* Timeline 1: !profile (0s to 3s) */\n"
    "      .reveal-mask { animation: reveal 1s steps(10, end) forwards; }\n"
    "      .cursor-move { animation: moveCursor 1s steps(10, end) forwards,"
    " hideCursor 0.1s forwards 1.5s; }\n"
    "      .output { opacity: 0; animation: appear 0.1s forwards 1.5s; }\n"
    "      .avatars { opacity: 0; animation: fadeIn 1.2s forwards 1.8s; }\n"
    "      .cursor-wait { opacity: 0; animation: appear 0.1s forwards 1.5s,"
    " blink 1s step-end 2.5, hideCursor 0.1s forwards 4s; }\n"
    "\n"
    "      /* Timeline 2: !LoveLife (4s to 8s) */\n"
    "      .text-appear-2 { opacity: 0; animation: appear 0.1s forwards 4s; }\n"
    "      .reveal-mask-2 { opacity: 0; animation: appear 0.1s forwards 4s,"
    " reveal 1s steps(9, end) forwards 4s; }\n"
    "      .cursor-move-2 { opacity: 0; animation: appear 0.1s forwards 4s,"
    " moveCursor 1s steps(9, end) forwards 4s, hideCursor 0.1s forwards 5.5s;"
    " }\n"
    "      .compile-text { opacity: 0; animation: appear 0.1s forwards 5.5s;"
    " }\n"
    "      .error-text { opacity: 0; animation: appear 0.1s forwards 7s; }\n"
    "\n"
    "      /* GIF Summon (8.5s) */\n"
    "      .gif-pic { opacity: 0; transform-origin: center; animation:"
    " slideUpFade 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards 8.5s;"
    " }\n"
    "      .cursor-final { opacity: 0; animation: appear 0.1s forwards 8.5s,"
    " blink 1s step-end infinite 8.5s; }\n"
    "\n"
    "      /* Keyframes */\n"
    "      @keyframes reveal { from { transform: translateX(0); } to {"
    " transform: translateX(95px); } }\n"
    "      @keyframes moveCursor { from { transform: translateX(0); } to {"
    " transform: translateX(95px); } }\n"
    "      @keyframes appear { to { opacity: 1; } }\n"
    "      @keyframes hideCursor { to { opacity: 0; } }\n"
    "      @keyframes fadeIn { from { opacity: 0; transform: scale(0.95); } to"
    " { opacity: 1; transform: scale(1); } }\n"
    "      @keyframes slideUpFade { from { opacity: 0; transform:"
    " translateY(15px); } to { opacity: 1; transform: translateY(0); } }\n"
    "      @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }\n"
    "    </style>\n"
    "\n"
    "    <!-- Circular Clips for Profile and Studio Logo -->\n"
    '    <clipPath id="user-clip">\n'
    '      <circle cx="55" cy="145" r="40" />\n'
    "    </clipPath>\n"
    '    <clipPath id="studio-clip">\n'
    '      <circle cx="55" cy="235" r="40" />\n'
    "    </clipPath>\n"
    "  </defs>\n"
    "\n"
    "  <!-- Terminal Background & Header Bar -->\n"
    '  <rect width="680" height="640" rx="8" class="bg" />\n'
    '  <path d="M0 8 a 8 8 0 0 1 8 -8 h 664 a 8 8 0 0 1 8 8 v 24 h -680 z"'
    ' fill="#1e1e1e" />\n'
    '  <circle cx="18" cy="16" r="5" fill="#ff5f56" />\n'
    '  <circle cx="34" cy="16" r="5" fill="#ffbd2e" />\n'
    '  <circle cx="50" cy="16" r="5" fill="#27c93f" />\n'
    '  <text x="70" y="20" fill="#999" font-size="12">glzzjhn-byte@system:'
    " ~ (cmd.exe)</text>\n"
    "\n"
    "  <!-- SEQUENCE 1: !profile -->\n"
    '  <text x="15" y="60" class="cmd-text">@glzzjhn-byte&gt; <tspan'
    ' class="accent">!profile</tspan></text>\n'
    '  <rect x="150" y="45" width="105" height="20" fill="#0c0c0c"'
    ' class="reveal-mask" />\n'
    '  <text x="150" y="60" class="cmd-text cursor-move">_</text>\n'
    "\n"
    "  <!-- Output Profile Block -->\n"
    '  <g class="output">\n'
    '    <text x="115" y="110" fill="#fff" font-weight="bold"'
    ' font-size="16">John Gabriel Ronao</text>\n'
    '    <text x="115" y="128" class="gold">Founder &amp; Lead Architect'
    " @ GlzzLexi Studios</text>\n"
    '    <text x="115" y="145"'
    ' class="dim">====================================================</text>\n'
    '    <text x="115" y="165"><tspan fill="#fff"'
    ' font-weight="bold">Major:</tspan> Computer Engineering (3rd'
    " Year)</text>\n"
    '    <text x="115" y="185"><tspan fill="#fff"'
    ' font-weight="bold">Studio:</tspan> GlzzLexi (<tspan fill="#00A2FF">Roblox'
    " Engine &amp; Systems</tspan>)</text>\n"
    '    <text x="115" y="205"><tspan fill="#fff"'
    ' font-weight="bold">Focus:</tspan> Wrapper Games, Obby, FPS, Survival'
    " Sim</text>\n"
    '    <text x="115" y="225"><tspan fill="#fff" font-weight="bold">Dev'
    "  :</tspan> Luau, Java, C++, Python, PHP</text>\n"
    '    <text x="115" y="245"><tspan fill="#fff"'
    ' font-weight="bold">Tasks:</tspan> studious-spoon, Forge IDE, NexusPOS'
    " Dev</text>\n"
    '    <text x="15" y="315" class="cmd-text">@glzzjhn-byte&gt; <tspan'
    ' class="cursor-wait">_</tspan></text>\n'
    "  </g>\n"
    "\n"
    "  <!-- Side Avatar & Studio Badges -->\n"
    '  <g class="avatars">\n'
    "    <!-- User Avatar -->\n"
    '    <circle cx="55" cy="145" r="42" fill="#00A2FF" opacity="0.6" />\n'
    '    <image href="__IMG_SRC__" x="15" y="105" height="80" width="80"'
    ' clip-path="url(#user-clip)" />\n'
    '    <text x="55" y="198" font-size="10" fill="#888"'
    ' text-anchor="middle">FOUNDER</text>\n'
    "\n"
    "    <!-- Studio Logo (PostImage) -->\n"
    '    <circle cx="55" cy="235" r="42" fill="#FFB300" opacity="0.6" />\n'
    '    <image href="__LOGO_SRC__" x="15" y="195" height="80" width="80"'
    ' clip-path="url(#studio-clip)" />\n'
    '    <text x="55" y="288" font-size="10" fill="#FFB300"'
    ' text-anchor="middle">GLZZLEXI</text>\n'
    "  </g>\n"
    "\n"
    "  <!-- SEQUENCE 2: !LoveLife -->\n"
    '  <text x="150" y="315" class="cmd-text text-appear-2"><tspan'
    ' class="accent">!LoveLife</tspan></text>\n'
    '  <rect x="150" y="300" width="105" height="20" fill="#0c0c0c"'
    ' class="reveal-mask-2" />\n'
    '  <text x="150" y="315" class="cmd-text cursor-move-2">_</text>\n'
    "\n"
    "  <!-- Error Output -->\n"
    '  <text x="15" y="350" fill="#f44336" class="compile-text">&gt;'
    " Compiling relationship algorithms...</text>\n"
    '  <text x="15" y="372" fill="#f44336" font-weight="bold"'
    ' class="error-text">[FATAL ERROR] 0x404: Partner not found.</text>\n'
    '  <text x="15" y="394" fill="#f44336" class="error-text">&gt; Initiating'
    " emergency anime fallback...</text>\n"
    "\n"
    "  <!-- SEQUENCE 3: GIF -->\n"
    '  <g class="gif-pic">\n'
    '    <image href="__GIF_SRC__" x="15" y="415" width="310" height="175"'
    ' preserveAspectRatio="xMinYMin meet" />\n'
    "  </g>\n"
    "\n"
    "  <!-- Final Prompt -->\n"
    '  <text x="15" y="620" class="cmd-text error-text">@glzzjhn-byte&gt; <tspan'
    ' class="cursor-final">_</tspan></text>\n'
    "</svg>"
)

svg_content = (
    svg_template.replace("__IMG_SRC__", img_src)
    .replace("__LOGO_SRC__", logo_src)
    .replace("__GIF_SRC__", gif_src)
)

with open("system_terminal_v3.svg", "w", encoding="utf-8") as file:
  file.write(svg_content)

print(
    "Successfully generated updated system_terminal_v3.svg with GlzzLexi Logo!"
)
