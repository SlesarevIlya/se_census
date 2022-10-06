from logging import Logger
from typing import NoReturn

from telegram.ext import Application, CommandHandler, InlineQueryHandler

from bot_tg.basic_communication import BasicCommunication
from bot_tg.credentials import bot_token, bot_token_rc
from bot_tg.logger import LogMixin
from bot_tg.who_am_i import WhoAmIConversation


def main() -> NoReturn:
    application = Application.builder().token(bot_token_rc).build()

    logger: Logger = LogMixin().logger
    basic_comm: BasicCommunication = BasicCommunication(logger=logger)
    who_am_i_conv: WhoAmIConversation = WhoAmIConversation(logger=logger)

    application.add_handler(CommandHandler('start', basic_comm.start))
    application.add_handler(CommandHandler('help', basic_comm.help))
    application.add_handler(CommandHandler("myprofile", basic_comm.my_profile))
    application.add_handler(who_am_i_conv.get_handler())
    application.add_handler(InlineQueryHandler(basic_comm.inline_query))

    logger.info("Bot started")
    application.run_polling()


if __name__ == '__main__':
    main()
