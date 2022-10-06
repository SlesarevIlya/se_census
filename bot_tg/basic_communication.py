import logging
from typing import NoReturn, List
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import CallbackContext, ContextTypes

from bot_tg.entities.table_factory import TableFactory
from bot_tg.entities.user import User
from bot_tg.postgres.tables.users import TableUsers


class BasicCommunication:
    def __init__(self, logger: logging.Logger):
        self.table_factory: TableFactory = TableFactory()
        self.logger = logger

    async def start(self, update: Update, context: CallbackContext):
        users: TableUsers = self.table_factory.get_table("users")
        users.insert_record(User(id=update.message.from_user.id))
        await update.message.reply_text("Hi SE participant!")

    async def help(self, update: Update, context: CallbackContext):
        await update.message.reply_text("WTF am I doing?? Help yourself!")

    async def my_profile(self, update: Update, context: CallbackContext):
        users: TableUsers = self.table_factory.get_table("users")
        users_meta: List[str] = [user.full_meta() for user in
                                 users.get_record_by_name(name=update.message.from_user.name,
                                                          substring=False)]
        if len(users_meta) > 0 and len(users_meta[0]) > 0:
            response_msg: str = users_meta[0]
        elif len(users_meta) > 0:
            response_msg: str = "Your profile is empty!"
        else:
            response_msg: str = "We didn't find your profile. Sorry!"

        await update.message.reply_text(text=response_msg)

    # TODO didn't test it yet
    async def inline_query(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> NoReturn:
        query = update.inline_query.query

        if query == "":
            return

        users: TableUsers = self.table_factory.get_table("users")
        results = [InlineQueryResultArticle(id=str(uuid4()),
                                            title=user.full_name(),
                                            input_message_content=InputTextMessageContent(user.full_meta()),
                                            description=user.description())
                   for user in users.get_record_by_name(name=query,
                                                        substring=True)]

        await update.inline_query.answer(results)
