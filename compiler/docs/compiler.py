#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import ast
import os
import re
import shutil

HOME = "compiler/docs"
DESTINATION = "docs/source/telegram"
PYROGRAM_API_DEST = "docs/source/api"

FUNCTIONS_PATH = "pyrogram/raw/functions"
TYPES_PATH = "pyrogram/raw/types"
BASE_PATH = "pyrogram/raw/base"

FUNCTIONS_BASE = "functions"
TYPES_BASE = "types"
BASE_BASE = "base"


def snek(s: str):
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def generate(source_path, base):
    all_entities = {}

    def build(path, level=0):
        last = path.split("/")[-1]

        for i in os.listdir(path):
            try:
                if not i.startswith("__"):
                    build("/".join([path, i]), level=level + 1)
            except NotADirectoryError:
                with open(path + "/" + i, encoding="utf-8") as f:
                    p = ast.parse(f.read())

                for node in ast.walk(p):
                    if isinstance(node, ast.ClassDef):
                        name = node.name
                        break
                else:
                    continue

                full_path = os.path.basename(path) + "/" + snek(name).replace("_", "-") + ".rst"

                if level:
                    full_path = base + "/" + full_path

                namespace = path.split("/")[-1]
                if namespace in ["base", "types", "functions"]:
                    namespace = ""

                full_name = f"{(namespace + '.') if namespace else ''}{name}"

                os.makedirs(os.path.dirname(DESTINATION + "/" + full_path), exist_ok=True)

                with open(DESTINATION + "/" + full_path, "w", encoding="utf-8") as f:
                    f.write(
                        page_template.format(
                            title=full_name,
                            title_markup="=" * len(full_name),
                            full_class_path="pyrogram.raw.{}".format(
                                ".".join(full_path.split("/")[:-1]) + "." + name
                            )
                        )
                    )

                if last not in all_entities:
                    all_entities[last] = []

                all_entities[last].append(name)

    build(source_path)

    for k, v in sorted(all_entities.items()):
        v = sorted(v)
        entities = []

        for i in v:
            entities.append(f'{i} <{snek(i).replace("_", "-")}>')

        if k != base:
            inner_path = base + "/" + k + "/index" + ".rst"
            module = "pyrogram.raw.{}.{}".format(base, k)
        else:
            for i in sorted(list(all_entities), reverse=True):
                if i != base:
                    entities.insert(0, "{0}/index".format(i))

            inner_path = base + "/index" + ".rst"
            module = "pyrogram.raw.{}".format(base)

        with open(DESTINATION + "/" + inner_path, "w", encoding="utf-8") as f:
            if k == base:
                f.write(":tocdepth: 1\n\n")
                k = "Raw " + k

            f.write(
                toctree.format(
                    title=k.title(),
                    title_markup="=" * len(k),
                    module=module,
                    entities="\n    ".join(entities)
                )
            )

            f.write("\n")


