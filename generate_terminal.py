import urllib.request
import base64

url1 = "https://github.com/glzzjhn-byte.png"
req1 = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req1) as response:
    b64_img1 = base64.b64encode(response.read()).decode('utf-8')
    img_src = f"data:image/png;base64,{b64_img1}"

gif_src = "https://i.makeagif.com/media/3-14-2024/o9Frsc.gif"

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="650" height="600" viewBox="0 0 650 600">
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
      
      /* GIF Summon (8.5s) */
      .gif-pic {{ opacity: 0; transform-origin: center; animation: slideUpFade 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards 8.5s; }}
      .cursor-final {{ opacity: 0; animation: appear 0.1s forwards 8.5s, blink 1s step-end infinite 8.5s; }}

      /* Keyframes */
      @keyframes reveal {{ from {{ transform: translateX(0); }} to {{ transform: translateX(95px); }} }}
      @keyframes moveCursor {{ from {{ transform: translateX(0); }} to {{ transform: translateX(95px); }} }}
      @keyframes appear {{ to {{ opacity: 1; }} }}
      @keyframes hideCursor {{ to {{ opacity: 0; }} }}
      @keyframes fadeIn {{ from {{ opacity: 0; transform: scale(0.9); }} to {{ opacity: 1; transform: scale(1); }} }}
      @keyframes slideUpFade {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
      @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    </style>
    <clipPath id="circle-clip">
      <circle cx="95" cy="180" r="65" />
    </clipPath>
  </defs>

  <rect width="650" height="600" rx="6" class="bg" />
  <path d="M0 6 a 6 6 0 0 1 6 -6 h 638 a 6 6 0 0 1 6 6 v 24 h -650 z" fill="#2d2d2d" />
  <text x="15" y="20" fill="#fff" font-size="12">C:\\Windows\\System32\\cmd.exe</text>

  <text x="15" y="60" class="cmd-text">@glzzjhn-byte> <tspan fill="#00A2FF">!profile</tspan></text>
  <rect x="155" y="45" width="100" height="
