from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 5900794245
bot_user = "SOURCETBOT"
api_id = 11355889
api_hash = "47fe0ed2db36847839fc57798e62cd26"
session = "BACZj8TIPfskhy03XF3H_OR4I7VUR8ZxaqFTz9Y5GC5NoZTrF5DLffv-Y_GjoTU5jWUPoOGfy2LnF9MtQUBBkvEgxaQqqnakaN2-rbdf5nZwkXi4MTvSOy0SQCb-v-FHuSWU1VXiT_lHx-IDIFMcX7WbHpkrwPjxub75qVn7yGSFYHSqcbe-GLwibIkYc_xjPc25GFEZA-PftG2ZR2ljqAiDcrLfKJRcnIjiO2IEddZlwGl3VnAT-MxAb4Bz4Jtnt2TLjfMkbpTWXXroNV4Vyk_ygZ_c1tZdCigKM47bG8574GDH4nWBb0fKDT0RW569g8UVQ-zRktQWkG-AlAVCcWSGAAAAAWelzXUA"
token = "5696059663:AAHPtR_Twg4Wp6n8xaqePHOUBPdYCMcV-OY"
sudo_command = [5900794245, 5900794245]
pm = "-1001569313780"
mention = "-1001569313780"
plugins = dict(root="plugins")
app = Client("user:Amrsabrrybot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("Amrsabrrybot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
