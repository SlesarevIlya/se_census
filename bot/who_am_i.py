import logging
from typing import List

from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (CommandHandler, ContextTypes, ConversationHandler,
                          MessageHandler, filters)

from bot.entities.user import User


class WhoAmIConversation:
    def __init__(self, pg_conn, logger: logging.Logger):
        self.pg_conn = pg_conn
        self.logger = logger
        self.user = User()

    NAME, BACHELOR_YEAR, MAGISTER_YEAR, COUNTRY, CITY, WORKING_COMPANY, POSITION, LINKEDIN, INST, HOBBIES = range(10)

    def get_handler(self):
        return ConversationHandler(
            entry_points=[CommandHandler("whoami", self.start),
                          CommandHandler("cancel", self.cancel)],
            states={
                self.NAME: [MessageHandler(filters=filters.ALL, callback=self.name)],
                self.BACHELOR_YEAR: [MessageHandler(filters=filters.ALL, callback=self.bachelor_year)],
                self.MAGISTER_YEAR: [MessageHandler(filters=filters.ALL, callback=self.magister_year)],
                self.COUNTRY: [MessageHandler(filters=filters.Regex("[^0]"), callback=self.country),
                               MessageHandler(filters=filters.Regex("0"), callback=self.city)],
                self.CITY: [MessageHandler(filters=filters.ALL, callback=self.city)],
                self.WORKING_COMPANY: [MessageHandler(filters=filters.Regex("[^0]"), callback=self.working_company),
                                       MessageHandler(filters=filters.Regex("0"), callback=self.position)],
                self.POSITION: [MessageHandler(filters=filters.ALL, callback=self.position)],
                self.LINKEDIN: [MessageHandler(filters=filters.ALL, callback=self.linkedin)],
                self.INST: [MessageHandler(filters=filters.ALL, callback=self.instagram)],
                self.HOBBIES: [MessageHandler(filters=filters.ALL, callback=self.hobbies)]
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
            # TODO return before merge
            conversation_timeout=60,
            allow_reentry=True
        )

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        user = update.message.from_user
        self.logger.info(f"Start dialog for {user.name}")

        self.user.name = user.name
        await update.message.reply_text(f"[{self.NAME}]: Pls introduce yourself in English!\n"
                                        f"like: Name Surname")
        return self.NAME

    async def name(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        name_arr: List[str] = update.message.text.split()
        if len(name_arr) == 1:
            self.user.first_name = name_arr[0]
        else:
            self.user.first_name, self.user.last_name = name_arr
        self.user.id = update.message.from_user.id
        self.logger.info(f"{self.user.name} name: {self.user.first_name} {self.user.last_name}")

        await update.message.reply_text(f"[{self.BACHELOR_YEAR}]: Graduating bachelor year? (0 - if not applicable)")
        return self.BACHELOR_YEAR

    async def bachelor_year(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.bachelor_year = update.message.text
        self.logger.info(f"{self.user.name} bachelor_year: {self.user.bachelor_year}")

        await update.message.reply_text(f"[{self.MAGISTER_YEAR}]: Graduating magister year? (0 - if not applicable)")
        return self.MAGISTER_YEAR

    async def magister_year(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.magister_year = update.message.text
        self.logger.info(f"{self.user.name} magister_year: {self.user.magister_year}")

        await update.message.reply_text(f"[{self.COUNTRY}]: Current location country? (0 - if you're shy)")
        return self.COUNTRY

    async def country(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.country = update.message.text
        self.logger.info(f"{self.user.name} current location country: {self.user.country}")

        await update.message.reply_text(f"[{self.CITY}]: Current location city? (0 - if you're shy)")
        return self.CITY

    async def city(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.city = update.message.text
        self.logger.info(f"{self.user.name} current location city: {self.user.city}")

        await update.message.reply_text(f"[{self.WORKING_COMPANY}]: Working company? (0 - if you're shy)")
        return self.WORKING_COMPANY

    async def working_company(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.company = update.message.text
        self.logger.info(f"{self.user.name} working company: {self.user.company}")

        await update.message.reply_text(
            f"[{self.POSITION}]: Role in the company? (0 - if you're not sure that it's important)")
        return self.POSITION

    async def position(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.position = update.message.text
        self.logger.info(f"{self.user.name} position: {self.user.position}")

        await update.message.reply_text(f"[{self.LINKEDIN}]: linkedin url? (0 - if you're shy)")
        return self.LINKEDIN

    async def linkedin(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.linkedin = update.message.text
        self.logger.info(f"{self.user.name} linkedin: {self.user.linkedin}")

        await update.message.reply_text(f"[{self.INST}]: instagram url? (0 - if you're shy)")
        return self.INST

    async def instagram(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.instagram = update.message.text
        self.logger.info(f"{self.user.name} instagram: {self.user.instagram}")

        await update.message.reply_text(f"[{self.HOBBIES}]: hobbies? via commas pls! (0 - if you're shy)")
        return self.HOBBIES

    async def hobbies(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.user.hobbies = update.message.text
        self.logger.info(f"{self.user.name} hobbies: {self.user.hobbies}")

        await update.message.reply_text("Thanks, it's great!")
        self.logger.info(self.user)
        self.pg_conn.insert_user(self.user)
        return ConversationHandler.END

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.logger.info(f"User {self.user.name} canceled the conversation.")
        await update.message.reply_text(
            "Ok, see you", reply_markup=ReplyKeyboardRemove()
        )

        return ConversationHandler.END
