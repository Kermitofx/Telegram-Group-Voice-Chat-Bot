from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""
TeleRadioBr ™ (Group Music Bot) 
Telegram UserBot para reproduzir áudio em bate-papos de voz do Telegram 🔊

**Todos os usuários**
/play <song name> - tocar a música que você solicitou
/dplay <song name> - tocar a música que você solicitou via deezer
/splay <song name> - tocar a música que você solicitou via jio saavn
/playlist - Mostre agora lista de reprodução
/current - Mostre agora tocar
/song <song name> - baixe as músicas que você deseja rapidamente
/search <query> - procure vídeos no youtube com detalhes
/deezer <song name> - baixe as músicas que você deseja rapidamente via deezer
/saavn <song name> - baixe as músicas que você deseja rapidamente via saavn
/video <song name> - baixe os vídeos que você deseja rapidamente

**Apenas administradoresy**
/player - abrir o painel de configurações do music player
/pause - pausar a reprodução da música
/resume - retomar a reprodução da música
/skip - tocar a próxima música
/end - pare de tocar música
/userbotjoin - convide assistente para o seu chat
/userbotleave - remover assistente de seu bate-papo
/admincache - Atualizar lista de administração

©2021 @YakkaAdaviyaMusicBot Bot All Rights Reserved
""",
        reply_markup=InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                             text=" 👪 Grupo de suporte de bots ",
                             url="https://t.me/TeleRadioBrazil"),
                         InlineKeyboardButton(
                             text=" 🔔 Canal de atualização de bot ",
                             url="https://t.me/TeleRadiobr ")
     oBrazil")
                    ],
                    [
                        InlineKeyboardButton(
                             text=" 👺 Grupo Do Dexty  ",
                             url="https://t.me/TheRealVibes"),
                         InlineKeyboardButton(
                             text=" 👹 Canal Do Dexty ",
                             url="https://t.me/DextyLixo")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" ⚡️ Desenvolvedor ",
                             url="https://t.me/TioDexty") 
                    
                    ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""
        @TeleRadio (Group Music Bot) 💫👹\n\nTelegram UserBot para reproduzir áudio em bate-papos de voz do Telegram 🔊\n\n©2021 @MusicaCallsbot Bot todos os direitos reservados
        """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "️Iniciar o bot", url="https://t.me/MusicaCallsbot")
                ]
            ]
        )
   )
