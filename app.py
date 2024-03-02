import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone https://github.com/MCRen88/ai_brush_art /home/xlab-app-center/ai_brush_art")
os.chdir(f"/home/xlab-app-center/ai_brush_art")
os.system(f"git lfs install")
os.system(f"git reset --hard")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/71392 -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o chilloutworld_v15.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/sdxl-refiner-1.0/weight//sd_xl_refiner_1.0.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o sd_xl_refiner_1.0.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/cyber-realistic/weight//cyberrealistic_v32.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o cyberrealistic_v32.safetensors")
os.system(f"python launch.py --cors-allow-origins=* --xformers --enable-insecure-extension-access --theme dark --gradio-queue --disable-safe-unpickle --ui-settings-file /home/xlab-app-center/config.json --ui-config-file /home/xlab-app-center/ui-config.json")