def pyrogram_api():
    def get_title_list(s: str) -> list:
        return [i.strip() for i in [j.strip() for j in s.split("\n") if j] if i]

    # Methods

    categories = dict(
        utilities="""
        Utilities
            run
            start
            stop
            restart
            export_session_string
            add_handler
            remove_handler
            stop_transmission
            set_parse_mode
        """,
        authorization="""
        Authorization
            initialize
            sign_up
            accept_terms_of_service
            sign_in
            sign_in_bot
            connect
            send_code
            resend_code
            recover_password
            send_recovery_code
            get_password_hint
            check_password
            log_out
            disconnect
            terminate
            get_me
            get_active_sessions
            terminate_session
            terminate_all_other_sessions
        """,
        messages="""
        Messages
            send_message
            forward_messages
            copy_message
            send_photo
            send_audio
            send_document
            send_video
            send_animation
            send_voice
            send_video_note
            send_cached_media
            send_paid_media
            send_media_group
            get_media_group
            copy_media_group
            send_location
            send_venue
            send_contact
            send_poll
            send_dice
            send_chat_action
            add_paid_message_reaction
            set_reaction
            download_media
            stream_media
            edit_message_text
            edit_inline_text
            edit_message_caption
            edit_inline_caption
            edit_message_media
            edit_inline_media
            edit_message_reply_markup
            edit_inline_reply_markup
            edit_cached_media
            stop_poll
            delete_messages
            get_chat_sponsored_messages
            get_chat_history
            get_chat_history_count
            read_chat_history
            get_messages
            get_chat_pinned_message
            get_callback_query_message
            get_replied_message
            view_messages
            get_discussion_message
            get_discussion_replies
            get_discussion_replies_count
            search_global
            search_global_count
            search_messages
            search_messages_count
            search_public_messages_by_tag
            count_public_messages_by_tag
            vote_poll
            retract_vote
            translate_text
            translate_message_text
        """,
        chats="""
        Chats
            ban_chat_member
            unban_chat_member
            restrict_chat_member
            promote_chat_member
            set_administrator_title
            set_chat_permissions
            set_chat_photo
            delete_chat_photo
            set_chat_title
            set_chat_description
            pin_chat_message
            unpin_chat_message
            unpin_all_chat_messages
            search_chats
            join_chat
            leave_chat
            get_chat
            get_chat_members
            get_chat_members_count
            get_chat_member
            
            get_dialogs
            get_dialogs_count
            set_chat_username
            get_nearby_chats
            archive_chats
            unarchive_chats
            add_chat_members
            create_channel
            create_group
            create_supergroup
            delete_channel
            delete_supergroup
            delete_user_history
            set_slow_mode
            set_chat_message_auto_delete_time
            mark_chat_unread
            get_chat_event_log
            get_chat_online_count
            get_send_as_chats
            set_send_as_chat
            set_chat_protected_content
            get_created_chats
            transfer_chat_ownership
        """,
        invite_links="""
        Invite Links
            export_chat_invite_link
            create_chat_invite_link
            edit_chat_invite_link
            revoke_chat_invite_link
            get_chat_admin_invite_links
            get_chat_admin_invite_links_count
            get_chat_admins_with_invite_links
            get_chat_invite_link
            get_chat_invite_link_joiners
            get_chat_invite_link_joiners_count
            delete_chat_invite_link
            delete_chat_admin_invite_links
            get_chat_join_requests
            approve_chat_join_request
            approve_all_chat_join_requests
            decline_chat_join_request
            decline_all_chat_join_requests            
        """,
        chat_topics="""
        Chat Forum Topics
            get_forum_topic_icon_stickers
            create_forum_topic
            edit_forum_topic
            close_forum_topic
            reopen_forum_topic
            delete_forum_topic
            hide_forum_topic
            unhide_forum_topic
            get_forum_topics
            get_forum_topic
            toggle_forum_topic_is_pinned
        """,
        users="""
        Users
            get_chat_photos
            get_chat_photos_count
            get_users
            
            set_profile_photo
            delete_profile_photos
            set_username
            update_profile
            block_user
            unblock_user
            get_common_chats
            get_default_emoji_statuses
            set_emoji_status
            set_birthdate
            set_personal_chat
            delete_account
            update_status
        """,
        contacts="""
        Contacts
            add_contact
            delete_contacts
            import_contacts
            get_contacts
            get_contacts_count
        """,
        password="""
        Password
            enable_cloud_password
            change_cloud_password
            remove_cloud_password
        """,
        bots="""
        Bots
            answer_callback_query
            request_callback_answer
            set_bot_commands
            delete_bot_commands
            get_bot_commands
            set_bot_name
            get_bot_name
            set_bot_info_description
            get_bot_info_description
            set_bot_info_short_description
            get_bot_info_short_description
            set_chat_menu_button
            get_chat_menu_button
            set_bot_default_privileges
            get_bot_default_privileges
            send_game
            set_game_score
            get_game_high_scores
            answer_inline_query
            get_inline_bot_results
            send_inline_bot_result
            answer_web_app_query
            send_web_app_custom_request
            get_owned_bots
            get_similar_bots
        """,
        phone="""
        Phone
            create_video_chat
            discard_group_call
            get_video_chat_rtmp_url
            invite_group_call_participants
            load_group_call_participants
        """,
        stickers="""
        Stickers
            send_sticker
            get_custom_emoji_stickers
            get_message_effects
            get_stickers
        """,
        stories="""
        Stories
            get_stories
        """,
        payments="""
        Payments
            send_invoice
            create_invoice_link
            answer_shipping_query
            answer_pre_checkout_query
            refund_star_payment
            get_business_connection
            get_collectible_item_info
            get_payment_form
            send_payment_form
            get_available_gifts
            get_received_gifts
            sell_gift
            send_gift
            toggle_gift_is_saved
            get_owned_star_count
        """,
        advanced="""
        Advanced
            invoke
            resolve_peer
            get_file
            save_file
        """
    )

    root = PYROGRAM_API_DEST + "/methods"

    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    with open(HOME + "/template/methods.rst") as f:
        template = f.read()

    with open(root + "/index.rst", "w") as f:
        fmt_keys = {}

        for k, v in categories.items():
            name, *methods = get_title_list(v)
            fmt_keys.update({k: "\n    ".join("{0} <{0}>".format(m) for m in methods)})

            for method in methods:
                with open(root + "/{}.rst".format(method), "w") as f2:
                    title = "{}()".format(method)

                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. automethod:: pyrogram.Client.{}()".format(method))

            functions = ["idle", "compose"]

            for func in functions:
                with open(root + "/{}.rst".format(func), "w") as f2:
                    title = "{}()".format(func)

                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. autofunction:: pyrogram.{}()".format(func))

        f.write(template.format(**fmt_keys))

    # Types

    categories = dict(
        users_chats="""
        Users & Chats
            Birthdate
            User
            Chat
            Username
            ChatShared
            WriteAccessAllowed
            UsersShared
            ChatAdminWithInviteLinks
            ChatColor
            ChatEvent
            ChatEventFilter
            ChatInviteLink
            ChatJoiner
            ChatJoinRequest
            ChatMember
            ChatMemberUpdated
            ChatPermissions
            ChatPhoto
            ChatPrivileges
            ChatReactions
            VideoChatScheduled
            VideoChatStarted
            VideoChatEnded
            VideoChatParticipantsInvited
            Dialog
            EmojiStatus
            GroupCallParticipant
            InviteLinkImporter
            Restriction
            RtmpUrl
        """,
        messages_media="""
        Messages & Media
            Message
            MessageEntity
            TextQuote
            ExternalReplyInfo
            ReplyParameters
            MessageOrigin
            MessageOriginUser
            MessageOriginHiddenUser
            MessageOriginChat
            MessageOriginChannel
            MessageImportInfo
            Photo
            AlternativeVideo
            Animation
            Audio
            Document
            Story
            Video
            VideoNote
            Voice
            PaidMediaInfo
            PaidMedia
            PaidMediaPreview
            PaidMediaPhoto
            PaidMediaVideo
            Contact
            Dice
            PollOption
            InputPollOption
            Poll
            PollAnswer
            Location
            Venue
            Gift
            ReceivedGift
            UpgradedGift
            WebAppData
            MessageAutoDeleteTimerChanged
            ChatBoostAdded
            ChatBackground
            Game
            GiftCode
            GiftedPremium
            GiftedStars
            Giveaway
            GiveawayCreated
            GiveawayCompleted
            GiveawayWinners
            MessageEffect
            MessageReactionCountUpdated
            MessageReactionUpdated
            MessageReactions
            Reaction
            ReactionCount
            ReactionType
            ReactionTypeEmoji
            ReactionTypeCustomEmoji
            ReactionTypePaid
            Thumbnail
            TranslatedText
            StrippedThumbnail
            SponsoredMessage
            Sticker
            WebPage
            ContactRegistered
            ScreenshotTaken
            DraftMessage
        """,
        chat_topics="""
        Chat Forum Topics
            ForumTopic
            ForumTopicCreated
            ForumTopicClosed
            ForumTopicEdited
            ForumTopicReopened
            GeneralForumTopicHidden
            GeneralForumTopicUnhidden
        """,
        bot_commands="""
        Bot Commands
            BotCommand
            BotCommandScope
            BotCommandScopeAllChatAdministrators
            BotCommandScopeAllGroupChats
            BotCommandScopeAllPrivateChats
            BotCommandScopeChat
            BotCommandScopeChatAdministrators
            BotCommandScopeChatMember
            BotCommandScopeDefault
        """,
        bot_keyboards="""
        Bot keyboards
            CallbackGame
            CallbackQuery
            CopyTextButton
            ForceReply
            GameHighScore
            InlineKeyboardButton
            InlineKeyboardMarkup
            KeyboardButton
            KeyboardButtonPollType
            KeyboardButtonPollTypeRegular
            KeyboardButtonPollTypeQuiz
            KeyboardButtonRequestChat
            KeyboardButtonRequestUsers
            ReplyKeyboardMarkup
            ReplyKeyboardRemove
            LoginUrl
            WebAppInfo
            MenuButton
            MenuButtonCommands
            MenuButtonWebApp
            MenuButtonDefault
            SentWebAppMessage
            SwitchInlineQueryChosenChat
        """,
        inline_mode="""
        Inline Mode
            ChosenInlineResult
            InlineQuery
            InlineQueryResult
            InlineQueryResultCachedAnimation
            InlineQueryResultCachedAudio
            InlineQueryResultCachedDocument
            InlineQueryResultCachedPhoto
            InlineQueryResultCachedSticker
            InlineQueryResultCachedVideo
            InlineQueryResultCachedVoice
            InlineQueryResultAnimation
            InlineQueryResultAudio
            InlineQueryResultDocument
            InlineQueryResultPhoto
            InlineQueryResultVideo
            InlineQueryResultVoice
            InlineQueryResultArticle
            InlineQueryResultContact
            InlineQueryResultGame
            InlineQueryResultLocation
            InlineQueryResultVenue
        """,
        authorization="""
        Authorization
            ActiveSession
            ActiveSessions
            SentCode
            TermsOfService
        """,
        input_media="""
        Input Media
            InputMedia
            InputMediaPhoto
            InputMediaVideo
            InputMediaAudio
            InputMediaAnimation
            InputMediaDocument
            InputPhoneContact
            LinkPreviewOptions
        """,
        input_paid_media="""
        Input Paid Media
            InputPaidMedia
            InputPaidMediaPhoto
            InputPaidMediaVideo
            PaidMediaPurchased
        """,
        input_message_content="""
        InputMessageContent
            InputMessageContent
            InputTextMessageContent
            InputLocationMessageContent
            InputVenueMessageContent
            InputContactMessageContent
            InputInvoiceMessageContent
        """,
        payments="""
        Payments
            BusinessConnection
            BusinessIntro
            BusinessLocation
            BusinessOpeningHours
            BusinessOpeningHoursInterval
            CollectibleItemInfo
            LabeledPrice
            Invoice
            ShippingAddress
            OrderInfo
            ShippingOption
            PaymentForm
            SuccessfulPayment
            RefundedPayment
            ShippingQuery
            PreCheckoutQuery
            StarAmount
            PaidReactionType
            PaidReactionTypeAnonymous
            PaidReactionTypeChat
            PaidReactionTypeRegular
        """
    )

    root = PYROGRAM_API_DEST + "/types"

    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    with open(HOME + "/template/types.rst") as f:
        template = f.read()

    with open(root + "/index.rst", "w") as f:
        fmt_keys = {}

        for k, v in categories.items():
            name, *types = get_title_list(v)

            fmt_keys.update({k: "\n    ".join(types)})

            # noinspection PyShadowingBuiltins
            for type in types:
                with open(root + "/{}.rst".format(type), "w") as f2:
                    title = "{}".format(type)

                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. autoclass:: pyrogram.types.{}()\n".format(type))

        f.write(template.format(**fmt_keys))

    # Bound Methods

    categories = dict(
        message="""
        Message
            Message.click
            Message.delete
            Message.download
            Message.forward
            Message.copy
            Message.pin
            Message.unpin
            Message.edit
            Message.edit_text
            Message.edit_cached_media
            Message.edit_caption
            Message.edit_media
            Message.edit_reply_markup
            Message.reply
            Message.reply_text
            Message.reply_animation
            Message.reply_audio
            Message.reply_cached_media
            Message.reply_chat_action
            Message.reply_contact
            Message.reply_document
            Message.reply_game
            Message.reply_inline_bot_result
            Message.reply_location
            Message.reply_media_group
            Message.reply_photo
            Message.reply_poll
            Message.reply_sticker
            Message.reply_venue
            Message.reply_video
            Message.reply_video_note
            Message.reply_voice
            Message.reply_invoice
            Message.get_media_group
            Message.react
            Message.read
            Message.view
            Message.translate
            Message.pay
            Message.star
            ReceivedGift.toggle
            ExternalReplyInfo.download
        """,
        chat="""
        Chat
            Chat.archive
            Chat.unarchive
            Chat.set_title
            Chat.set_description
            Chat.set_photo
            Chat.ban_member
            Chat.unban_member
            Chat.restrict_member
            Chat.promote_member
            Chat.get_member
            Chat.get_members
            Chat.add_members
            Chat.join
            Chat.leave
            Chat.mark_unread
            Chat.set_protected_content
            Chat.unpin_all_messages
            Chat.set_message_auto_delete_time
        """,
        user="""
        User
            User.archive
            User.unarchive
            User.block
            User.unblock
        """,
        callback_query="""
        Callback Query
            CallbackQuery.answer
            CallbackQuery.edit_message_text
            CallbackQuery.edit_message_caption
            CallbackQuery.edit_message_media
            CallbackQuery.edit_message_reply_markup
            ChosenInlineResult.edit_message_text
            ChosenInlineResult.edit_message_caption
            ChosenInlineResult.edit_message_media
            ChosenInlineResult.edit_message_reply_markup
        """,
        inline_query="""
        InlineQuery
            InlineQuery.answer
        """,
        pre_checkout_query="""
        PreCheckoutQuery
            PreCheckoutQuery.answer
        """,
        shipping_query="""
        ShippingQuery
            ShippingQuery.answer
        """,
        chat_join_request="""
        ChatJoinRequest
            ChatJoinRequest.approve
            ChatJoinRequest.decline
        """,
        story="""
        Story
            Story.react
            Story.download
        """,
        active_session="""
        ActiveSession
            ActiveSession.terminate
        """,
    )

    root = PYROGRAM_API_DEST + "/bound-methods"

    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    with open(HOME + "/template/bound-methods.rst") as f:
        template = f.read()

    with open(root + "/index.rst", "w") as f:
        fmt_keys = {}

        for k, v in categories.items():
            name, *bound_methods = get_title_list(v)

            fmt_keys.update({"{}_hlist".format(k): "\n    ".join("- :meth:`~{}`".format(bm) for bm in bound_methods)})

            fmt_keys.update(
                {"{}_toctree".format(k): "\n    ".join("{} <{}>".format(bm.split(".")[1], bm) for bm in bound_methods)})

            # noinspection PyShadowingBuiltins
            for bm in bound_methods:
                with open(root + "/{}.rst".format(bm), "w") as f2:
                    title = "{}()".format(bm)

                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. automethod:: pyrogram.types.{}()".format(bm))

        f.write(template.format(**fmt_keys))

    # Enumerations

    categories = dict(
        enums="""
        Enumerations
            ChatAction
            ChatEventAction
            ChatMemberStatus
            ChatMembersFilter
            ChatType
            ChatJoinType
            ClientPlatform
            MessageEntityType
            MessageMediaType
            MessageServiceType
            MessagesFilter
            ParseMode
            PollType
            ProfileColor
            AccentColor
            SentCodeType
            NextCodeType
            UserStatus
        """,
    )

    root = PYROGRAM_API_DEST + "/enums"

    shutil.rmtree(root, ignore_errors=True)
    os.mkdir(root)

    with open(HOME + "/template/enums.rst") as f:
        template = f.read()

    with open(root + "/cleanup.html", "w") as f:
        f.write("""<script>
  document
    .querySelectorAll("em.property")
    .forEach((elem, i) => i !== 0 ? elem.remove() : true)
  document
    .querySelectorAll("a.headerlink")
    .forEach((elem, i) => [0, 1].includes(i) ? true : elem.remove())
</script>""")

    with open(root + "/index.rst", "w") as f:
        fmt_keys = {}

        for k, v in categories.items():
            name, *enums = get_title_list(v)

            fmt_keys.update({"{}_hlist".format(k): "\n    ".join("{}".format(enum) for enum in enums)})

            fmt_keys.update(
                {"{}_toctree".format(k): "\n    ".join("{}".format(enum) for enum in enums)})

            # noinspection PyShadowingBuiltins
            for enum in enums:
                with open(root + "/{}.rst".format(enum), "w") as f2:
                    title = "{}".format(enum)

                    f2.write(title + "\n" + "=" * len(title) + "\n\n")
                    f2.write(".. autoclass:: pyrogram.enums.{}()".format(enum))
                    f2.write("\n    :members:\n")

                    f2.write("\n.. raw:: html\n    :file: ./cleanup.html\n")

        f.write(template.format(**fmt_keys))


def start():
    global page_template
    global toctree

    shutil.rmtree(DESTINATION, ignore_errors=True)

    with open(HOME + "/template/page.txt", encoding="utf-8") as f:
        page_template = f.read()

    with open(HOME + "/template/toctree.txt", encoding="utf-8") as f:
        toctree = f.read()

    generate(TYPES_PATH, TYPES_BASE)
    generate(FUNCTIONS_PATH, FUNCTIONS_BASE)
    generate(BASE_PATH, BASE_BASE)
    pyrogram_api()


if "__main__" == __name__:
    FUNCTIONS_PATH = "../../pyrogram/raw/functions"
    TYPES_PATH = "../../pyrogram/raw/types"
    BASE_PATH = "../../pyrogram/raw/base"
    HOME = "."
    DESTINATION = "../../docs/source/telegram"
    PYROGRAM_API_DEST = "../../docs/source/api"

    start()
