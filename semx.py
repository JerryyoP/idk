import time
import os
import pyrogram
    
with pyrogram.Client(
    "pepe", 
    api_id = 2622951,
    api_hash = "52b92d6003747dc2d101cd8f5a081d38") as gensession:
    os.system('clear')
    message_ = f"#STRING_SESSION\n<code>{gensession.export_session_string()} </code>\n\n<b>>> Powered by ThePepeUserbot!</b>"
    gensession.send_message(
        "me",
        message_,
        parse_mode = "html"
    )
    time.sleep(1)
    print(message_)
    print("\nDone! Your string session has successfully been sent to your saved messages section vro ;)\n")
    os.remove("pepe.session")
