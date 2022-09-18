import logging
from typing import NoReturn
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import CallbackContext, ContextTypes

from bot.credentials import postgre_creds
from bot.postgre.users import PgUsers


class BasicCommunication:
    def __init__(self, pg_conn, logger: logging.Logger):
        self.pg_conn = pg_conn
        self.logger = logger

    async def start(self, update: Update, context: CallbackContext):
        await update.message.reply_text("Hi SE participant!")

    async def help(self, update: Update, context: CallbackContext):
        await update.message.reply_text("WTF am I doing?? Help yourself!")

    async def my_profile(self, update: Update, context: CallbackContext):
        pg_conn = PgUsers(pg_creds=postgre_creds)
        user_meta = [user.full_meta() for user in pg_conn.get_users_by_name(name=update.message.from_user.name,
                                                                            substring=False)]
        await update.message.reply_text(text=user_meta[0])

    async def inline_query(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> NoReturn:
        query = update.inline_query.query

        if query == "":
            return

        pg_conn = PgUsers(pg_creds=postgre_creds)
        results = [InlineQueryResultArticle(id=str(uuid4()),
                                            title=user.full_name(),
                                            input_message_content=InputTextMessageContent(user.full_meta()),
                                            description=user.description())
                   for user in pg_conn.get_users_by_name(name=query,
                                                         substring=True)]

        await update.inline_query.answer(results)
