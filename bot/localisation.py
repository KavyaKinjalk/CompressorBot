#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, \n\nI am made to compress video files. Send me any file and i will compress it.</b> \n\n/help for more details... \n\n"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = " Downloading... \n"
    
    UPLOAD_START = " Uploading...  \n"
    
    COMPRESS_START = "Compressing..."
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "Downloaded in {}\n\n Compressed in {}\n\n Uploaded in {}"

    COMPRESS_PROGRESS = " ETA: {}\n Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = " Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = " Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = " Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "wrong format bruh\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = " Already One Process going on. \n or \n A media already exists. \n  Please send /cancel to delete existing media. "
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "By now you must have known what I do. Let me tell you the commands. \n\n1. Send me a telegram file which you want to compress (either Forward or upload it.) \n2. Reply the file - /compress And Persentage \nEg:- <code>/compress 75</code> With this command, a 1000MB File Will be converted into 750MB.  \n\n"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
