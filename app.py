import logging
from typing import NoReturn

from telegram.ext import Application, CommandHandler, InlineQueryHandler

from bot.basic_communication import BasicCommunication
from bot.credentials import bot_token, postgre_creds
from bot.postgre.users import PgUsers
from bot.who_am_i import WhoAmIConversation

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> NoReturn:
    application = Application.builder().token(bot_token).build()

    pg_client: PgUsers = PgUsers(pg_creds=postgre_creds)

    basic_comm: BasicCommunication = BasicCommunication(pg_conn=pg_client,
                                                        logger=logger)
    who_am_i_conv: WhoAmIConversation = WhoAmIConversation(pg_conn=pg_client,
                                                           logger=logger)

    application.add_handler(who_am_i_conv.get_handler())
    application.add_handler(CommandHandler("myprofile", basic_comm.my_profile))
    application.add_handler(InlineQueryHandler(basic_comm.inline_query))
    application.add_handler(CommandHandler('start', basic_comm.start))
    application.add_handler(CommandHandler('help', basic_comm.help))

    application.run_polling()


if __name__ == '__main__':
    main()
