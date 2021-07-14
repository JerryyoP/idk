import time
import os
import pyrogram
    
with pyrogram.Client(
    "pepe", 
    api_id = 1273127,
    api_hash = "2626aee4ea587947c6a703f1a0d6a3cc") as gensession:
    os.system('clear')
    message_ = f"#STRING_SESSION\n<code>{gensession.export_session_string()} </code>\n\n<b>>> Powered by ThePepeUserbot!</b>"
    gensession.send_message(
        "me",
        message_,
        parse_mode = "html"
    )
    time.sleep(1) 
    print("\nDone! Your string session has successfully been sent to your saved messages section vro ;)\n")
