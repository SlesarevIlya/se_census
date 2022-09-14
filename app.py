import logging
from typing import NoReturn

from telegram.ext import (Application, CommandHandler,
                          InlineQueryHandler)

from bot.basic_communication import help, inline_query, my_profile, start
from bot.credentials import bot_token, postgre_creds
from bot.postgre.users import PgUsers
from bot.who_am_i import WhoAmIConversation

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> NoReturn:
    application = Application.builder().token(bot_token).build()

    # application.add_handler(ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER))

    application.add_handler(WhoAmIConversation(pg_conn=PgUsers(pg_creds=postgre_creds), logger=logger).get_handler())
    application.add_handler(CommandHandler("myprofile", my_profile))
    application.add_handler(InlineQueryHandler(inline_query))
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))

    application.run_polling()


if __name__ == '__main__':
    main()
