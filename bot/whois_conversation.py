import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (CallbackContext, ChatMemberHandler, CommandHandler,
                          ContextTypes, ConversationHandler, MessageHandler,
                          filters)


class WhoIsConversation:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    ISSUE_YEAR, CURRENT_LOCATION, COMPANY, POSITION, REF_POSSIBILITIES, HOBBIES = range(6)

    async def whoami(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        print("whoami")

        await update.message.reply_text(
            "Let's start. What is your FINAL university graduation year? If you have both (bac and mag) pls choose one")

        return self.ISSUE_YEAR

    async def current_location(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        print("current_location")
        user = update.message.from_user
        self.logger.info(f"graduation year of {user.first_name}: {update.message.text}")
        await update.message.reply_text("What is your current leaving location? Or just send 'skip'", )

        return self.CURRENT_LOCATION

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        print("cancel")

        user = update.message.from_user
        self.logger.info(f"User {user.first_name} canceled the conversation.")
        await update.message.reply_text(
            "Ok, see you", reply_markup=ReplyKeyboardRemove()
        )

        return ConversationHandler.END

# ChatMemberHandler.MY_CHAT_MEMBER
# def whois(update: Update, context: CallbackContext) -> NoReturn:
#     a = 4
#     user_login = update.message.from_user.name
#     chat_members_count = update.effective_chat.get_members_count()
#
#     """Starts the conversation and asks the user about their gender."""
#     reply_keyboard = [["Boy", "Girl", "Other"]]
#
#     update.message.reply_text(
#         "Hi! My name is Professor Bot. I will hold a conversation with you. "
#         "Send /cancel to stop talking to me.\n\n"
#         "Are you a boy or a girl?",
#         reply_markup=ReplyKeyboardMarkup(
#             reply_keyboard, one_time_keyboard=True, input_field_placeholder="Boy or Girl?"
#         ),
#     )
#     update.message.reply_text("Hi SE participant!")
#     a = 5


# async def whoami(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Starts the conversation and asks the user about their gender."""
#     reply_keyboard = [["Boy", "Girl", "Other"]]
#
#     await update.message.reply_text(
#         "test",
#         reply_markup=ReplyKeyboardMarkup(
#             reply_keyboard, one_time_keyboard=True, input_field_placeholder="Boy or Girl?"
#         ),
#     )
